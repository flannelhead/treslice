# treslice
Visualize 3D data easily!

Usage
-----
treslice takes arrays X, Y, Z and C as inputs. X, Y and Z contain the coordinates of the gridpoints, C contains the function values at the gridpoints. It then lets you view colour maps of slices of the data. You can switch slices with up, down, right and left arrows. Pressing space changes the axes. The underlying implementation relies on matplotlib and specifically [pcolormesh](http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.pcolormesh) – you should consult that for more information.

You can call TreSlice from a Python script:
```python
  import numpy as np
  from treslice import TreSlice
  
  grid = np.linspace(0, 1, 11)
  X, Y, Z = np.meshgrid(grid, grid, grid)
  C = X + Y + Z
  plot = TreSlice(grid, grid, grid, C)
  plot.show()
```

Given your grid and the values in a NumPy .npz file as arrays X, Y, Z and Z, you can call treslice from the command line:
```
  python treslice.py datafile.npz
```
or, having treslice.py in your `PYTHONPATH`,
```
  python -m treslice datafile.npz
```
