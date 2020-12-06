/*-------------------------------------------------------------------*\
  NAME
    simple_number_publisher.cpp

  DESCRIPTION
    ROS publisher node publishing an incrementing number 

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <ros/ros.h>
#include <std_msgs/Int64.h>

int main (int argc, char **argv)
{
	ros::init(argc, argv, "simple_number_publisher", ros::init_options::AnonymousName);
	ros::NodeHandle nh;

	ros::Publisher pub = nh.advertise<std_msgs::Int64>("/number", 10);
	ros::Rate rate(0.2);    // publish every 5 seconds

	ROS_INFO("[INFO] simple_number_publisher started");

	int number = 1;

	while (ros::ok()) {
		std_msgs::Int64 msg;
		msg.data = number;
		number++;
		pub.publish(msg);
		ROS_INFO("Published number %d", number);
		rate.sleep();
	}
}
