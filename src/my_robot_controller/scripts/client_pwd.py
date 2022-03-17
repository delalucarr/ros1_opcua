from opcua import Client
import time 
#from my_robot_controller.scripts.my_first_node import TIME, Press, Pressure, Ros1, Temp, Temparature

url ="opc.tcp://0.0.0.0:4840"
client = Client(url)

client.connect()
print("Client Connected")

while True:

    temp = client.get_node("ns= 2;i= 2")
    temp_value = temp.get_value()
    print("Temparature is {}".format(temp_value))
    time.sleep(1)
