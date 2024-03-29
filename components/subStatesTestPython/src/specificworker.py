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
#
from time import sleep

from genericworker import *

# If RoboComp was compiled with Python bindings you can use InnerModel in Python
# sys.path.append('/opt/robocomp/lib')
# import librobocomp_qmat
# import librobocomp_osgviewer
# import librobocomp_innermodel

class SpecificWorker(GenericWorker):
	def __init__(self, proxy_map):
		super(SpecificWorker, self).__init__(proxy_map)
		self.Period = 2000
		self.timer.start(self.Period)

		self.myStateMachine.start()

	def __del__(self):
		print 'SpecificWorker destructor'

	def setParams(self, params):
		#try:
		#	self.innermodel = InnerModel(params["InnerModelPath"])
		#except:
		#	traceback.print_exc()
		#	print "Error reading config params"
		return True


#Slots funtion State Machine
	#
	# sm_two
	#
	@QtCore.Slot()
	def sm_two(self):
		print("Entered state two")
		sleep(1)
		self.twotothree.emit()
		pass

	#
	# sm_three
	#
	@QtCore.Slot()
	def sm_three(self):
		print("Entered state three")
		sleep(1)
		self.threetofour.emit()
		pass

	#
	# sm_four
	#
	@QtCore.Slot()
	def sm_four(self):
		print("Entered state four")
		sleep(1)
		self.fourtofive.emit()
		pass

	#
	# sm_one
	#
	@QtCore.Slot()
	def sm_one(self):
		print("Entered state one")
		sleep(1)
		self.onetotwo.emit()
		pass

	#
	# sm_five	#
	@QtCore.Slot()
	def sm_five(self):
		print("Entered state five")
		sleep(1)
		pass

	#
	# sm_test2sub1
	#
	@QtCore.Slot()
	def sm_test2sub1(self):
		print("Entered state test2sub1")
		sleep(1)
		self.test2sub1totest2sub1.emit()
		pass

	#
	# sm_test2sub2
	#
	@QtCore.Slot()
	def sm_test2sub2(self):
		print("Entered state test2sub2")
		sleep(1)
		self.test2sub2totest2sub2.emit()
		pass

	#
	# sm_test2sub21
	#
	@QtCore.Slot()
	def sm_test2sub21(self):
		print("Entered state test2sub21")
		sleep(1)
		self.test2sub21totest2sub21.emit()
		pass

	#
	# sm_test2sub22
	#
	@QtCore.Slot()
	def sm_test2sub22(self):
		print("Entered state test2sub22")
		sleep(1)
		# self.test2sub22to__.emit()
		pass

	#
	# sm_test3sub1
	#
	@QtCore.Slot()
	def sm_test3sub1(self):
		print("Entered state test3sub1")
		sleep(1)
		self.test3sub1totest3sub1.emit()
		pass

	#
	# sm_test3sub2
	#
	@QtCore.Slot()
	def sm_test3sub2(self):
		print("Entered state test3sub2")
		sleep(1)
		self.test3sub2totest3sub2.emit()
		pass

	#
	# sm_test3sub3
	#
	@QtCore.Slot()
	def sm_test3sub3(self):
		# self.test3sub3to_.emit()
		print("Entered state test3sub3")
		sleep(1)
		pass

	#
	# sm_test4sub2
	#
	@QtCore.Slot()
	def sm_test4sub2(self):
		print("Entered state test4sub2")
		sleep(1)
		self.test4sub2totest4sub1.emit()
		pass

	#
	# sm_test4sub1
	#
	@QtCore.Slot()
	def sm_test4sub1(self):
		print("Entered state test4sub1")
		sleep(1)
		self.test4sub1totest4sub2.emit()
		pass


#-------------------------
