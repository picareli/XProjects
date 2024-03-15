
METER_FEET = 3.28084
METER_NMILE = .0005399568

LITRE_USG = .264172

LITRE_100LL = .72
LITRE_JETA = .78

def litre_to_usgallon (value) :
    return value * LITRE_USG

def usgallon_to_litre (value) :
    return value / LITRE_USG

def litre_to_kg_100LL (value) :
    return value * LITRE_100LL
    
def kg_100LL_to_litre (value) :
    return value / LITRE_100LL
    
def litre_to_kg_jetA (value) :
    return value * LITRE_JETA
    
def kg_jetA_to_litre (value) :
    return value / LITRE_JETA

def meter_to_feet (value) :
    return value * METER_FEET

def feet_to_meter (value) :
    return value / METER_FEET

def kmeter_to_feet (value) :
    return meter_to_feet(value) * 1000

def feet_to_kmeter (value) :
    return feet_to_meter(value) / 1000

def meter_to_nmile (value) :
    return value * METER_NMILE

def nmile_to_meter (value) :
    return value / METER_NMILE

def kmeter_to_nmile (value) :
    return meter_to_nmile(value) * 1000

def nmile_to_kmeter (value) :
    return nmile_to_meter(value) / 1000

#def convert_units (current_unit, target_unit)

    # m to ft
    # m * ft
    # km to ft
    # km * ft
    # nm to km