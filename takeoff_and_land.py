from copter import Copter
import time

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

big_print("Let's wait ready to arm")
# example of mavlink takeoff
copter.user_takeoff(11)

time.sleep(5)

# Get back to home
copter.land_and_disarm()