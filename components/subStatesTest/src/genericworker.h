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
#ifndef GENERICWORKER_H
#define GENERICWORKER_H

#include "config.h"
#include <stdint.h>
#include <qlog/qlog.h>

#if Qt5_FOUND
	#include <QtWidgets>
#else
	#include <QtGui>
#endif
#include <ui_mainUI.h>
#include <QStateMachine>
#include <QState>
#include <CommonBehavior.h>


#define CHECK_PERIOD 5000
#define BASIC_PERIOD 100

using namespace std;

typedef map <string,::IceProxy::Ice::Object*> MapPrx;


class GenericWorker :
#ifdef USE_QTGUI
	public QWidget, public Ui_guiDlg
#else
	public QObject
 #endif
{
Q_OBJECT
public:
	GenericWorker(MapPrx& mprx);
	virtual ~GenericWorker();
	virtual void killYourSelf();
	virtual void setPeriod(int p);

	virtual bool setParams(RoboCompCommonBehavior::ParameterList params) = 0;
	QMutex *mutex;




protected:
//State Machine
	QStateMachine myStateMachine;

	QState *twoState = new QState(QState::ParallelStates);
	QState *threeState = new QState(QState::ParallelStates);
	QState *fourState = new QState();
	QState *oneState = new QState();
	QFinalState *fiveState = new QFinalState();
	QState *test2sub1State = new QState(twoState);
	QState *test2sub2State = new QState(twoState);
	QState *test2sub21State = new QState(test2sub2State);
	QFinalState *test2sub22State = new QFinalState(test2sub2State);
	QState *test3sub1State = new QState(threeState);
	QState *test3sub2State = new QState(threeState);
	QState *test3sub3State = new QState(threeState);
	QState *test4sub2State = new QState(fourState);
	QState *test4sub1State = new QState(fourState);

//-------------------------

	QTimer timer;
	int Period;

private:


public slots:
//Slots funtion State Machine
	virtual void sm_two() = 0;
	virtual void sm_three() = 0;
	virtual void sm_four() = 0;
	virtual void sm_one() = 0;
	virtual void sm_five() = 0;
	virtual void sm_test2sub1() = 0;
	virtual void sm_test2sub2() = 0;
	virtual void sm_test2sub21() = 0;
	virtual void sm_test2sub22() = 0;
	virtual void sm_test3sub1() = 0;
	virtual void sm_test3sub2() = 0;
	virtual void sm_test3sub3() = 0;
	virtual void sm_test4sub2() = 0;
	virtual void sm_test4sub1() = 0;

//-------------------------
    virtual void initialize(int period) = 0;
	
signals:
	void kill();
//Signals for State Machine
	void onetotwo();
	void twotothree();
	void threetofour();
	void fourtoone();
	void fourtofive();
	void test2sub1totest2sub1();
	void test2sub2totest2sub2();
	void test2sub21totest2sub21();
	void test2sub21totest2sub22();
	void test3sub1totest3sub1();
	void test3sub2totest3sub2();
	void test4sub1totest4sub2();
	void test4sub2totest4sub1();

//-------------------------
};

#endif
