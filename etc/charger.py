#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
from std_msgs.msg import Bool, String, Empty
from std_msgs.msg import UInt8MultiArray, UInt16MultiArray
from geometry_msgs.msg import *
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
from PySide.QtGui import *
from PySide.QtCore import *
from PySide import QtGui, QtCore
import thread
import rospkg
import os
import datetime
import time
from sensor_msgs.msg import JointState
import yaml
import io
from robocare_msgs.srv import LeaveStation, DockOnStation, LeaveStationRequest, DockOnStationRequest

class Communicate(QtCore.QObject):
    signal = QtCore.Signal(str)

class ChargerUI(QtGui.QMainWindow):

  def __init__(self):

    super(ChargerUI, self).__init__()

    self.__comm = Communicate()
    self.__comm.signal.connect(self.get_signal)

    self.__leave_service = rospy.ServiceProxy('/social_recharge/leave_station', LeaveStation, persistent=True)
    self.__dock_service = rospy.ServiceProxy('/social_recharge/dock_on_station', DockOnStation, persistent=True)
    self.__reset_pub = rospy.Publisher('/reset', Empty, queue_size=1)
    self.__go_to_init_pub = rospy.Publisher('/social_nav/go_to_init', Bool, queue_size=1)
    self.__go_to_goal_pub = rospy.Publisher('/social_nav/go_to_goal', Bool, queue_size=1)
    self.__dock_publish = rospy.Publisher('/social_recharge/dock_state', Bool, queue_size=10)
    rospy.Subscriber('/social_recharge/dock_state', Bool, self.dock_callback)


    screen_width = 800
    screen_height = 600
    self.setGeometry(0, 0, screen_width, screen_height)

    thread.start_new_thread(self.spin, ("", ))

    self.__size_x = 30
    self.__size_y = 150
    self.__size_data = 300
    self.__gap_x = 10

    self.__start_x1 = 30
    self.__start_y1 = 200

    x = self.__start_x1
    y = self.__start_y1 -130

    num_label = QLabel(u"SOCIAL ROBOT TEST", self)
    num_label.setStyleSheet("color: black; border: 2px solid rgb(0,0,0);")
    num_label.setFont(QFont(u"나눔고딕",20,weight=QFont.Bold))
    num_label.setGeometry(x,y,self.__size_data, self.__size_x)
    num_label.setAlignment(QtCore.Qt.AlignCenter)

    y = self.__start_y1 - 80
    undock_button = QPushButton(u"UNDOCKING", self)
    undock_button.setGeometry(x,y,self.__size_y, 30) 
    undock_button.clicked.connect(self.undock_test)

    x = x + self.__size_y + self.__gap_x
    y = self.__start_y1 - 80
    dock_button = QPushButton(u"DOCKING", self)
    dock_button.setGeometry(x,y,self.__size_y, 30) 
    dock_button.clicked.connect(self.dock_test)

    x = self.__start_x1
    y = self.__start_y1 - 30
    self.__ir_label = QLabel(self)
    self.__ir_label.setFont(QFont(u"나눔고딕", 25))
    self.__ir_label.setAlignment(QtCore.Qt.AlignCenter)
    self.__ir_label.setStyleSheet("border:3px solid rgb(255,255,255); ")
    self.__ir_label.setGeometry(x, y, self.__size_data, self.__size_y)

    y = self.__start_y1  + 140
    go_to_button = QPushButton(u"GO TO INIT", self)
    go_to_button.setGeometry(x,y,self.__size_y, 30) 
    go_to_button.clicked.connect(self.go_to_init)


    x = x + self.__size_y + self.__gap_x
    y = self.__start_y1  + 140
    go_to_button = QPushButton(u"GO TO GOAL", self)
    go_to_button.setGeometry(x,y,self.__size_y, 30) 
    go_to_button.clicked.connect(self.go_to_test)

    self.show()
    # self.showFullScreen()

#================================================================
# function
#================================================================
  def spin(self, tmp) :
    if not rospy.is_shutdown():
      rospy.spin()

  def dock_callback(self, msg):
    print 'msg.data : ' + str(msg.data)  
  
    dock_singal = 'DOCK|'
    dock_singal = dock_singal + str(msg.data)
    self.__comm.signal.emit(dock_singal)

  def get_signal(self, s):
    if str(s).startswith('DOCK|'):
      dock_str = str(s).replace('DOCK|', '')
      self.__ir_label.setText(dock_str)
      if dock_str == 'True':
          print '111111111111111'
          self.__ir_label.setText('Charging Success')
      else:
          print '22222222222222222'
          undock_srv = LeaveStationRequest()
          self.__ir_label.setText('Charging Failed')
          self.__leave_service(undock_srv)

  def undock_test(self):
    print 'undock push'
    self.__ir_label.setText('Charging Failed')
    undock_msg = Bool()
    undock_msg.data = False
    self.__dock_publish.publish(undock_msg)
  def dock_test(self):
    print 'dock push'
    dock_srv = DockOnStationRequest()
    self.__dock_service(dock_srv)

  # def reset_test(self):
  #   self.__reset_pub.publish(Empty())

  def go_to_init(self):
    go_init_msg = Bool()
    go_init_msg.data = True
    self.__go_to_init_pub.publish(go_init_msg)

  def go_to_test(self):
    go_goal_msg = Bool()
    go_goal_msg.data = True
    self.__go_to_goal_pub.publish(go_goal_msg)



#================================================================
# MAIN
#================================================================
def main():
  print 'recog_user_pos_ui v 1.0.1'
  qt_app = QApplication(sys.argv)
  rospy.init_node('recog_user_pos_ui', anonymous=True)
  ChargerUI()
  qt_app.exec_()

if __name__ == '__main__':
    main()
