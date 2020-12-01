#! /usr/bin/env python3
"""
    Simple ROS publisher node
    
    Transmits /robot_news String Message at 1Hz

    Author: Jari Honkanen
"""

import rospy
from std_msgs.msg import String

if __name__ == "__main__":

    rospy.init_node("simple_robot_transmitter")

    rospy.loginfo("simple_robot_transmitter Node started")

    # publisher with message name, message type, Queue size
    pub = rospy.Publisher("/robot_news", String, queue_size=10)

    rate = rospy.Rate(1)   # publish at 1Hz

    count = 0

    while not rospy.is_shutdown():

        msg = String()
        msg.data = "Hello, this is a message from the Simple Robot Transmitter, msg #%d" % count
        pub.publish(msg)
        count += 1
        rate.sleep()

    rospy.loginfo("simple_robot_transmitter Node stopped")
