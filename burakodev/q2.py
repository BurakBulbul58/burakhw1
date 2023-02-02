#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def hiz_kontrol():
    ref_hiz=1.0
    vel=Twist()
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        
        vel.linear.y=0
        vel.linear.z=0
        vel.angular.x=0
        vel.angular.y=0
        vel.angular.z=0
        if(vel.linear.x==ref_hiz):
            publisher.publish(vel)
            rate.sleep()
        else:
            vel.linear.x=ref_hiz


if __name__=="__main__":
    rospy.init_node("hiz_kontrol",anonymous=True)
    publisher=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    hiz_kontrol()