/*
* Software License Agreement (BSD License)
* Copyright (c) 2013, Georgia Institute of Technology
* All rights reserved.
*
* Redistribution and use in source and binary forms, with or without
* modification, are permitted provided that the following conditions are met:
*
* 1. Redistributions of source code must retain the above copyright notice, this
* list of conditions and the following disclaimer.
* 2. Redistributions in binary form must reproduce the above copyright notice,
* this list of conditions and the following disclaimer in the documentation
* and/or other materials provided with the distribution.
*
* THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
* AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
* IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
* DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
* FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
* DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
* SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
* CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
* OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
* OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/
/**********************************************
 * @file JoystickControl.h
 * @author Brian Goldfain <bgoldfai@gmail.com>
 * @date January 29, 2012
 * @copyright 2012 Georgia Institute of Technology
 * @brief Use a joystick or gamepad connected to the the computer
 * to control the throttle/brake and steering commands
 *
 * @details This file contains the JoystickControl class
 ***********************************************/
#ifndef JOYSTICK_CONTROL_H_
#define JOYSTICK_CONTROL_H_

//#include "autorally_msgs/servoControllerMSG.h"
#include <ros/ros.h>
#include <ros/time.h>
#include <sensor_msgs/Joy.h>
#include <autorally_msgs/servoMSG.h>
#include <autorally_msgs/safeSpeed.h>

/**
 *  @class JoystickControl JoystickControl.h "joystick/JoystickControl.h"
 *  @brief Use a joystick or gamepad connected to the computer to send out
 *  ServoControllerCommand messages
 *
 *  The default configuration is for a gamepad with two joysticks. The left
 *  stick controlls the steering and the right stick controls the trottle.
 *  Make sure that ROS is able to access the input device of choice before
 *  running. This class is not meant to be used to freal time control, it is
 *  for component testing purposes and demonstration.
 *
 *  @note in order to receive joy messages from ROS the joystick path must be
 *  set with [rosparam set joy_node/dev "/dev/input/js0"] if not already set.
 *  Also, joy must be running:  [rosrun joy joy_node]
 *
 */
class JoystickControl
{
 public:
  /**
   * Constructor registers callbacks and advertises message that will be
   * published
   *
   */
  JoystickControl();
  ~JoystickControl();

  /**
   * Callback for receiving new joystick state data
   * @see sensor_messages::joy
   * @param joy the message received from ros comms
   */
  void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);

  void safeSpeedCallback(const ros::TimerEvent& time);

  ros::Subscriber m_joySub; ///< Channel to receive joystick state
//  ros::Subscriber m_statusSub; ///< Channel to receive servo status
  ros::Publisher m_commandPub; ///< Channel to publish servo commands
  ros::Publisher m_safeSpeedPub; ///< Channel to publish servo commands
  ros::Timer m_safeSpeedTimer;
 private:
  ros::NodeHandle m_nh;

  autorally_msgs::servoMSGPtr m_servoCommand; ///< command message
  autorally_msgs::safeSpeedPtr m_safeSpeed; ///< command message
  double m_throttleDamping;
  double m_steeringDamping;
  
  bool m_throttleEnabled;
  bool m_steeringEnabled;
  bool m_throttleBrakePaired;
  bool m_frontBrake;

  int m_throttleAxis;
  int m_steeringAxis;
  int m_brakeAxis;
  int m_safeSpeedIncButton;
  int m_safeSpeedDecButton;
  int m_safeSpeedZeroButton1;
  int m_safeSpeedZeroButton2;
  int m_throttleEnableButton;
  int m_steeringEnableButton;
};

#endif //JOYSTICK_CONTROL_H_
