#!/usr/bin/env python3

import rospy
import rosbag
 
rospy.init_node("read_bag")
bag=rosbag.Bag("/home/sinem/catkin_ws/src/pub_sub/bag/test.bag")

for topic, msg, t in bag.read_messages(topics = ["/ask1","/ask2"]):
  if topic == "/ask1":
    print ("ask1 data is:")
    print (msg.data)
    print ("and it was recorded at:")
    print(t)
   
  if topic == "/ask2":
    print ("ask2 data is:")
    print (msg.data)
    print ("and it was recorded at:")
    print(t)
