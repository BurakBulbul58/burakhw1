#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

def fonksiyon():
    rospy.init_node("show_angle_velocity", anonymous=True)
    pub1=rospy.Publisher("/turtle1/pose",Twist, queue_size=10)
    pub2=rospy.Publisher("turtle1/cmd_vel",Pose, queue_size=10)
    vel=Twist()
    angle=Pose()
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        linex=vel.linear.x
        liney=vel.linear.y
        rospy.loginfo("x velocity is %f: y velocity is %f:",linex,liney)
        if angle.theta < 0:
            rospy.loginfo("angle is %f:",-180*angle.theta)
        else:
            rospy.loginfo("angle is %f:",180*angle.theta)
        pub1.publish(vel)
        pub2.publish(angle)
        rate.sleep()

if __name__ =="__main__":
    try:
        fonksiyon()
    except rospy.ROSInterruptException:
        pass

