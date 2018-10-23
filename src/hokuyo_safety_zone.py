#!/usr/bin/env python
import rospy
import copy
from sensor_msgs.msg import LaserScan

global pub

def callback(data):
    filtered_data = copy.deepcopy(data)
    filtered_data.ranges = []
    for i in range(len(data.ranges)):
       laser_range = data.ranges[i]
       if laser_range < 1.0 and laser_range > 0.05:
           filtered_data.ranges.append(laser_range)
       else:
           filtered_data.ranges.append(0.0)
    global pub
    pub.publish(filtered_data)




def listener():

    rospy.init_node('scan_listener', anonymous=True)

    global pub
    pub = rospy.Publisher('/scan_filtered', LaserScan, queue_size=10)
    rospy.Subscriber("/scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
