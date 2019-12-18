import numpy as np
import matplotlib.pylab as pl

nx = 4
ny = 5
data = np.random.randint(0, 10, size=(ny,nx))

pl.figure()
tb = pl.table(cellText=data, loc=(0, 0), cellLoc='center')

tc = tb.properties()['child_artists']
for cell in tc:
    cell.set_height(1/ny)
    cell.set_width(1/nx)

ax = pl.gca()
ax.set_xticks([])
ax.set_yticks([])

pl.show()
