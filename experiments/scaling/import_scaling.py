f = open(r"scaling_data.csv")
lines = f.readlines()
f.close()
headers = lines[0]
lines = [[x.strip() for x in y.split(',')] for y in lines[1:]]
bench = set([x[0] for x in lines])


for b in bench:
    benchlines = list(filter(lambda x: x[0] == b, lines))
    maxelem = max([int(x[2]) for x in benchlines])
    res = (list(reversed([sum([float(y[4]) if y[4] != '-' else 121.0 for y in filter(lambda x: x[2] == str(i), benchlines)])/5 for i in range(1,maxelem+1)])))
    print(b + "," + ",".join([str(x) for x in res]))
