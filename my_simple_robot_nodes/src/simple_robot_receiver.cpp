/*-------------------------------------------------------------------*\
  NAME
    simple_robot_receiver.cpp

  DESCRIPTION
    Simple ROS subscriber node 
    Receives and prints /robot_news String Message

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <ros/ros.h>
#include <std_msgs/String.h>


// Callback function for receiving messages
void callback_receive_message(const std_msgs::String &msg)
{
    ROS_INFO("[INFO] Message Received: '%s'", msg.data.c_str());
}


int main(int argc, char **argv)
{
    // Initialize node
    ros::init(argc, argv, "simple_robot_receiver");

    ROS_INFO("[INFO] simple_robot_receiver started");

    // Instantiate node handle
    ros::NodeHandle nh;

    // topic name, queue size, callback function
    ros::Subscriber sub = nh.subscribe("/robot_news", 100, callback_receive_message);  

    // Keep node running with callback active until shutdown
    ros::spin();

}