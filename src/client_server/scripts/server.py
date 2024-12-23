#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool, SetBoolResponse

def callback(req):
 # Create the response message 
  response = SetBoolResponse ()
  
  # Execute the task
  if req.data == True:
   response.success = True
   response.message = "The device was enabled"
  else:
   response.success = True
   response.message = "The device was disabled"
   
  # Return yourresponse
  return response 
  
# Node setup
rospy.init_node("server")
rospy.Service("test_service", SetBool, callback)
rospy.spin()
