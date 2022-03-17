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
    # server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    url ="opc.tcp://0.0.0.0:4840"
    server.set_endpoint(url) 
    name = "OPCUA_SIMULATION_SERVER_ROS1"
    #addspace = server.register_namespace(name)

    # setup our own namespace, not really necessary but should as spec
    #uri = "http://.freeopcua.examplesgithub.io"
    idx = server.register_namespace(name)

    # get Objects node, this is where we should put our nodes
    node = server.get_objects_node()

    Param = node.add_object(idx , "PARAMETERS")
    Temp =  Param.add_variable(idx,"Temparature",0)
    Press = Param.add_variable(idx,"Presure",0)
    Time = Param.add_variable(idx,"Time",0)
    Dell = Param.add_variable(idx,"Ros1",0)


    Temp.set_writable()
    Press.set_writable()
    Time.set_writable()
    Dell.set_writable()


    # starting!
    server.start()
    print("Server started at {}." ,format(url))

    try:
        count = 0
        while True:
            Temparature = randint(10,50)
            Pressure = randint(200,500)
            TIME = datetime.datetime.now()
            Ros1 = randint(1,5)


            print(Temparature,Press,TIME)

            Temp.set_value(Temparature)
            Press.set_value(Pressure)
            Time.set_value(TIME)
            Dell.set_value(Ros1)


            time.sleep(1)
            count += 0.1



           # myvar.set_value(count)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()