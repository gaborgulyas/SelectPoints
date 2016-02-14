# Routine to select some points in matplotlib

In some cases it might be handy if you could put on an outline on some points in your plots. This exactly is what this code is intended to do. Like this:

![Example](/example.png)

It is relatively easy to use the `selectpoints()` function, use this by default, where the second variable should be a list of your point coordinates:
	selectpoints(ax, points)
However, there are some additional parameters:
* `radius`: 
* `path_type`: how polygon points are connected (possible values: `matplotlib.path.Path.LINETO`, `matplotlib.path.Path.CURVE3`, or `matplotlib.path.Path.CURVE4`) 
* `ec`: outline color
* `ls`: line style string
* `lw`: line widht
* `fc`: fill color 
* `a`: alpha
* `fill`: fill the polygon or not
* `js`: polygon line join style

You can also play around with the example.py to test its features.

Any comments or suggestions? Contact me. Improvements are also welcome as this was written mainly in a mainly quick-and-dirty approach. :)