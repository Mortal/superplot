import math
import matplotlib

def matplotlib_setup():
    fig_width_pt = 341.0
    inches_per_pt = 1.0/72.27
    golden_mean = (math.sqrt(5)-1.0)/2.0
    fig_width = fig_width_pt*inches_per_pt
    fig_height = fig_width*golden_mean
    fig_size = [fig_width,fig_height]

    matplotlib.use('ps')
    matplotlib.rc('font', size=10, family='serif')
    matplotlib.rc('axes', labelsize=10)
    matplotlib.rc('legend', fontsize=8)
    matplotlib.rc('xtick', labelsize=8)
    matplotlib.rc('ytick', labelsize=8)
    matplotlib.rc('text', usetex=True)
    matplotlib.rc('figure', figsize=fig_size)

matplotlib_setup()

import matplotlib.pyplot as plt


def plot_init(xlabel, ylabel):
    fig, ax = plt.subplots()
    hmargin = 0.12
    fig.subplots_adjust(left=hmargin, bottom=0.15, right=1 - hmargin, top=0.95)
    # fig.suptitle(title)
    ax.grid()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    return fig, ax


fig, ax = plot_init(r'My $x$ label', r'My $y$ label')
ax.plot([0, 1, 1, 0], [0, 0, 1, 1], 'rx-', label='Some data')
ax.legend(loc='upper right')
fig.savefig('plot.pdf')
