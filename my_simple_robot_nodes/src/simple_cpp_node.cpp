
/*-------------------------------------------------------------------*\
  NAME
    simple_cpp_node.cpp

  DESCRIPTION
    Simple ROS Node 

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <ros/ros.h>


int main(int argc, char **argv)
{
    // Initialize Node
    ros::init(argc, argv, "simple_cpp_node");

    // Get Node Handle
    ros::NodeHandle nh;

    ROS_INFO("[INFO] simple_cpp_node started");

    ros::Duration(0.5).sleep();   // Sleep half a second
    ROS_INFO("[INFO] simple_cpp_node ready");

    ros::Rate rate(10);  // Set execution rate to 10Hz
    int count = 0;

    while (ros::ok())
    {
        ROS_INFO("Hello from simple_cpp_node, #%d", count++);
        rate.sleep();  // sleep to keep 10Hz
    }
}