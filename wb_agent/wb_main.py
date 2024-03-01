import time

# The ammount of fuel in KG per second that is filled into the plane
fuel_rate_kg = 15.42

current_fuel = 0
total_filled = 0

def fill_fuel_kg (quantity_kg) :

    global current_fuel
    global total_filled

    while total_filled < quantity_kg :

        time.sleep(1)

        current_fuel += fuel_rate_kg
        current_fuel = round(current_fuel)
        total_filled += fuel_rate_kg
        total_filled = round(total_filled)

        if total_filled > quantity_kg :
            total_filled = quantity_kg

fill_fuel_kg(548)