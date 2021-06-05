import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns; sns.set_theme()
from more_itertools import interleave

def converter(s):
  if s == b'-':
    return np.double(-1)
  else:
    return np.double(s)

def nanconverter(s):
  return np.double(s)

def accumulate(data, buckets):
  totals = {buck : 0 for buck in buckets}
  for point in data:
    added = False
    for buck in buckets:
      if point <= buck and not added:
        totals[buck] += 1
        added = True
      else:
        continue
      
  return list(totals.values())

def log_range(number, center):
  return [center * 10**(x-int(number/2)) for x in range(1,number+1)]

def plot_error():

  treatments = ["baseline", "nt-all", "nt-none"]
  names = ["Avg RMS"]
  dtypes = [("Avg RMS", np.double)]
  csvs_3 = [
    np.genfromtxt(
      'noise/3/' + pref + '.csv', 
      delimiter=",", skip_header=1, names=names, usecols=2, 
      converters={2: converter}, 
      ) for pref in treatments]
  csvs_10 = [
    np.genfromtxt(
      'noise/10/' + pref + '.csv', 
      delimiter=",", skip_header=1, names=names, usecols=2, 
      converters={2: converter}, 
      ) for pref in treatments]

  buckets_tail = [1, 5, 10, 50, 100, 500]
  buckets = [-1] + [1, 5, 10, 50, 100, 500]
  base_3, base_10 = accumulate(csvs_3[0], buckets), accumulate(csvs_10[0], buckets)
  ntall_3, ntall_10 = accumulate(csvs_3[1], buckets), accumulate(csvs_10[1], buckets)
  ntnone_3, ntnone_10 = accumulate(csvs_3[2], buckets), accumulate(csvs_10[2], buckets)


  fig, ax = plt.subplots()

  cmap = cm.get_cmap('Blues')

  results = [base_3, ntnone_3, ntall_3]
  xticklabels = ["Timeout"] + [ str(x) for x in buckets_tail]
  yticklabels = ["baseline", "nt-none", "nt-all"]
  
  sns.heatmap(results, cmap=cmap, linewidths=0.5, fmt="d", annot=True, xticklabels=xticklabels, yticklabels=yticklabels)
  ax.set_xlabel('RMSD error')

  for label in ax.get_yticklabels():
    label.set_rotation(0)

  plt.gcf().set_size_inches(12, 3)
  save_fig(plt, "error_3", 6, 2.5)

  fig.clear(True)

  fig, ax1 = plt.subplots()
  results = [base_10, ntnone_10, ntall_10]
  xticklabels = ["Timeout"] + [ str(x) for x in buckets_tail ]
  yticklabels = ["baseline", "nt-none", "nt-all"]
  
  sns.heatmap(results, cmap=cmap, linewidths=0.5, fmt="d", annot=True, xticklabels=xticklabels, yticklabels=yticklabels)
  ax1.set_xlabel('RMSD error')

  for label in ax1.get_yticklabels():
    label.set_rotation(0)
  
  plt.gcf().set_size_inches(12, 3)
  save_fig(plt, "error_10", 6, 2.5)

def plot_error_android():

  names = ["Avg RMS"]
  dtypes = [("Avg RMS", np.double)]
  csv = np.genfromtxt(
     'android/android_results.csv', 
      delimiter=",", skip_header=1, names=names, usecols=3, 
      converters={3: converter}, 
      )

  buckets_tail = [1, 5, 10, 50, 100, 500]
  buckets = [-1] + buckets_tail
  results = accumulate(csv, buckets) 
  fig, ax = plt.subplots()

  cmap = cm.get_cmap('Blues')
  xticklabels = ["Timeout"] + [ str(x) for x in buckets_tail]
  yticklabels = False
  
  sns.heatmap([results], cmap=cmap, linewidths=0.5, fmt="d", annot=True, xticklabels=xticklabels, yticklabels=yticklabels)
  ax.set_xlabel('RMSD error')

  for label in ax.get_yticklabels():
    label.set_rotation(0)

  save_fig(plt, "android_error", 6, 0.66)

  fig.clear(True)

