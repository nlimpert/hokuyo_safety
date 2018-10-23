#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    for i in range(len(data.ranges)):
       laser_range = data.ranges[i]
       if laser_range < 1.0 and laser_range > 0.05:
           rospy.loginfo("scan %i range: %f", i, laser_range)


def listener():

    rospy.init_node('scan_listener', anonymous=True)

    rospy.Subscriber("/scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
