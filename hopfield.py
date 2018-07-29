import numpy as np 
from tkinter import *

'''
Class: Hopfield()
Description: the following class generate and runs the pattern engine for the hopfield 
	neural network. All the computation is done in real time thus, for larger input
	prediction may take a few moment
'''
class Hopfield(object):
	'''
	Name: __init__()
	Description: constructor of the Hopfield class. Generates the GUI
	Parameters:
		row -- number of row for the pattern engine
		col -- number of column for the pattern engine
		order -- visiting order of each node for the hopfield network
	Return Values: none
	'''
	def __init__(self, row = None, col = None, order = None):
		self.root = Tk()
		self.root.title("Hopfield Game")
		# self.root.geometry("500x500")

		self.row = 3 if row is None else row
		self.col = 3 if col is None else col
		
		self.button = [[0 for x in range(self.col)] for x in range(self.row)]
		self.buttonState = np.zeros((self.row, self.col)) - 1

		self.patterns = []

		if order is None:
			self.order = None
		elif order is list:
			if len(order) != self.row * self.col:
				self.order = None
			else:
				self.order = order
		else:
			self.order = None

		self.createGUI()

	'''
	Name: buttonClick()
	Description: action for the button click event of the patter engine
	Parameters:
		x -- row of the pattern engine
		y -- column of the pattern engien
	Return Values: none
	'''
	def buttonClick(self, x, y):
		if self.buttonState[x][y] == 1:
			self.button[x][y].config(bg = "white")
		else:
			self.button[x][y].config(bg = "black")

		self.buttonState[x][y] = -1 * self.buttonState[x][y]

	'''
	Name: clearGUI()
	Description: reset the GUI to its default configuration
	Parameters: none
	Return Values: none
	'''
	def clearGUI(self):
		for x in range(self.row):
			for y in range(self.col):
				self.button[x][y].config(bg = "white")
				self.buttonState[x][y] = -1

	'''
	Name: clearTraining()
	Description: on click event for 'Clear Training Data'. Clears the
		training dataset
	Parameters: none
	Return Value: none
	'''
	def clearTraining(self):
		self.patterns = []
		print("Cleared Training Data")

	'''
	Name: createGUI()
	Description: generates the main structure GUI
	Parameters:
		row -- number of rows for the pattern engine
		col -- number of columns for the pattern engine
	Return Values:
	'''
	def createGUI(self, row = None, col = None):
		if row is None:
			row = self.row

		if col is None:
			col = self.col

		self.frame = Frame(self.root)
		self.frame.grid(row = 0, column = 0)

		w = self.root.winfo_width()
		h = self.root.winfo_height()

		for x in range(row):
			for y in range(col):
				self.button[x][y] = Button(self.frame, bg = "white",
					command = lambda x1 = x,y1 = y: self.buttonClick(x1,y1))
				self.button[x][y].grid(column = y, row = x)
				self.button[x][y].config(height = int(row / h), width = int(col / w))

		self.frame.pack(expand = True)

		clearCol = int(self.col / 2)
		clear = Button(self.frame, text = "Clear Selection", command = self.clearGUI)
		# clear.grid(column = int(self.col / 2), row = self.row)
		clear.grid(column = self.col + 1, row = 0)

		train = Button(self.frame, text = "Train", command = self.onTrain)
		# train.grid(column = int(self.col / 4), row = self.row)
		train.grid(column = self.col + 1, row = 1)

		predict = Button(self.frame, text = "Predict", command = self.onPredict)
		# predict.grid(column = clearCol + 1, row = self.row)
		predict.grid(column = self.col + 1, row = 2)

		self.createMenubar()

	'''
	Name: createMenuBar()
	Description: creates the menubar for the GUI
	Parameters: none
	Return Values: none
	'''
	def createMenubar(self):
		self.menu = Menu(self.root)
		self.root.config(menu = self.menu)

		options = Menu(self.menu)
		options.add_command(label = "Train", command = self.onTrain)
		options.add_command(label = "Predict", command = self.onPredict)
		options.add_command(label = "Clear Selection", command = self.clearGUI)
		options.add_command(label = "Clear Training Data", command = self.clearTraining)
		options.add_command(label = "Exit", command = self.onExit)

		self.menu.add_cascade(label = "Options", menu = options)

	'''
	Name: evolve()
	Description: this function determines the next state of a
		given neuron for the hopfield network algorithm
	Parameters:
		W -- weight matrix of the hopfield network
		X -- current state of the hopfield network
		position -- node whose state needs to be updated
	Return values:
		-1 -- if the next state of the neuron is OFF
		+1 -- if the next state of the neuron is ON
	'''	
	def evolve(self, W, X, position):	
		newX = np.dot(W[ position - 1, : ], X)
		if newX < 0:
			return -1
		else:
			return 1

	'''
	Name: generateWeightMatrix()
	Description: this function generates the weight matrix for
		the hopfield network
	Parameters:
		X -- matrix whose columns represents the patterns that needs to be
					memorized
	Return value:
		W -- weight matrix of the hopfield network
	'''
	def generateWeightMatrix(self, X):
		X = np.asarray(X)
		XShape = X.shape
		W = np.matmul(X, X.T) / float(XShape[0])
		W = W - (( float(XShape[1]) / float(XShape[0])) * np.identity(XShape[0]))

		return W

	'''
	Name: hopfieldNetworkAlgorithm()
	Description: this function perform the algorithm for hopfield
		network algorithm
	Parameters:
		W -- weight matrix of the network
		V -- initial state of the network
		order -- vector specifying the visiting order of each nodes
							by default, its sequential visiting order
	Return values:
		U -- end state of the hopfield network
		updateHistory -- matrix whose columns represent the state of hopfield
			network at each iteration
	'''	
	def  hopfieldNetworkAlgorithm(self, W, V, order = None):
		U = V
		Vshape = V.shape
		updateHistory = U

		if order is None:
			order = range(Vshape[0])
		
		error = True
		count = 0

		while error:
			error = False
			for i in order:
				temp = self.evolve(W, U, i)
				count += 1
				if U[ i - 1 ] != temp:
					count = 0
					error = True
				U[ i - 1 ] = temp
				updateHistory = np.append(updateHistory, U, axis = 1)

				if count == Vshape[0]:
					break

		return U, updateHistory

	'''
	Name: onExit()
	Description: on click event for the 'Exit' selection under menubar
	Parameters: none
	Return Values: none
	'''
	def onExit(self):
		exit()

	'''
	Name: onPredict()
	Description: on click event for the 'Predict' button selection. The pattern
		engine predicts and display the final state based on the training set
	Parameters: none
	Return Values: none
	'''
	def onPredict(self):
		if self.patterns == []:
			print("Must train on at least one pattern before predicting.")
			exit(-1)

		weights = self.generateWeightMatrix(self.transposeList(self.patterns))
		initialState = self.stackButtonState()


		U, updateHistory = self.hopfieldNetworkAlgorithm(weights, 
								initialState, self.order)

		self.updateGUI(U)

	'''
	Name: onTrain()
	Description: on click event for the 'Train' button selection. The pattern
		engine stores the current configuration as training set and reset the 
		GUI to default configuration
	Parameters: none
	Return Values: none
	'''
	def onTrain(self):
		self.patterns.append(np.hstack(self.buttonState))
		self.clearGUI()

	'''
	Name: run()
	Description: mainloop that runs the GUI
	Parameters: none
	Return Values: none
	'''
	def run(self):
		self.root.mainloop()

	'''
	Name: stackButtonState()
	Description: vertically stack the current configuration of the pattern engine
		into a column vector
	Parameters: none
	Return Values:
		vec -- column vector representing the current state of the pattern engine
	'''
	def stackButtonState(self):
		vec = np.empty((self.row * self.col, 1))

		for x in range(self.row):
			for y in range(self.col):
				vec[self.col * x + y, 0] = self.buttonState[x][y]

		return vec 

	'''
	Name: transposeList()
	Description: transpose any list into a column vector
	Parameters:
		l -- list to transpose
	Return Values: list as column vector 
	'''
	def transposeList(self, l):
		return [list(i) for i in zip(*l)]

	'''
	Name: updateGUI()
	Description: updates the pattern engine to match a specified state
	Parameters:
		state -- state of the pattern engine as column vector
	Return Values: none
	'''
	def updateGUI(self, state):
		for i in range(self.row * self.col):
			row = int(i / self.col)
			col = i % self.col
			# print("row = ", row, " col = ", col)
			if state[i] == 1:
				self.buttonState[row][col] = 1
				self.button[row][col].config(bg = "black")
			else:
				self.buttonState[row][col] = -1
				self.button[row][col].config(bg = "white")