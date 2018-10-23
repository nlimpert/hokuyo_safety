#!/usr/bin/env python
import rospy
import copy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool

global filtered_data
filtered_data = None
global state
state = None
global min_range, max_range

def callback(data):
    global filtered_data, state
    state = Bool()
    filtered_data = copy.deepcopy(data)
    filtered_data.ranges = []
    global min_range, max_range
    for i in range(len(data.ranges)):
       laser_range = data.ranges[i]
       state.data = True
       if laser_range < max_range and laser_range > min_range or laser_range == float('Inf'):
           filtered_data.ranges.append(laser_range)
       else:
           filtered_data.ranges.append(0.0)
           state.data = False


def listener():
    rospy.init_node('scan_listener', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    global min_range, max_range
    min_range = rospy.get_param("min_range", 0.5)
    max_range = rospy.get_param("max_range", 1.0)
    pub = rospy.Publisher('/scan_filtered', LaserScan, queue_size=10)
    pub_bool = rospy.Publisher('/bool', Bool, queue_size=10)
    rospy.Subscriber("/scan", LaserScan, callback)

    while not rospy.is_shutdown():
        global filtered_data, state
        if filtered_data is not None and state is not None:
            pub.publish(filtered_data)
            pub_bool.publish(state)
        rate.sleep()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
