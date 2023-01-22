#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose

def functon(posex,posey):
    rospy.init_node("location", anonymous=True)
    pub=rospy.Publisher("/turtle1/pose", Pose, queue_size=10)
    rate=rospy.Rate(10)
    loc=Pose()
    while True:
        loc.x=posex
        loc.y=posey
        
        
        rospy.loginfo("position of x is %f: position of y is %f:",posex,posey)
        pub.publish(loc)
        rate.sleep()
if __name__=="__main__":
    while not rospy.is_shutdown():
        functon(6.0,6.0)

