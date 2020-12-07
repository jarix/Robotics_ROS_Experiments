#!/usr/bin/env python3
"""
    ROS publisher node publishing an incrementing number 
	Reads the publish rate from ROS Parameter server
    
    Author: Jari Honkanen
"""

import rospy
from std_msgs.msg import Int64

if __name__ == '__main__':

	rospy.init_node("simple_number_publisher")
	pub = rospy.Publisher("/number", Int64, queue_size=10)

	rospy.loginfo("[INFO] simple_number_publisher started")

	try:
		publish_freq = rospy.get_param("/number_publish_frequency")   # Rate in Hz
	except KeyError as e:
		rospy.logwarn("[ERROR] getting number_publish_frequency failed")
		publish_freq = 1

	rate = rospy.Rate(publish_freq) 

	rospy.set_param("/number_publisher_message", "Hi, there!")

	number = 1

	while not rospy.is_shutdown():

		msg = Int64()
		msg.data = number 
		pub.publish(msg)
		rospy.loginfo("[INFO] Published number " + str(number))
		number += 1
		rate.sleep()
