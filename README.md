# Hopfield Pattern Engine

## About
The following is a pattern recognition engine based on the Hopfield Neural Network.

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
-h, --help		show this help message and exit
-r ROW, --row ROW 	Number of rows for the pattern engine (int)
-c COL, --col COL 	Number of columns for the pattern engine (int)
-o [ORDER [ORDER ...]], --order [ORDER [ORDER ...]]
			List specifying visiting order of each node
```  

By default, the pattern engine contains 4 rows and 4 columns with random visiting order. To run the program with default setting, use `python ./testHopfield.py`.

To run the program with 4 rows and 5, use `python ./testHopfield.py -r 4 -c 5`

### Visiting Order for the Hopfield Algorithm
Size of the list specifying order must exactly be equal to `row * column`. Furthermore, each of the element in the `order` list must be unique, ranging from `0 to [(row * col) - 1]`.

For example, if the pattern machine has 4 row and 3 column, then the size of the `order` list must be `4 * 3 = 12` element. The following is one possible combination:

`python .\testHopfield.py -r 4 -c 3 -o 0 2 4 6 8 10 1 3 5 7 9 11`

If the size of the `order` list does not match `row * column` or the element of the list does not satisfy the ranging criteria, then `order` list will be randomized to a new valid list.

## Future Imporovements
* Add additional features to GUI

## Contributors
* Ravi Patel: https://github.com/rpatel26