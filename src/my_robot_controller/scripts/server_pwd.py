#!/usr/bin/env python3
import rospy
#server 
import time
from random import randint
import datetime

from opcua import ua, Server


if __name__ == "__main__":

    # setup our server
    server = Server()
    url ="opc.tcp://0.0.0.0:4840"
    server.set_endpoint(url) 
    name = "OPCUA_SIMULATION_SERVER_ROS1"
    idx = server.register_namespace(name)

    # get Objects node, this is where we should put our nodes
    node = server.get_objects_node()

    Param = node.add_object(idx , "PARAMETERS")
    temp =  Param.add_variable(idx,"Temparature",0)
  


    temp.set_writable()

    server.start()
    print("Server started at {}." ,format(url))

    try:
        count = 0
        while True:
            Temparature = randint(10,50)

            temp.set_value(Temparature)
        
            print(Temparature)


            time.sleep(1)




           # myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()