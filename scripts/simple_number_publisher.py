#!/usr/bin/env python3
"""
    ROS publisher node publishing an incrementing number 
    
    Author: Jari Honkanen
"""

import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':

	rospy.init_node("simple_number_publisher")
	pub = rospy.Publisher("/number", Int64, queue_size=10)

	rospy.loginfo("[INFO] simple_number_publisher started")

	rate = rospy.Rate(0.2)    # Publish every 5 seconds

	number = 1

	while not rospy.is_shutdown():

		msg = Int64()
		msg.data = number 
		pub.publish(msg)
		rospy.loginfo("Published number " + str(number))
		number += 1
		rate.sleep()
