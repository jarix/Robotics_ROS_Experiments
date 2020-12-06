#!/usr/bin/env python3
"""
    Simple ROS client for /add_two_ints service
    
    Author: Jari Honkanen
"""

import rospy
from rospy_tutorials.srv import AddTwoInts

if __name__ == "__main__":

    rospy.init_node("simple_adder_client")
    rospy.wait_for_service("/add_two_ints")   # Block until service is advertised

    try:
        add_two_ints = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        a = 7
        b = 8
        response = add_two_ints(a,b)
        rospy.loginfo("[RESULT] " + str(a) + " + " + str(b) + " = " + str(response.sum))

    except rospy.ServiceException as e:
        rospy.logwarn("[ERROR] Service call failed: " + str(e))