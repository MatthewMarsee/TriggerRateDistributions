## DESCRIPTION:

* Plot trigger rate distribution for stations. 

## REQUIREMENTS:
### Non-Standard Python Imports:
* Clone the RNO-G Runtable and follow installation instructions. (https://github.com/RNO-G/rnog-runtable)
  * Add directory to your $PYTHONPATH in your ```~/.zshrc/``` or ```~/.bashrc``` file. <br/> (export ```PYTHONPATH=/path/to/rnog-runtable:$PYTHONPATH``` )


## INSTRUCTIONS:

### Option 1: Python notebook
* Open ```plotTriggerRateDist.ipynb```
* Change the ```station``` variable
* Run all cells, histogram of distribution will save to 

### Option 2: Python Script
For "station xx"

* ```python3 plotTriggerRateDist.py -s xx```
  
or

* ```python3 plotTriggerRateDist.py --station xx```

A png of the histogram(s) will be saved in the working directory.

