
/*-------------------------------------------------------------------*\
  NAME
    simple_adder_service.cpp

  DESCRIPTION
    Simple ROS Service that adds two integers

  AUTHOR
    Jari Honkanen
\*-------------------------------------------------------------------*/

#include <ros/ros.h>
#include <rospy_tutorials/AddTwoInts.h>

// Service callback function
bool handle_request(rospy_tutorials::AddTwoInts::Request &request,
                    rospy_tutorials::AddTwoInts::Response &response)
{
    int result = request.a + request.b;
    ROS_INFO("[INFO] %d + %d = %d", (int)request.a, (int)request.b, (int)result);
    response.sum = result;

    return true;
}


int main(int argc, char **argv)
{
    ros::init(argc, argv, "simple_adder_service");
    ros::NodeHandle nh;

    ros::ServiceServer server = nh.advertiseService("/add_two_ints", handle_request);

    ROS_INFO("[INFO] simple_adder_service started");
    ROS_INFO("[INFO] Waiting for client requests");

    // Spin here until service is killed
    ros::spin();
}