"""
Matplotlib 提供许多专业的绘制统计学相关的图函数

更多统计学相关图可使用 Seaborn 库，它基于Matplotlib编写。 
"""
import numpy as np
import matplotlib.pyplot as plt

import example_utils


def main():
    colors = ['cyan', 'red', 'blue', 'green', 'purple']
    dists = generate_data()

    fig, axes = example_utils.setup_axes()
    hist(axes[0], dists, colors)
    boxplot(axes[1], dists, colors)
    violinplot(axes[2], dists, colors)

    # example_utils.title(fig, 'hist/boxplot/violinplot: Statistical plotting',
    #                     y=0.9)
    fig.savefig('statistical_example.png', facecolor='none')

    plt.show()


def generate_data():
    means = [0, -1, 2.5, 4.3, -3.6]
    sigmas = [1.2, 5, 3, 1.5, 2]
    # 每一个分布的样本个数
    nums = [150, 1000, 100, 200, 500]

    dists = [np.random.normal(*args) for args in zip(means, sigmas, nums)]
    return dists

# 频率分布直方图
def hist(ax, dists, colors):
    #ax.set_color_cycle(colors)
    for dist in dists:
        ax.hist(dist, bins=20, density=True, edgecolor='none', alpha=0.5)

    ax.margins(y=0.05)
    ax.set_ylim(bottom=0)

    example_utils.label(ax, 'ax.hist(dists)')

# 箱型图
def boxplot(ax, dists, colors):
    result = ax.boxplot(dists, patch_artist=True, notch=True, vert=False)

    for box, color in zip(result['boxes'], colors):
        box.set(facecolor=color, alpha=0.5)
    for item in ['whiskers', 'caps', 'medians']:
        plt.setp(result[item], color='gray', linewidth=1.5)
    plt.setp(result['fliers'], markeredgecolor='gray', markeredgewidth=1.5)
    plt.setp(result['medians'], color='black')

    ax.margins(0.05)
    ax.set(yticks=[], ylim=[0, 6])

    example_utils.label(ax, 'ax.boxplot(dists)')

#小提琴图
def violinplot(ax, dists, colors):
    result = ax.violinplot(dists, vert=False, showmedians=True)
    for body, color in zip(result['bodies'], colors):
        body.set(facecolor=color, alpha=0.5)
    for item in ['cbars', 'cmaxes', 'cmins', 'cmedians']:
        plt.setp(result[item], edgecolor='gray', linewidth=1.5)
    plt.setp(result['cmedians'], edgecolor='black')

    ax.margins(0.05)
    ax.set(ylim=[0, 6])

    example_utils.label(ax, 'ax.violinplot(dists)')


main()