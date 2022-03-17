from operator import ne
from re import T
from opcua import Client
import time 
#from my_robot_controller.scripts.my_first_node import TIME, Press, Pressure, Ros1, Temp, Temparature

url ="opc.tcp://10.8.0.2:4840"
client = Client(url)


client.set_user("DrNo")
client.set_password("Bond2022!")

client.connect()
print("Client Connected")

while True:

  vara = client.get_node("ns = 4;s = |var|CODESYS Control Win V3 x64.Application.PLC_PRG.a")
 # value2 = var.set_value(10)
  value_a = vara.get_value()

  varb = client.get_node("ns = 4;s = |var|CODESYS Control Win V3 x64.Application.PLC_PRG.b")
  value2 = varb.set_value(10)
  value_b = varb.get_value()
 # print(varb)
  #print("Neu Variable is = ".format(varb.get_value()))


  varc = client.get_node("ns = 4;s = |var|CODESYS Control Win V3 x64.Application.PLC_PRG.c")
 # value2 = var.set_value(10)
  value_c = varc.get_value()
 # print(varc)
  #print("Neu Variable is = ".format(varc.get_value()))


  if 'value' is not None:
    print("im here and a have something %s\n " % value_a)
    print("im here and b have something %s\n " % value_b)
    print("im here and c have something  %s\n " % value_c)

    #print("im here and i have something",value2)
  else:
    print("empty")
     
  
