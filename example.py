import numpy as np
import matplotlib.pyplot as plt
from selectpoints import selectpoints

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = ["r"  if c > .75 else "b" for c in np.random.rand(N)]

pts = []
for ix in range(N):
	if colors[ix] == "r":
		pts.append([x[ix], y[ix]])

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
c, r = selectpoints(ax, pts, radius=.05, ec='r', fill=False)
print "center:", c
print "radius:", r

plt.scatter(x, y, s=30, c=colors, alpha=0.5)
plt.savefig("example.png")