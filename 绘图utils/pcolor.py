"""
pcolor/pcolormesh的基本用法
记住一点：假如数据在矩形区域内建议使用imshow，这样速度更快。此例子展示imshow不能使用的场景

"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cbook import get_sample_data

import example_utils

# 拿到数据 ...
z = np.load(get_sample_data('./bivariate_normal.npy'))
ny, nx = z.shape
y, x = np.mgrid[:ny, :nx]
y = (y - y.mean()) * (x + 10)**2

mask = (z > -0.1) & (z < 0.1)
z2 = np.ma.masked_where(mask, z)

fig, axes = example_utils.setup_axes()

# pcolor 或 pcolormesh 都可，后者效率更高
axes[0].pcolor(x, y, z, cmap='gist_earth')
example_utils.label(axes[0], 'either')

# pcolor和pcolormesh的不同展示
# 使用pcolor
axes[1].pcolor(x, y, z2, cmap='gist_earth', edgecolor='black')
example_utils.label(axes[1], 'pcolor(x,y,z)')

# 使用pcolormesh
axes[2].pcolormesh(x, y, z2, cmap='gist_earth', edgecolor='black', lw=0.5,
                   antialiased=True)
example_utils.label(axes[2], 'pcolormesh(x,y,z)')

#example_utils.title(fig, 'pcolor/pcolormesh: Colormapped 2D arrays')
fig.savefig('pcolor_example.png', facecolor='none')

plt.show()
