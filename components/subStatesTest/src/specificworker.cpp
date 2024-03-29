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
#include "specificworker.h"

/**
* \brief Default constructor
*/
SpecificWorker::SpecificWorker(MapPrx& mprx) : GenericWorker(mprx)
{

}

/**
* \brief Default destructor
*/
SpecificWorker::~SpecificWorker()
{
	std::cout << "Destroying SpecificWorker" << std::endl;
}

bool SpecificWorker::setParams(RoboCompCommonBehavior::ParameterList params)
{
//       THE FOLLOWING IS JUST AN EXAMPLE
//	To use innerModelPath parameter you should uncomment specificmonitor.cpp readConfig method content
//	try
//	{
//		RoboCompCommonBehavior::Parameter par = params.at("InnerModelPath");
//		std::string innermodel_path = par.value;
//		innerModel = new InnerModel(innermodel_path);
//	}
//	catch(std::exception e) { qFatal("Error reading config params"); }



	myStateMachine.start();
	


	return true;
}

void SpecificWorker::initialize(int period)
{
	std::cout << "Initialize worker" << std::endl;
	this->Period = period;
	timer.start(Period);

}



void SpecificWorker::sm_two()
{
	std::cout<<"Entered state two"<<std::endl;
}

void SpecificWorker::sm_three()
{
	std::cout<<"Entered state three"<<std::endl;
}

void SpecificWorker::sm_four()
{
	std::cout<<"Entered state four"<<std::endl;
}

void SpecificWorker::sm_one()
{
	std::cout<<"Entered initial state one"<<std::endl;
}

void SpecificWorker::sm_five()
{
	std::cout<<"Entered final state five"<<std::endl;
}

void SpecificWorker::sm_test2sub1()
{
	std::cout<<"Entered state test2sub1"<<std::endl;
}

void SpecificWorker::sm_test2sub2()
{
	std::cout<<"Entered state test2sub2"<<std::endl;
}

void SpecificWorker::sm_test2sub21()
{
	std::cout<<"Entered state test2sub21"<<std::endl;
}

void SpecificWorker::sm_test2sub22()
{
	std::cout<<"Entered state test2sub22"<<std::endl;
}

void SpecificWorker::sm_test3sub1()
{
	std::cout<<"Entered state test3sub1"<<std::endl;
}

void SpecificWorker::sm_test3sub2()
{
	std::cout<<"Entered state test3sub2"<<std::endl;
}

void SpecificWorker::sm_test3sub3()
{
	std::cout<<"Entered state test3sub3"<<std::endl;
}

void SpecificWorker::sm_test4sub2()
{
	std::cout<<"Entered state test4sub2"<<std::endl;
}

void SpecificWorker::sm_test4sub1()
{
	std::cout<<"Entered state test4sub1"<<std::endl;
}






