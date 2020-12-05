#!/usr/bin/env python3
"""
    Simple ROS Service that adds two integers
    
    Author: Jari Honkanen
"""

import rospy
from rospy_tutorials.srv import AddTwoInts

def handle_service_call(request):
    """ Service callback function """
    sum = request.a + request.b
    rospy.loginfo(str(request.a) + " + " + str(request.b) + " = " + str(sum))
    return sum


if __name__ == "__main__":

    rospy.init_node("add_two_ints_service")
    rospy.loginfo("[INFO] /add_two_ints_service created")

    service = rospy.Service("/add_two_ints", AddTwoInts, handle_service_call)
    rospy.loginfo("[INFO] /add_two_ints_service started")
    rospy.loginfo("[INFO] waiting for client calls ...")

    # Spin here until killed
    rospy.spin()
    
