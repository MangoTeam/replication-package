The following supplements FSE 2021 submission #24, Synthesis of Web Layouts from Examples:
1. Scraped website layout data, suitable for open access. This is found in the `layouts/` subdirectory. It contains a corpus of layouts in JSON format with filenames corresponding to our submission's scraped layouts.
2. A video demonstration `website-difference.mp4` of the visual difference between our algorithm's predicted
layout for a complex website, and the actual rendered layout of the website.
For visualization purposes we render each layer of the view hierarchy a different color.
Despite the visibly and intuitively low error, the computed accuracy is actually around 50%.
his video demonstrates why RMSD error is a better measurement than accuracy. 