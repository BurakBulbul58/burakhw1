import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import time
import math



ref_x=2
ref_y=2
def go2goal(velocity_publisher, x_goal, y_goal):
    global x 
    global y 
    global yaw
    if(x_goal!=ref_x or y_goal!=ref_y):
        x_goal=ref_x
        y_goal=ref_y

    velocity_message=Twist()
    rate=rospy.Rate(10)
    while True:
        K_linear=0.5
        distance=abs(math.sqrt(((x_goal-x)**2)+((y_goal-y)**2)))
        linear_speed=distance*K_linear

        K_angular=4
        
        desired_angle_goal=math.atan2(y_goal-y, x_goal-x)
        angular_speed=(desired_angle_goal-yaw) * K_angular
        
        velocity_message.linear.x=linear_speed
        velocity_message.angular.z=angular_speed
        velocity_publisher.publish(velocity_message)
        rate.sleep()

        print(distance)
       
        if(distance<0.01):
            break   
def poseCallback(pose_message:Pose):
    global x
    global y 
    global yaw
    x=pose_message.x
    y=pose_message.y
    yaw=pose_message.theta
if __name__=="__main__":
    try:
        rospy.init_node("robot_cleaner",anonymous=True)
        velocity_publisher=rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
        velocity_subscriber=rospy.Subscriber("/turtle1/pose",Pose,poseCallback)
        time.sleep(2)
        go2goal(velocity_publisher,3,3)
    except:
        pass
