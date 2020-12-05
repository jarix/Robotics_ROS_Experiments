#!/usr/bin/env python3
"""
    ROS node doing the following
	- Subscribes to simple_number_publisher
	- Publishes the sum of received numbers
	- Provide a service to reset the count 
    
    Author: Jari Honkanen
"""

import rospy
from std_msgs.msg import Int64
from std_srvs.srv import SetBool

sum = 0
pub = None

def handle_callback_number(msg):
	global sum
	sum += msg.data
	new_msg = Int64()
	new_msg.data = sum
	pub.publish(new_msg)

def handle_callback_reset_adder(request):
	
	if request.data:
		global sum
		sum = 0
		return True, "[INFO] Counter reset successful"

	return False, "[ERROR] Counter reset failed"

if __name__ == '__main__':

	rospy.init_node("simple_number_sub_pub_srv")

	sub = rospy.Subscriber("/number", Int64, handle_callback_number)

	pub = rospy.Publisher("/number_sum", Int64, queue_size=12)

	service = rospy.Service("/reset_adder", SetBool, handle_callback_reset_adder)

	rospy.loginfo("[INFO] simple_number_sub_pub_srv started")

	rospy.spin()
