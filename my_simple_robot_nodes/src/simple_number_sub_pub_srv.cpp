/*-------------------------------------------------------------------*\
  NAME
    simple_number_publisher.cpp

  DESCRIPTION
    ROS node doing the following:
	- Subscribes to simple_number_publisher
	- Publishes the sum of received numbers
	- Provide a service to reset the count 

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <ros/ros.h>
#include <std_msgs/Int64.h>
#include <std_srvs/SetBool.h>

int sum = 0;
ros::Publisher pub;

void handle_callback_number(const std_msgs::Int64& msg)
{
	sum += msg.data;
	std_msgs::Int64 new_msg;
	new_msg.data = sum;
	pub.publish(new_msg);
}

bool handle_callback_reset_adder(std_srvs::SetBool::Request &req, std_srvs::SetBool::Response &res)
{
	if (req.data) {
		sum = 0;
		res.message = "[INFO] Counter reset successful";
		res.success = true;
	}
	else {
		res.message = "[ERROR] Counter reset failed";
		res.success = false;
	}

	return true;
}


int main (int argc, char **argv)
{
	ros::init(argc, argv, "number_counter");
	ros::NodeHandle nh;

	ros::Subscriber sub = nh.subscribe("/number", 1000, handle_callback_number);

	pub = nh.advertise<std_msgs::Int64>("/number_sum", 12);

	ros::ServiceServer reset_service = nh.advertiseService("/reset_adder", handle_callback_reset_adder);

	ROS_INFO("[INFO] simple_number_sub_pub_srv started");

	ros::spin();
}
