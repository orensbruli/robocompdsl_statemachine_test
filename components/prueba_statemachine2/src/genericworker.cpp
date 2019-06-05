/*
 *    Copyright (C)2019 by YOUR NAME HERE
 *
 *    This file is part of RoboComp
 *
 *    RoboComp is free software: you can redistribute it and/or modify
 *    it under the terms of the GNU General Public License as published by
 *    the Free Software Foundation, either version 3 of the License, or
 *    (at your option) any later version.
 *
 *    RoboComp is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU General Public License for more details.
 *
 *    You should have received a copy of the GNU General Public License
 *    along with RoboComp.  If not, see <http://www.gnu.org/licenses/>.
 */
#include "genericworker.h"
/**
* \brief Default constructor
*/
GenericWorker::GenericWorker(MapPrx& mprx) :
#ifdef USE_QTGUI
Ui_guiDlg()
#else
QObject()
#endif

{

//Initialization State machine
	start_waiting->addTransition(this, SIGNAL(start_waitingtoinitialize()), initialize);
	initialize->addTransition(this, SIGNAL(initializetocompute()), compute);
	compute->addTransition(this, SIGNAL(computetocompute()), compute);
	compute->addTransition(this, SIGNAL(computetofinalize()), finalize);

	Machine_testcpp.addState(initialize);
	Machine_testcpp.addState(compute);
	Machine_testcpp.addState(start_waiting);
	Machine_testcpp.addState(finalize);

	Machine_testcpp.setInitialState(start_waiting);

	QObject::connect(initialize, SIGNAL(entered()), this, SLOT(fun_initialize()));
	QObject::connect(compute, SIGNAL(entered()), this, SLOT(fun_compute()));
	QObject::connect(start_waiting, SIGNAL(entered()), this, SLOT(fun_start_waiting()));
	QObject::connect(finalize, SIGNAL(entered()), this, SLOT(fun_finalize()));

//------------------

	mutex = new QMutex(QMutex::Recursive);

	#ifdef USE_QTGUI
		setupUi(this);
		show();
	#endif
	Period = BASIC_PERIOD;

}

/**
* \brief Default destructor
*/
GenericWorker::~GenericWorker()
{

}
void GenericWorker::killYourSelf()
{
	rDebug("Killing myself");
	emit kill();
}
/**
* \brief Change compute period
* @param per Period in ms
*/
void GenericWorker::setPeriod(int p)
{
	rDebug("Period changed"+QString::number(p));
	Period = p;
	timer.start(Period);
}

