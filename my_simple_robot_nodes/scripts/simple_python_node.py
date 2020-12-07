#!/usr/bin/env python3
"""
    Simple ROS node in Python

    Author: Jari Honkanen
"""

import rospy

if __name__ == "__main__":
    
    # Initialize Node
    rospy.init_node("simple_python_node")
    rospy.loginfo("[INFO] simple_python_node has started")

    rospy.sleep(0.5)  # Sleep 0.5 seconds
    rospy.loginfo("[INFO] my_first_python_node ready")    

    rate = rospy.Rate(10)  # Set execution rate to 10 Hz
    count = 0

    while not rospy.is_shutdown():
        msg = "[INFO] Hello from simple_python_node, #%d" % count
        rospy.loginfo(msg)
        count += 1
        rate.sleep()   # Sleep to keep 10Hz rate


