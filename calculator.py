import sys
from PyQt5 import QtWidgets
from gui import Ui_MainWindow

class CalculatorWindow(QtWidgets.QMainWindow,Ui_MainWindow):
	firstNum = None
	userIsTypyingSecondNumber = False

	def __init__(self):
		super().__init__()
		self.setupUi(self)
		self.show()

		self.zero_btn.clicked.connect(self.digit_pressed)
		self.one_btn.clicked.connect(self.digit_pressed)
		self.two_btn.clicked.connect(self.digit_pressed)
		self.three_btn.clicked.connect(self.digit_pressed)
		self.four_btn.clicked.connect(self.digit_pressed)
		self.five_btn.clicked.connect(self.digit_pressed)
		self.six_btn.clicked.connect(self.digit_pressed)
		self.seven_btn.clicked.connect(self.digit_pressed)
		self.eight_btn.clicked.connect(self.digit_pressed)
		self.nine_btn.clicked.connect(self.digit_pressed)
		self.clear_btn.clicked.connect(self.clear)

		self.dot_btn.clicked.connect(self.decimal_pressed)
		self.inveter_btn.clicked.connect(self.unary_operation_pressed)
		self.percent_btn.clicked.connect(self.unary_operation_pressed)

		self.add_btn.clicked.connect(self.binary_operation_pressed)
		self.subtract_btn.clicked.connect(self.binary_operation_pressed)
		self.multipl_btn.clicked.connect(self.binary_operation_pressed)
		self.div_btn.clicked.connect(self.binary_operation_pressed)

		self.result_btn.clicked.connect(self.equals_pressed)

		self.add_btn.setCheckable(True)
		self.subtract_btn.setCheckable(True)
		self.multipl_btn.setCheckable(True)
		self.div_btn.setCheckable(True)

	def digit_pressed(self):
		button = self.sender()

		if ((self.add_btn.isChecked() or self.subtract_btn.isChecked() or 
			self.multipl_btn.isChecked() or self.div_btn.isChecked()) and (not self.userIsTypyingSecondNumber)):
			newLabel = format(float(button.text()),'.15g')
			self.userIsTypyingSecondNumber = True
		else:
			if (('.' in self.output_lbl.text()) and (button.text() == "0")):
				newLabel = format(self.output_lbl.text() + button.text(),'.15')
			else:	
				newLabel = format(float(self.output_lbl.text() + button.text()),'.15g')

		self.output_lbl.setText(newLabel)

	def decimal_pressed(self):
		self.output_lbl.setText(self.output_lbl.text() + '.')

	def unary_operation_pressed(self):
		button = self.sender()
		labelNumber = float(self.output_lbl.text())

		if button.text() == '+/-':
			labelNumber *= -1
		else:
			labelNumber *= 0.01

		newLabel = format(labelNumber, '.15g')
		self.output_lbl.setText(newLabel)

	def binary_operation_pressed(self):
		button = self.sender()
		self.firstNum = float(self.output_lbl.text())
		button.setChecked(True)

	def equals_pressed(self):
		secondNum = float(self.output_lbl.text())

		if self.add_btn.isChecked():
			labelNumber = self.firstNum + secondNum
			newLabel = format(labelNumber,'.15g')
			self.output_lbl.setText(newLabel)
			self.add_btn.setChecked(False)

		elif self.subtract_btn.isChecked():
			labelNumber = self.firstNum - secondNum
			newLabel = format(labelNumber,'.15g')
			self.output_lbl.setText(newLabel)
			self.subtract_btn.setChecked(False)

		elif self.multipl_btn.isChecked():
			labelNumber = self.firstNum * secondNum
			newLabel = format(labelNumber,'.15g')
			self.output_lbl.setText(newLabel)
			self.multipl_btn.setChecked(False)

		elif self.div_btn.isChecked():
			labelNumber = self.firstNum / secondNum
			newLabel = format(labelNumber,'.15g')
			self.output_lbl.setText(newLabel)
			self.div_btn.setChecked(False)

		self.userIsTypyingSecondNumber = False


	def clear(self):
		self.add_btn.setChecked(False)
		self.subtract_btn.setChecked(False)
		self.multipl_btn.setChecked(False)
		self.div_btn.setChecked(False)
		self.add_btn.setChecked(False)

		self.userIsTypyingSecondNumber = False

		self.output_lbl.setText('0')