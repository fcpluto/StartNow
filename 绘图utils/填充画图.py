"""
fill函数的各种用法
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils


# -- 产生数据 ----------------------


def stackplot_data():
    x = np.linspace(0, 10, 100)
    y = np.random.normal(0, 1, (5, 100))
    y = y.cumsum(axis=1)
    y -= y.min(axis=0, keepdims=True)
    return x, y


def sin_data():
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    y2 = np.cos(x)
    return x, y, y2


def fill_data():
    t = np.linspace(0, 2*np.pi, 100)
    r = np.random.normal(0, 1, 100).cumsum()
    r -= r.min()
    return r * np.cos(t), r * np.sin(t)


def fill_example(ax):
    # fill一个多边形区域
    x, y = fill_data()
    ax.fill(x, y, color='lightblue')
    ax.margins(0.1)
    example_utils.label(ax, 'fill')


def fill_between_example(ax):
    # 两条线间填充
    x, y1, y2 = sin_data()

    # fill_between的最常用法1
    err = np.random.rand(x.size)**2 + 0.1
    y = 0.7 * x + 2
    ax.fill_between(x, y + err, y - err, color='orange')

    # 最常用法2:两条曲线相交区域对应不同填充色
    ax.fill_between(x, y1, y2, where=y1 > y2, color='lightblue')
    ax.fill_between(x, y1, y2, where=y1 < y2, color='forestgreen')

    # 最常用法3
    ax.fill_betweenx(x, -y1, where=y1 > 0, color='red', alpha=0.5)
    ax.fill_betweenx(x, -y1, where=y1 < 0, color='blue', alpha=0.5)

    ax.margins(0.15)
    example_utils.label(ax, 'fill_between/x')


def stackplot_example(ax):
    # Stackplot就是多次调用 ax.fill_between
    x, y = stackplot_data()
    ax.stackplot(x, y.cumsum(axis=0), alpha=0.5)
    example_utils.label(ax, 'stackplot')


def main():
    fig, axes = example_utils.setup_axes()

    fill_example(axes[0])
    fill_between_example(axes[1])
    stackplot_example(axes[2])

    # example_utils.title(fig, 'fill/fill_between/stackplot: Filled polygons',
    #                     y=0.95)
    fig.savefig('fill_example.png', facecolor='none')
    plt.show()


main()