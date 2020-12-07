
/*-------------------------------------------------------------------*\
  NAME
    simple_robot_transmitter.cpp

  DESCRIPTION
    Simple ROS publisher node  
    Transmits /robot_news String Message at 1Hz

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <string>

#include <ros/ros.h>
#include <std_msgs/String.h>


int main(int argc, char **argv)
{
    // Initialize node
    ros::init(argc, argv, "simple_robot_transmitter");

    ROS_INFO("[INFO] simple_robot_transmitter started");

    // Instantiate node handle
    ros::NodeHandle nh;

    // Create publisher
    ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news", 10);  // message name and queue size

    ros::Rate rate(1);  // 1 Hz

    int count = 0;

    while (ros::ok())
    {
        std_msgs::String msg;
        msg.data = "Hello, this is a message from the Simple Robot Transmitter, #" + std::to_string(count++); 

        pub.publish(msg);
        rate.sleep();
    }
}