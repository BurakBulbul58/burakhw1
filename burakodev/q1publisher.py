#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from itu_asteam.msg import mesaj



def fonksiyon():
    pub2=rospy.Publisher("topic",mesaj,queue_size=10)
    rospy.init_node("Publisher_node",anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        bilgi =mesaj()
        bilgi.x=1.0
        bilgi.aci=60
        pub2.publish(bilgi)
        rate.sleep()
if __name__=="__main__":
    try:
        fonksiyon()
    except:
        pass