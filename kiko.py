#!/usr/bin/env python

import matplotlib.pyplot as plt

# TABLE OF CONTENTS

# largeTickLabels
# prettyGrid

def largeTickLabels(ax,fontsize=20):
    
    [ii.set(fontsize=fontsize) for ii in ax.get_xticklabels()];
    [ii.set(fontsize=fontsize) for ii in ax.get_yticklabels()];
    
    return ax

def prettyGrid(ax,color=(0.8,0.8,0.8),lw=1.5):

    for ss in ax.spines:
        ax.spines[ss].set(color=color,lw=lw)   

    ax.grid(color=color,lw=lw)
