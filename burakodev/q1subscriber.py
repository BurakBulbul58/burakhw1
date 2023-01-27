#!/usr/bin/env python3
import rospy
from turtlesim.msg import Pose
from itu_asteam.msg import mesaj
def callback_func(bilgiler):
        rospy.loginfo("X: %f aci: %f",bilgiler.x,bilgiler.aci)
        


def fonksiyon():
        rospy.init_node("subscriber",anonymous=True)
        sub=rospy.Subscriber("topic",mesaj,callback_func)

        rospy.spin()






if __name__=="__main__":
    fonksiyon()