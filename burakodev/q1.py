#!/usr/bin/env python
import rospy
from turtlesim.msg import Pose 
from itu_asteam.msg import mesaj



def callback_func(msg:Pose):
    mesajim=mesaj()
    mesajim.aci=msg.theta
    mesajim.x=msg.linear_velocity
    pub.publish(mesajim)
def callback_func2(bilgi):
    rospy.loginfo("X:"+str(bilgi.x)+"aci:"+str(bilgi.aci*57.2958))




if __name__=="__main__":
    rospy.init_node("hiz_aci")
    pub=rospy.Publisher("benim_topic",mesaj,queue_size=10)
    sub=rospy.Subscriber("/turtle1/pose",Pose,callback_func)
    sub2=rospy.Subscriber("benim_topic",mesaj,callback_func2)
    rospy.spin()