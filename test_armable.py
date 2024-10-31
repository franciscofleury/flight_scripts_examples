import time
from copter import Copter

# CHANGE THE VALUES IN THIS DICTIONARY TO MATCH THE ONES IN YOUR SITL INSTANCE
copter_params = {
    "sysid": 10,
    "connection_string": "udpin:127.0.0.1:17171", 
}

def big_print(text):
    print("##################################################################################")
    print("########## %s  ##########" % text)
    print("##################################################################################")

big_print("Test armable")
copter = Copter(sysid=int(copter_params['sysid']))

big_print("Let's connect on " + str(copter_params['connection_string']))
copter.connect(connection_string=str(copter_params['connection_string']))

big_print("Let's wait ready to arm")
# We wait that can pass all arming check
copter.wait_ready_to_arm()


big_print("Let's arm the vehicle for 5 seconds")
copter.arm_vehicle()


time.sleep(5)

copter.disarm_vehicle()