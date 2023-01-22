#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
 

def move_turtle(line_vel):
    rospy.init_node("turtlemove", anonymous=True)
    pub=rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    rate =rospy.Rate(10)

    vel = Twist()
    while True:
        vel.linear.x=line_vel
        vel.linear.y=0
        vel.linear.z=0
        vel.angular.x=0
        vel.angular.y=0
        vel.angular.z=0

        rospy.loginfo("Linear velocity is %f: ", line_vel)
        pub.publish(vel)
        rate.sleep()

if __name__=="__main__":
    while not rospy.is_shutdown():
        try:
            move_turtle(1.0)
        except rospy.ROSInterruptException:
            pass