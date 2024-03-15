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

is_interrupted = False

_total_filled = 0

def fill_kg (desired_kg, fill_rate) :

    global _total_filled
    global current_fuel
    global is_interrupted

    result_kg = current_fuel + desired_kg

    _total_filled = 0

    while _total_filled < desired_kg :

        print(is_interrupted)
        
        if is_interrupted == True :

            print("interrupted filling")

            return

        time.sleep(1)

        _total_filled += fill_rate
        current_fuel += fill_rate

        print(_total_filled, " ", current_fuel)

    if current_fuel > result_kg :
        current_fuel = result_kg

# Fills a desired ammount of fuel in kg to the aircraft.
def fill_fuel_kg (desired_ammount) :

    global FUEL_RATE_KG

    fill_kg(desired_ammount, FUEL_RATE_KG)

    print("Fuel filling complete\nAMMOUNT: ", current_fuel)

# Fills a desired ammount of payload in kg to the aircraft.
def fill_payload_kg (desired_ammount) :

    global PAYLOAD_RATE_KG

    fill_kg(desired_ammount, PAYLOAD_RATE_KG)

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

def interrupt_filling () :

    global is_interrupted

    is_interrupted = True

fill_fuel_kg(340)