from __future__ import annotations
from matplotlib import pyplot as plt
from matplotlib import rc
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

rc('text', usetex=True)
 

# Define a wrapper class for the loaded function
class HashableFunctionWrapper:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __hash__(self):
        # Create a unique hash based on the function's code
        return hash(self.func.__code__.co_code)
                    

plt.rcParams.update({
    "text.usetex"        : True,
    "font.family"        : "Helvetica",
    'font.size'          : 15,
    'xtick.top'          : True,
    'ytick.right'        : True,
    'xtick.direction'    : 'in',
    'ytick.direction'    : 'in',
    'xtick.major.size'   : 5,
    'xtick.minor.size'   : 3,
    'ytick.major.size'   : 5,
    'ytick.minor.size'   : 3,
    'xtick.labelsize'    : 18,
    'ytick.labelsize'    : 18
})
def PowerTen(num,pos=None):
    if (num==0.):
        return "$0$"
    decimal_digits=3
    exponent=int(np.floor(np.log10(abs(num))))
    coeff=round(num/float(10**exponent),decimal_digits)
    # if (exponent==0.):
    #     return "${:.2f}$".format(coeff)
    if (coeff==1.):
        return r"$10^{{{:d}}}$".format(exponent)
    else:
        return r"${0:.1f}\times10^{{{1:d}}}$".format(coeff,exponent)
    
path_data = "./data/"
path_out = "./results/"


def FracClip(x):
    return 1/np.clip(x, 1e-20, None)
  
def LogTicks(beg,end,mod=2,even=0):
    beg = int(beg)
    end = int(end)
    ticks  = np.logspace(beg,end,end-beg+1)
    labels = []
    
    for i,num in enumerate(ticks):
        if i%mod == even: 
            labels.append(PowerTen(num)) 
        else:
            labels.append("") 
    return ticks,labels


def set_ymix(ax,beg,end,endlin,mod=2,even=0,rot=0,size=1.5):
 
    ax.set_yscale("log")
    ax.set_ylim((10**beg,10**end))
    ymajticks,ylabels =  LogTicks(beg,end,mod,even)     
    ax.set_xticks(ymajticks,labels=ylabels)
    # ax.xaxis.set_major_formatter(mpl.ticker.NullFormatter())
    y_minor = mpl.ticker.LogLocator(base = 10.0, subs = np.arange(1.0, 10.0) * 0.1, numticks = 999)
    ax.yaxis.set_minor_locator(y_minor)
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    if rot: ax.yaxis.set_tick_params(rotation=rot)
    ax.spines['top'].set_visible(False)
    # ax.yaxis.set_ticks_position('bottom')

    # otherhalf (linear)
    divider = make_axes_locatable(ax)
    axLin = divider.append_axes("top", size=size, pad=0, sharex=ax)

    axLin.set_xscale('linear')
    axLin.set_ylim((10**end, 10**endlin))

    # Removes bottom axis line
    axLin.spines['bottom'].set_visible(False)
    axLin.xaxis.set_ticks_position('top')
    plt.setp(axLin.get_xticklabels(), visible=False)

    return axLin


def set_xlogticks(ax,beg,end,mod=2,even=0,rot=0):
    ax.set_xscale("log")
    ax.set_xlim(10**beg,10**end)
    xmajticks,xlabels =  LogTicks(beg,end,mod,even)     
    ax.set_xticks(xmajticks,labels=xlabels)
    # ax.xaxis.set_major_formatter(mpl.ticker.NullFormatter())
    x_minor = mpl.ticker.LogLocator(base = 10.0, subs = np.arange(1.0, 10.0) * 0.1, numticks = 999)
    ax.xaxis.set_minor_locator(x_minor)
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())
    if rot: ax.xaxis.set_tick_params(rotation=rot)
    

def set_ylogticks(ax,beg,end,mod=2,even=0,rot=0,nolab=0):
    ax.set_yscale("log")
    ymajticks,ylabels =  LogTicks(beg,end,mod,even)     
    ax.set_yticks(ymajticks,labels=ylabels)
    # ax.yaxis.set_major_formatter(mpl.ticker.NullFormatter())
    y_minor = mpl.ticker.LogLocator(base = 10.0, subs = np.arange(1.0, 10.0) * 0.1, numticks = 999)
    ax.yaxis.set_minor_locator(y_minor)
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter()) 
    if nolab: ax.yaxis.set_major_formatter(mpl.ticker.NullFormatter()) 
    if rot: ax.yaxis.set_tick_params(rotation=rot)
    ax.set_ylim(10**beg,10**end)

def set_cblogticks(cb,beg,end,mod=2,even=0,rot=0,nolab=0):
    ymajticks,ylabels =  LogTicks(beg,end,mod,even)     
    y_minor = mpl.ticker.LogLocator(base = 10.0, subs = np.arange(1.0, 10.0) * 0.1, numticks = 999)
    cb.set_ticks(y_minor,labels=ylabels)
    if nolab: cb.set_ticklabels([])

 


def set_xlinticks(ax,multmaj,mult):
    xlocmaj = mpl.ticker.MultipleLocator(multmaj) 
    ax.xaxis.set_major_locator(xlocmaj)
    x_minor = mpl.ticker.MultipleLocator(mult)
    ax.xaxis.set_minor_locator(x_minor)
    ax.xaxis.set_minor_formatter(mpl.ticker.NullFormatter())

def set_ylinticks(ax,multmaj,mult,nolab=0):
    ylocmaj = mpl.ticker.MultipleLocator(multmaj) 
    ax.yaxis.set_major_locator(ylocmaj)
    y_minor =mpl.ticker.MultipleLocator(mult)
    ax.yaxis.set_minor_locator(y_minor)
    ax.yaxis.set_minor_formatter(mpl.ticker.NullFormatter()) 
    if nolab: ax.yaxis.set_major_formatter(mpl.ticker.NullFormatter()) 
    
