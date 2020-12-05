
/*-------------------------------------------------------------------*\
  NAME
    simple_adder_client.cpp

  DESCRIPTION
    Simple ROS Service that adds two integers

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <ros/ros.h>
#include <rospy_tutorials/AddTwoInts.h>


int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_adder_client");
    ros::NodeHandle nh;

    ros::ServiceClient client = nh.serviceClient<rospy_tutorials::AddTwoInts>("/add_two_ints");
    
    rospy_tutorials::AddTwoInts msg;
    msg.request.a = 7;
    msg.request.b = 8;

    if (client.call(msg)) {
        ROS_INFO("[RESULT] Sum = %d", int(msg.response.sum));
    } else {
        ROS_WARN("[ERROR] Service call failed");
    }

}