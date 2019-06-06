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
		self.two_state = QtCore.QState(self.myStateMachine)
		self.three_state = QtCore.QState(self.myStateMachine)
		self.four_state = QtCore.QState(self.myStateMachine)
		self.one_state = QtCore.QState(self.myStateMachine)

		self.five_state = QtCore.QFinalState(self.myStateMachine)


#------------------
#Initialization State machine
		self.one_state.addTransition(self.onetotwo, self.two_state)
		self.two_state.addTransition(self.twotothree, self.three_state)
		self.three_state.addTransition(self.threetofour, self.four_state)
		self.four_state.addTransition(self.fourtoone, self.one_state)
		self.four_state.addTransition(self.fourtofive, self.five_state)


		self.two_state.entered.connect(self.sm_two)
		self.three_state.entered.connect(self.sm_three)
		self.four_state.entered.connect(self.sm_four)
		self.one_state.entered.connect(self.sm_one)
		self.five_state.entered.connect(self.sm_five)

		self.myStateMachine.setInitialState(self.one_state)

#------------------

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
