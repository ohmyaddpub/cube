import math
import json
import seaborn as sns
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


ylabel = ["%02d" % i for i in range(1, 14)]
xlabel = ["%02d" % i for i in range(6, 55)]
with open("data2.json") as f:
    datas = np.array(json.load(f))


fig, ax = plt.subplots()
im = ax.imshow(datas, cmap=plt.cm.hot_r)

# We want to show all ticks...
plt.xlabel("Number of Differences")
plt.ylabel("Length of Actions")
ax.set_xticks(np.arange(len(xlabel)))
ax.set_yticks(np.arange(len(ylabel)))
# ... and label them with the respective list entries
ax.set_xticklabels(xlabel)
ax.set_yticklabels(ylabel)
#plt.colorbar(im)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=60, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
"""
for i in range(len(ylabel)):
    for j in range(len(xlabel)):
        if datas[i, j] == 0.0:
            text = ax.text(j, i, -20,
                           ha="center", va="center", color="b")
        else:
            text = ax.text(j, i, math.log(datas[i, j], 10),
                           ha="center", va="center", color="b")
"""



fig.tight_layout()
plt.savefig("../jscube/data1.png")