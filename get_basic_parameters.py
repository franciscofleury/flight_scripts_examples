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

big_print("Get parameters")
copter = Copter(sysid=int(copter_params['sysid']))

big_print("Let's connect on " + str(copter_params['connection_string']))
copter.connect(connection_string=str(copter_params['connection_string']))

big_print("Let's change some parameters")
print("RTL_ALT value %f" % copter.get_parameter("RTL_ALT"))
copter.set_parameters({"RTL_ALT": 2000})
print("RTL_ALT value %f" % copter.get_parameter("RTL_ALT"))
print("BATT_CAPACITY value %f" % copter.get_parameter("BATT_CAPACITY"))
print("\n\n\n")