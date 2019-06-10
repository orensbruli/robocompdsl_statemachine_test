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
	oneState->addTransition(this, SIGNAL(onetotwo()), twoState);
	twoState->addTransition(this, SIGNAL(twotothree()), threeState);
	threeState->addTransition(this, SIGNAL(threetofour()), fourState);
	fourState->addTransition(this, SIGNAL(fourtoone()), oneState);
	fourState->addTransition(this, SIGNAL(fourtofive()), fiveState);
	test2sub1State->addTransition(this, SIGNAL(test2sub1totest2sub1()), test2sub1State);
	test2sub2State->addTransition(this, SIGNAL(test2sub2totest2sub2()), test2sub2State);
	test2sub21State->addTransition(this, SIGNAL(test2sub21totest2sub21()), test2sub21State);
	test2sub21State->addTransition(this, SIGNAL(test2sub21totest2sub22()), test2sub22State);
	test3sub1State->addTransition(this, SIGNAL(test3sub1totest3sub1()), test3sub1State);
	test3sub2State->addTransition(this, SIGNAL(test3sub2totest3sub2()), test3sub2State);
	test4sub1State->addTransition(this, SIGNAL(test4sub1totest4sub2()), test4sub2State);
	test4sub2State->addTransition(this, SIGNAL(test4sub2totest4sub1()), test4sub1State);

	myStateMachine.addState(twoState);
	myStateMachine.addState(threeState);
	myStateMachine.addState(fourState);
	myStateMachine.addState(oneState);
	myStateMachine.addState(fiveState);

	myStateMachine.setInitialState(oneState);
	test2sub2State->setInitialState(test2sub21State);
	fourState->setInitialState(test4sub1State);

	QObject::connect(twoState, SIGNAL(entered()), this, SLOT(sm_two()));
	QObject::connect(threeState, SIGNAL(entered()), this, SLOT(sm_three()));
	QObject::connect(fourState, SIGNAL(entered()), this, SLOT(sm_four()));
	QObject::connect(oneState, SIGNAL(entered()), this, SLOT(sm_one()));
	QObject::connect(fiveState, SIGNAL(entered()), this, SLOT(sm_five()));
	QObject::connect(test2sub1State, SIGNAL(entered()), this, SLOT(sm_test2sub1()));
	QObject::connect(test2sub2State, SIGNAL(entered()), this, SLOT(sm_test2sub2()));
	QObject::connect(test2sub21State, SIGNAL(entered()), this, SLOT(sm_test2sub21()));
	QObject::connect(test2sub22State, SIGNAL(entered()), this, SLOT(sm_test2sub22()));
	QObject::connect(test3sub1State, SIGNAL(entered()), this, SLOT(sm_test3sub1()));
	QObject::connect(test3sub2State, SIGNAL(entered()), this, SLOT(sm_test3sub2()));
	QObject::connect(test3sub3State, SIGNAL(entered()), this, SLOT(sm_test3sub3()));
	QObject::connect(test4sub1State, SIGNAL(entered()), this, SLOT(sm_test4sub1()));
	QObject::connect(test4sub2State, SIGNAL(entered()), this, SLOT(sm_test4sub2()));

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

