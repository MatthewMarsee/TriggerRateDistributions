import numpy as np
import csv
import math

import matplotlib.pyplot as plt
plt.rcParams['axes.facecolor'] = 'white'
import matplotlib as mpl
mpl.rcParams['figure.dpi'] = 300

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

stations = [11,12,13,14,21,22,23,24]
colors = ['yellow','orange','red','magenta','lawngreen','cyan','blue','purple']


#=======================================================#
def getData(station,filename):
    #> Access data in csv from grafana data grabber
    data = []
    with open(filename,'r') as rdf:
        for i,line in enumerate(csv.reader(rdf)):
            if i==0:
                params = line
                data = [[] for par in line]
            else:
                if float(line[[j for j,p in enumerate(params) if 'trigger rate' in p][0]]) <0: #ignore runs with trigger rates around -1000
                    continue
                for ip,p in enumerate(params):
                    if 'run ids' in p:
                        data[ip].append(int(float(line[ip])))
                    else:
                        data[ip].append(float(line[ip]))
    return np.array(data)


def getRunType(station,run,runtable):
    #>Get run type from runtable
    headers = ['run_type']

    mask_station = (runtable['station'] == int(station))
    mask_run = (runtable['run'] == int(run))
    mask = mask_station * mask_run

    res = runtable[mask][headers].values
    if len(res)==0:
        return 'MISSING'
    else:
        return res[0][0]



#=============#

def plotHist(station,param_data,param_name,param_unit,bin_width):
    #>Plot trigger rates for all runs of a station 

    plt.axvline(2,c='r',linestyle=':',label='2Hz')

    bins = np.arange(math.floor(np.min(param_data)), math.ceil(np.max(param_data)) + bin_width, bin_width)
    plt.hist(param_data,bins=bins,color=colors[stations.index(station)],label=f'N = {len(param_data)}\n  '+
                                                                            r'$\mu$'+f' = {np.round(np.mean(param_data),3)}\n  '+
                                                                            r'$\sigma$'+f' = {np.round(np.std(param_data),3)}'
                                                                            )
    plt.suptitle(f'{param_name}s per Run: Station {station}\n2021 - 2025')
    plt.xlabel(f'{param_name} [{param_unit}]')
    plt.ylabel('Count')
    plt.yscale('log')
    plt.legend()
    filename =  f'{param_name.replace(" ","")}s_Station{station}.png'
    plt.savefig(filename,dpi=300)
    print(f'Plot saved to {filename}')
    plt.show()


def plotRunTypeHist(station,param_data,param_name,param_unit,bin_width,runtypes,physonly=False):
    #>Plot trigger rates, sorting by trigger types.
    #>Option to only show physics runs (no calibration or broken runs will be used in the analysis)

    plt.axvline(2,c='r',linestyle=':',label=f'2 {param_unit} upper bound')
    hatches = ['x','-','o']

    counter=0
    for k, rType in enumerate(runtypes):
        if physonly and not (rType=='physics'):
            continue
        bins = np.arange(math.floor(np.min(param_data[k])), math.ceil(np.max(param_data[k])) + bin_width, bin_width)
        plt.hist(param_data[k],hatch=hatches[k],alpha = 0.5,bins=bins,
                                               label=f'{rType[0].capitalize()+rType[1:]}\n'+
                                               f'  N = {len(param_data[k])}\n'+
                                               r'  $\mu$'+f' = {np.round(np.mean(param_data[k]),3)}'
                                               ) 
        counter+=1

    plt.suptitle(f'{param_name}s per Run: Station {station}\n2021 - 2025; By Run Type')
    plt.xlabel(f'{param_name} [{param_unit}]')
    plt.ylabel('Count')
    plt.yscale('log')
    plt.legend()
    filename =  f'{param_name.replace(" ","")}s_Station{station}_{counter}runTypes.png'
    plt.savefig(filename,dpi=300)
    print(f'Plot saved to {filename}')
    plt.show()


#=================================#



