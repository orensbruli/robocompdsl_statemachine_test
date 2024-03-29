#
# Copyright (C) 2019 by YOUR NAME HERE
#
#    This file is part of RoboComp
#
#    RoboComp is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    RoboComp is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.

import sys, Ice, os
from PySide2 import QtWidgets, QtCore

ROBOCOMP = ''
try:
	ROBOCOMP = os.environ['ROBOCOMP']
except KeyError:
	print '$ROBOCOMP environment variable not set, using the default value /opt/robocomp'
	ROBOCOMP = '/opt/robocomp'

preStr = "-I/opt/robocomp/interfaces/ -I"+ROBOCOMP+"/interfaces/ --all /opt/robocomp/interfaces/"
Ice.loadSlice(preStr+"CommonBehavior.ice")
import RoboCompCommonBehavior

additionalPathStr = ''
icePaths = [ '/opt/robocomp/interfaces' ]
try:
	SLICE_PATH = os.environ['SLICE_PATH'].split(':')
	for p in SLICE_PATH:
		icePaths.append(p)
		additionalPathStr += ' -I' + p + ' '
	icePaths.append('/opt/robocomp/interfaces')
except:
	print 'SLICE_PATH environment variable was not exported. Using only the default paths'
	pass




try:
	from ui_mainUI import *
except:
	print "Can't import UI file. Did you run 'make'?"
	sys.exit(-1)


class GenericWorker(QtWidgets.QWidget):

	kill = QtCore.Signal()
#Signals for State Machine
	onetotwo = QtCore.Signal()
	twotothree = QtCore.Signal()
	threetofour = QtCore.Signal()
	fourtoone = QtCore.Signal()
	fourtofive = QtCore.Signal()
	test2sub1totest2sub1 = QtCore.Signal()
	test2sub2totest2sub2 = QtCore.Signal()
	test2sub21totest2sub21 = QtCore.Signal()
	test2sub21totest2sub22 = QtCore.Signal()
	test3sub1totest3sub1 = QtCore.Signal()
	test3sub2totest3sub2 = QtCore.Signal()
	test4sub1totest4sub2 = QtCore.Signal()
	test4sub2totest4sub1 = QtCore.Signal()

#-------------------------

	def __init__(self, mprx):
		super(GenericWorker, self).__init__()


		self.ui = Ui_guiDlg()
		self.ui.setupUi(self)
		self.show()

		
		self.mutex = QtCore.QMutex(QtCore.QMutex.Recursive)
		self.Period = 30
		self.timer = QtCore.QTimer(self)

#State Machine
		self.myStateMachine= QtCore.QStateMachine()
		self.four_state = QtCore.QState(self.myStateMachine)
		self.one_state = QtCore.QState(self.myStateMachine)

		self.five_state = QtCore.QFinalState(self.myStateMachine)

		self.two_state = QtCore.QState(QtCore.QState.ParallelStates, self.myStateMachine)
		self.three_state = QtCore.QState(QtCore.QState.ParallelStates, self.myStateMachine)


		self.test2sub1_state = QtCore.QState(self.two_state)
		self.test2sub2_state = QtCore.QState(self.two_state)




		self.test2sub21_state = QtCore.QState(self.test2sub2_state)

		self.test2sub22_state = QtCore.QFinalState(self.test2sub2_state)



		self.test3sub1_state = QtCore.QState(self.three_state)
		self.test3sub2_state = QtCore.QState(self.three_state)
		self.test3sub3_state = QtCore.QState(self.three_state)




		self.test4sub2_state = QtCore.QState(self.four_state)
		self.test4sub1_state = QtCore.QState(self.four_state)



#------------------
#Initialization State machine
		self.one_state.addTransition(self.onetotwo, self.two_state)
		self.two_state.addTransition(self.twotothree, self.three_state)
		self.three_state.addTransition(self.threetofour, self.four_state)
		self.four_state.addTransition(self.fourtoone, self.one_state)
		self.four_state.addTransition(self.fourtofive, self.five_state)
		self.test2sub1_state.addTransition(self.test2sub1totest2sub1, self.test2sub1_state)
		self.test2sub2_state.addTransition(self.test2sub2totest2sub2, self.test2sub2_state)
		self.test2sub21_state.addTransition(self.test2sub21totest2sub21, self.test2sub21_state)
		self.test2sub21_state.addTransition(self.test2sub21totest2sub22, self.test2sub22_state)
		self.test3sub1_state.addTransition(self.test3sub1totest3sub1, self.test3sub1_state)
		self.test3sub2_state.addTransition(self.test3sub2totest3sub2, self.test3sub2_state)
		self.test4sub1_state.addTransition(self.test4sub1totest4sub2, self.test4sub2_state)
		self.test4sub2_state.addTransition(self.test4sub2totest4sub1, self.test4sub1_state)


		self.two_state.entered.connect(self.sm_two)
		self.three_state.entered.connect(self.sm_three)
		self.four_state.entered.connect(self.sm_four)
		self.one_state.entered.connect(self.sm_one)
		self.five_state.entered.connect(self.sm_five)
		self.test2sub1_state.entered.connect(self.sm_test2sub1)
		self.test2sub2_state.entered.connect(self.sm_test2sub2)
		self.test2sub21_state.entered.connect(self.sm_test2sub21)
		self.test2sub22_state.entered.connect(self.sm_test2sub22)
		self.test3sub1_state.entered.connect(self.sm_test3sub1)
		self.test3sub2_state.entered.connect(self.sm_test3sub2)
		self.test3sub3_state.entered.connect(self.sm_test3sub3)
		self.test4sub1_state.entered.connect(self.sm_test4sub1)
		self.test4sub2_state.entered.connect(self.sm_test4sub2)

		self.myStateMachine.setInitialState(self.one_state)
		self.test2sub2_state.setInitialState(self.test2sub21_state)
		self.four_state.setInitialState(self.test4sub1_state)

#------------------

#Slots funtion State Machine
	@QtCore.Slot()
	def sm_two(self):
		print "Error: lack sm_two in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_three(self):
		print "Error: lack sm_three in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_four(self):
		print "Error: lack sm_four in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_one(self):
		print "Error: lack sm_one in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_five(self):
		print "Error: lack sm_five in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test2sub1(self):
		print "Error: lack sm_test2sub1 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test2sub2(self):
		print "Error: lack sm_test2sub2 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test2sub21(self):
		print "Error: lack sm_test2sub21 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test2sub22(self):
		print "Error: lack sm_test2sub22 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test3sub1(self):
		print "Error: lack sm_test3sub1 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test3sub2(self):
		print "Error: lack sm_test3sub2 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test3sub3(self):
		print "Error: lack sm_test3sub3 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test4sub2(self):
		print "Error: lack sm_test4sub2 in Specificworker"
		sys.exit(-1)

	@QtCore.Slot()
	def sm_test4sub1(self):
		print "Error: lack sm_test4sub1 in Specificworker"
		sys.exit(-1)


#-------------------------
	@QtCore.Slot()
	def killYourSelf(self):
		rDebug("Killing myself")
		self.kill.emit()

	# \brief Change compute period
	# @param per Period in ms
	@QtCore.Slot(int)
	def setPeriod(self, p):
		print "Period changed", p
		Period = p
		timer.start(Period)
