#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback(data):
    rospy.loginfo("scan length: %i", len(data.ranges))

def listener():

    rospy.init_node('scan_listener', anonymous=True)

    rospy.Subscriber("/scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
