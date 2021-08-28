#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print ("Number of scan points: "+ str(len(msg.ranges)))
    # values at 0 degree
    #print ("Distance at 0º: " + str(msg.ranges[0]))
    print (msg.ranges[0])
    # values at 90 degree
    #print ("Distance at 90º: " + str(msg.ranges[90]))
    # values at 180 degree
    #print ("Distance at 180º: " + str(msg.ranges[180]))
    # values at 270 degree
    #print ("Distance at 270º: " + str(msg.ranges[270]))
    # values at 360 degree
    #print ("Distance at 360º: " + str(msg.ranges[359]))

rospy.init_node('scan_values')
sub = rospy.Subscriber('/scan', LaserScan, callback)
rospy.spin()