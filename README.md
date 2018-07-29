# Hopfield Pattern Engine

## About

## Prerequisite
Before running any of the code in this repo, the following must be installed at the minimum:
* Python 3.6.4
* Numpy version 1.14.0
* Tkinter version 8.6
* Argparse version 1.4.0

## Files List
* README.md
* hopfiled.py
* testHopfield.py

## Running
Program supports commandline interface which allows to run with variable number of row and columns and the visiting order for the hopfiled algorithm.

```
-h, --help	show this help message and exit
-r ROW, --row ROW 	Number of rows for the pattern engine (int)
-c COL, --col COL 	Number of columns for the pattern engine (int)
-o [ORDER [ORDER ...]], --order [ORDER [ORDER ...]]
	List specifying visiting order of each node
```  

By default, the pattern engine contains 3 rows and 3 columns with lexicographical ordering.


## Future Imporovements
* Add additional features to GUI

## Contributors
* Ravi Patel: https://github.com/rpatel26