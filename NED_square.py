import time
from copter import Copter
from classes.pos import *
# CHANGE THE VALUES IN THIS DICTIONARY TO MATCH THE ONES IN YOUR SITL INSTANCE
copter_params = {
    "sysid": 10,
    "connection_string": "udpin:127.0.0.1:17171", 
}

def big_print(text):
    print("##################################################################################")
    print("########## %s  ##########" % text)
    print("##################################################################################")

big_print("Lets test takeoff and land")
copter = Copter(sysid=int(copter_params['sysid']))

big_print("Let's connect on " + str(copter_params['connection_string']))
copter.connect(connection_string=str(copter_params['connection_string']))

big_print("Let's do some GUIDED movement")
# We will do some guided command
copter.change_mode("GUIDED")

big_print("Let's wait ready to arm")
# We wait that can pass all arming check
copter.wait_ready_to_arm()

if not copter.armed():
    copter.arm_vehicle()

square_points = [(100,100,-50), (-100,100,-50), (-100,-100,-50), (100,-100,-50)]

if copter.armed():
    copter.user_takeoff(15)
    time.sleep(2)
    for point in square_points:
        pos = Local_pos(x=point[0],y=point[1],z=point[2])
        copter.go_to_ned(pos.x, pos.y, pos.z)
        copter.ensure_moving()
        copter.wait_ned_position(pos)
        time.sleep(1)
    copter.do_RTL()
else:
    big_print("ARM FAIL")