def plot_accuracy_android():

  names = ["Accuracy"]
  dtypes = [("Accuracy", np.double)]
  csv = np.genfromtxt(
     'android/android_results.csv', 
      delimiter=",", skip_header=1, names=names, usecols=7, 
      converters={7: converter}, 
      )

  buckets_tail = [x/10.0 for x in range(11)]
  buckets = [-1] + buckets_tail
  results = accumulate(csv, buckets) 
  fig, ax = plt.subplots()

  cmap = cm.get_cmap('Blues')
  xticklabels = ["Timeout"] + [ str(x) for x in buckets_tail]
  yticklabels = False
  
  sns.heatmap([results], cmap=cmap, linewidths=0.5, fmt="d", annot=True, xticklabels=xticklabels, yticklabels=yticklabels)

  ax.set_xlabel('Accuracy (percentage)')

  for label in ax.get_yticklabels():
    label.set_rotation(0)

  plt.gcf().set_size_inches(6, 0.66)
  save_fig(plt, "android_accuracy", 6, 0.66)


def plot_accuracy():

  treatments = ["baseline", "nt-all", "nt-none"]
  names = ["Accuracy"]
  dtypes = [("Accuracy", np.double)]
  csvs_3 = [
    np.genfromtxt(
      'noise/3/' + pref + '.csv', 
      delimiter=",", skip_header=1, names=names, usecols=4, 
      converters={4: converter}, 
      ) for pref in treatments]
  csvs_10 = [
    np.genfromtxt(
      'noise/10/' + pref + '.csv', 
      delimiter=",", skip_header=1, names=names, usecols=4, 
      converters={4: converter}, 
      ) for pref in treatments]

  buckets = [-1] + [x/10.0 for x in range(11)]
  base_3, base_10 = accumulate(csvs_3[0], buckets), accumulate(csvs_10[0], buckets)
  ntall_3, ntall_10 = accumulate(csvs_3[1], buckets), accumulate(csvs_10[1], buckets)
  ntnone_3, ntnone_10 = accumulate(csvs_3[2], buckets), accumulate(csvs_10[2], buckets)

  fig, ax = plt.subplots()
  cmap = cm.get_cmap('Blues')

  results = [base_3, ntnone_3, ntall_3]
  yticklabels = ["baseline", "nt-none", "nt-all"]

  xticklabels = ["Timeout"] + [ str(x*10) + "%" for x in range(11)]
  sns.heatmap(results, cmap=cmap, linewidths=0.5, fmt="d", annot=True, xticklabels=xticklabels, yticklabels=yticklabels)
  ax.set_xlabel('Accuracy (percent)')

  for label in ax.get_yticklabels():
    label.set_rotation(0)

  save_fig(plt, "accuracy_3", 6, 2.5)

  fig.clear(True)



  fig, ax1 = plt.subplots()
  results = [base_10, ntnone_10, ntall_10]
  yticklabels = ["baseline", "nt-none", "nt-all"]

  xticklabels = ["Timeout"] + [ str(x*10) + "%" for x in range(11)]
  sns.heatmap(results, cmap=cmap, linewidths=0.5, fmt="d", annot=True, xticklabels=xticklabels, yticklabels=yticklabels)
  ax1.set_xlabel('Accuracy (percent)')

  for label in ax1.get_yticklabels():
    label.set_rotation(0)

  plt.gcf().set_size_inches(6, 2.5)
  save_fig(plt, "accuracy_10", 6, 2.5)



