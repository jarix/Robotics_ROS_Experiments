#! /usr/bin/env python3
"""
    ROS publisher node publishing hardware status
    using a custom SimpleHardwareStatus message
    
    Author: Jari Honkanen
"""

import rospy
from my_simple_robot_msgs.msg import SimpleHardwareStatus   # Import custom message

if __name__ == "__main__":

    rospy.init_node("simple_status_publisher_with_custom_msg")

    rospy.loginfo("[INFO] simple_status_publisher_with_custom_msg node started")

    # publisher with message name, message type, Queue size
    pub = rospy.Publisher("/my_simple_robot/hardware_status", SimpleHardwareStatus, queue_size=10)

    rate = rospy.Rate(2)   # publish at 2Hz

    while not rospy.is_shutdown():

        msg = SimpleHardwareStatus()
        msg.status_ok = True
        msg.temp = 40 
        msg.debug_msg = "All Systems a Go"
        pub.publish(msg)
        rate.sleep()

    rospy.loginfo("[INFO] simple_status_publisher_with_custom_msg stopped")