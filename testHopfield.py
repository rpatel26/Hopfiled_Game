from hopfield import Hopfield
import argparse

if ( __name__ == '__main__' ):
	parser = argparse.ArgumentParser()
	parser.add_argument('-r', "--row", 
		help = "Number of rows for the pattern engine (int)", type = int)
	parser.add_argument('-c', "--col", 
		help = "Number of columns for the pattern engine (int)", type = int)
	parser.add_argument('-o', "--order", nargs = '*',
		help = "List specifying visiting order of each node", type = int)

	args = parser.parse_args()

	row = 3 if args.row is None else args.row
	col = 4 if args.col is None else args.col
	order = args.order

	# print("row = ", row)
	# print("col = ", col)
	# print("order = ", order)
	
	test = Hopfield(row = row, col = col, order = order)
	test.runGUI()