def plot_synth_time():

  treatments = ["baseline", "nt-all", "nt-none"]
  names = ["Synth time"]
  dtypes = [("Synth time", np.double)]
  csvs_3 = [
    np.genfromtxt(
      'noise/3/' + pref + '.csv', 
      delimiter=",", skip_header=1, names=names, usecols=8, 
      dtype=np.double,
      converters={8: nanconverter}, 
      invalid_raise=False, 
      ) for pref in treatments]
  csvs_10 = [
    np.genfromtxt(
      'noise/10/' + pref + '.csv', 
      delimiter=",", skip_header=1, names=names, usecols=8, 
      dtype=np.double,
      converters={8: nanconverter}, 
      invalid_raise=False, 
      ) for pref in treatments]


  base_3 = csvs_3[0]
  ntall_3 = csvs_3[1]
  ntnone_3 = csvs_3[2]

  base_10 = csvs_10[0]
  ntall_10 = csvs_10[1]
  ntnone_10 = csvs_10[2]

  inset = False

  results_3 = [base_3, ntnone_3, ntall_3]
  results_10 = [base_10, ntnone_10, ntall_10]

  for idx in range(len(results_3)):
    results_3[idx] = results_3[idx][np.where(~np.isnan(results_3[idx]))]
  for idx in range(len(results_10)):
    results_10[idx] = results_10[idx][np.where(~np.isnan(results_10[idx]))]
  

  fig, ax = plt.subplots()

  results_3 = [np.sort(x) for x in results_3]
  results_10 = [np.sort(x) for x in results_10]

  # plt.subplot(1,2,1)
  xlim = 180
  ylim = max(*list(map(len, results_3)))
  # print(ylim)
  ylim = 180 # this makes a nicer graph
  plt.xlim([0, xlim])
  plt.ylim([0, ylim])
  # targs = [(results_3)]
  colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
  lines = ['-.', '--', '-', ':']
  # markers = ['.', '^', 'x', None]
  markers = [None, None, None, None]
  labels = ['baseline', 'nt-none', 'nt-all', 'total']

  xvals = results_3 + [range(xlim)]
  yvals = [range(len(x)) for x in results_3] + [[max(*list(map(len, results_3))) for _ in range(xlim)]]

  for idx in range(len(xvals)):
    ax.plot(xvals[idx], yvals[idx], label=labels[idx], marker=markers[idx], color=colors[idx], linestyle=lines[idx])
    
    extra_x = [x for x in range(xlim) if x > xvals[idx][-1]]
    extra_y = [yvals[idx][-1] for _ in extra_x]

    ax.plot(extra_x, extra_y, label=None, marker=None, color=colors[idx], linestyle=lines[idx])

  ax.legend()
  ax.set_ylabel('Number of solved benchmarks')
  ax.set_xlabel('Synthesis time (seconds)')

  if inset:
    plt.axes([.4, .3, .3, .3], facecolor='y')
    # plt.axes([.3, .35, .3, .3], facecolor='y')
    plt.xlim([80, 180])
    plt.ylim([150, 180])

    for idx in range(len(xvals)):
      plt.plot(xvals[idx], yvals[idx], label=labels[idx], marker=markers[idx], color=colors[idx], linestyle=lines[idx])
      
      extra_x = [x for x in range(xlim) if x > xvals[idx][-1]]
      extra_y = [yvals[idx][-1] for _ in extra_x]

      plt.plot(extra_x, extra_y, label=None, marker=None, color=colors[idx], linestyle=lines[idx])
  
  save_fig(plt, "synthtime_3", 6, 2.5)

  fig.clear(True)
  fig, ax = plt.subplots()
  
  xlim = 180
  ylim = max(*list(map(len, results_10)))
  ylim = 180 # this makes a nicer graph
  plt.xlim([0, xlim])
  plt.ylim([0, ylim])
  colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
  lines = ['--', '-.', '-', ':']
  # markers = ['.', '^', 'x', None]
  markers = [None, None, None, None]
  labels = ['baseline', 'nt-none', 'nt-all', 'total']

  xvals = results_10 + [range(xlim)]
  yvals = [range(len(x)) for x in results_10] + [[max(*list(map(len, results_10))) for _ in range(xlim)]]

  for idx in range(len(xvals)):
    ax.plot(xvals[idx], yvals[idx], label=labels[idx], marker=markers[idx], color=colors[idx], linestyle=lines[idx])
    
    extra_x = [x for x in range(xlim) if x > xvals[idx][-1]]
    extra_y = [yvals[idx][-1] for _ in extra_x]

    ax.plot(extra_x, extra_y, label=None, marker=None, color=colors[idx], linestyle=lines[idx])


  # ax.set_title('3 Training Examples')
  ax.legend()
  ax.set_ylabel('Number of solved benchmarks')
  ax.set_xlabel('Synthesis time (seconds)')

  if inset:
    plt.axes([.4, .3, .3, .3], facecolor='y')
    # plt.axes([.3, .35, .3, .3], facecolor='y')
    plt.xlim([80, 180])
    plt.ylim([150, 180])

    for idx in range(len(xvals)):
      plt.plot(xvals[idx], yvals[idx], label=labels[idx], marker=markers[idx], color=colors[idx], linestyle=lines[idx])
      
      extra_x = [x for x in range(xlim) if x > xvals[idx][-1]]
      extra_y = [yvals[idx][-1] for _ in extra_x]

      plt.plot(extra_x, extra_y, label=None, marker=None, color=colors[idx], linestyle=lines[idx])
  
  save_fig(plt, "synthtime_10", 6, 2.5)


# TODO: factor out dims
def save_fig(plt, name, x, y):
  plt.gcf().set_size_inches(x, y)
  plt.savefig(name + ".png", bbox_inches = 'tight', pad_inches = 0.03, dpi=300)

  
# plot_synth_time()
# plot_accuracy()
# plot_error()
# plot_error_android()
# plot_accuracy_android()
