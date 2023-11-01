import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import typing as tp
from cycler import cycler
import os

MARKER = ["o","v","^","<",">","s","p"]

def plot_cdf_series(cdf_dict : tp.Dict[float,float], **kwargs):
    plt.step(x = cdf_dict.keys(),
             y = cdf_dict.values(),
             where = 'post',
             **kwargs)
# ===== #

def plot_cdf(cdf_list : tp.List[tp.Dict[float,float]],
             label : tp.List[str],
             filename : str = None,
             xlabel : str = '',
             has_markers : bool = None,
             legend_loc = 4):
    #plt.figure(figsize = (8,6))
    fig, ax = plt.subplots(figsize = (10,8))

    max_cdf_key = 0
    min_cdf_key = 100000

    for cdf in cdf_list:
        keys = list(cdf.keys())
        if len(keys) == 0: continue
        max_cdf_key = max(max_cdf_key,float(keys[-1]))
        min_cdf_key = min(min_cdf_key,float(keys[0]))

    cmap = plt.get_cmap('viridis')
    line_count = len(cdf_list)
    line_norm = [i/line_count for i in range(0,line_count)]
    line_color = cmap(line_norm)
    cycle_step = 0

    for cdf in cdf_list:
        if max_cdf_key not in cdf: cdf[max_cdf_key] = 1
        cdf[0] = 0
        cdf = dict(sorted(cdf.items()))
        plot_cdf_series(cdf, 
                        label = label[cycle_step], 
                        marker = MARKER[cycle_step] if has_markers else None,
                        color = line_color[cycle_step],
                        linestyle = (0,(3*(cycle_step+1),1*cycle_step)),
                        linewidth = 4,
                        markevery = (10, len(cdf.keys())))
        cycle_step += 1

    for dir in ['top','bottom','left','right']:
        ax.spines[dir].set_linewidth(4)
    ax.xaxis.set_tick_params(width=4)
    ax.yaxis.set_tick_params(width=4)

    plt.subplots_adjust(left=0.15, right=0.95, top=0.8, bottom=0.2)
    plt.xlabel(xlabel, fontsize = 30, labelpad = 20)
    plt.ylabel('Cumulative Fraction of Changes', fontsize=30, labelpad = 20)
    plt.yticks(np.arange(0,1.1,0.2), fontsize = 30)
    plt.xticks(fontsize = 30)
    plt.ylim(0,1)
    plt.legend(loc = legend_loc, fontsize = 20)
    plt.tick_params(axis = 'both', direction = 'in')
    if filename : plt.savefig(filename)
# ===== #