#!/usr/bin/env python3
"""
    Simple ROS node in Python

    Author: Jari Honkanen
"""

import rospy

if __name__ == "__main__":
    
    rospy.init_node("simple_python_node")

    rospy.loginfo("simple_python_node has started")

    rate = rospy.Rate(10)  # 10 Hz

    count = 0

    while not rospy.is_shutdown():
        msg = "Hello from simple_python_node, #%d" % count
        rospy.loginfo(msg)
        count += 1
        rate.sleep()


