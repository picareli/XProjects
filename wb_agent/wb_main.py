import time

# The ammount of fuel in KG per second that is filled into the plane.
FUEL_RATE_KG = 15
# The rate in KG at which the payload is loaded.
PAYLOAD_RATE_KG = 1

# Attributes 

# The current ammount in kg of fuel that is loaded in the aircraft.
current_fuel = 160
# When true, signald that the filling of fuel has been interrupted by the user.
interrupt_fuel_flag = False

# The current ammount in kg of payload that is loaded in the aircraft.
current_payload = 70
# When true, signals that the filling of the payload has been interrupted by the user.
interrupt_payload_flag = False

_total_filled = 0

def fill_kg (desired_kg, fill_rate, current_kg, is_interrupted) :

    global _total_filled

    _total_filled = 0

    while _total_filled < desired_kg :
        
        if is_interrupted == True :
        
            print("interrupted filling")

            return current_kg
        
        time.sleep(1)

        _total_filled += fill_rate

        if _total_filled > desired_kg :
            _total_filled = desired_kg

        current_kg += fill_rate
        print(_total_filled, " ", current_kg)

    return current_kg

# Fills a desired ammount of fuel in kg to the aircraft.
def fill_fuel_kg (desired_ammount) :

    global current_fuel

    current_fuel = fill_kg(desired_ammount, FUEL_RATE_KG, current_fuel, interrupt_fuel_flag)

    print("Fuel filling complete\nAMMOUNT: ", current_fuel)

# Fills a desired ammount of payload in kg to the aircraft.
def fill_payload_kg (desired_ammount) :

    global current_payload

    current_payload = fill_kg(desired_ammount, PAYLOAD_RATE_KG, current_payload, interrupt_payload_flag)

    print("Payload filling complete\nAMMOUNT: ", current_payload)

# Sets the interrupt fuel filling flag to true.
def interrupt_fuel_filling () :

    global interrupt_fuel_flag
    
    interrupt_fuel_flag = True

    print("Interrupting fuel filling...")

# Sets the interrupt payload filling flag to true.
def interrupt_payload_filling () :

    global interrupt_payload_flag

    interrupt_payload_flag = True

    print("Interrupting payload filling...")


fill_fuel_kg(340)