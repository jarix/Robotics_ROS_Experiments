#! /usr/bin/env python3
"""
    Simple ROS subscriber node
    
    Receives and prints /robot_news String Message

    Author: Jari Honkanen
"""

import rospy
from std_msgs.msg import String


def callback_receive_message(msg):
    """ Callback function for received message """
    rospy.loginfo("[INFO] Message Received: ")
    rospy.loginfo(msg)


if __name__ == "__main__":

    rospy.init_node("simple_robot_receiver")

    rospy.loginfo("[INFO] simple_robot_receiver Node started")    

    # Create subscriber:  message name, message type, callback function
    sub = rospy.Subscriber("/robot_news", String, callback_receive_message)

    # Keep script running with callback active until node stopped
    rospy.spin()

