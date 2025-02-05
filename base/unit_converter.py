# 1 metre in feet.
METRE_FEET = 3.28084
# 1 metre in nautical miles.
METRE_NMILE = .0005399568

# 1 litre in US gallons.
LITRE_USG = .264172
# 1 litre of 100LL fuel in kilos.
LITRE_100LL = .72
# 1 litre of JetA fuel in kilos.
LITRE_JETA = .78

# 1 hectopascal in inches of mercury.
HPA_INHG = 0.0295299830
# 1 hectopascal in torr.
HPA_TORR = 0.7500617

# 1 kilometre per hour in knots.
KMPH_KT = METRE_NMILE * 1000
# 1 kilometre per hour in miles per hour.
KMPH_MPH = 0.6213712

# DISTANCE / ALTITUDE #

# Converts the given value of metres to feet.
def metre_to_feet (value) :
    return value * METRE_FEET

# Converts the given value of feet to metres.
def feet_to_metre (value) :
    return value / METRE_FEET

# Converts the given value of kilometres to feet.
def kmetre_to_feet (value) :
    return metre_to_feet(value) * 1000

# Converts the given value of feet to kilometres.
def feet_to_kmetre (value) :
    return feet_to_metre(value) / 1000

# Converts the given value of metres to nautical miles.
def metre_to_nmile (value) :
    return value * METRE_NMILE

# Converts the given value of nautical miles to metres.
def nmile_to_metre (value) :
    return value / METRE_NMILE

# Converts the given value of kilometres to nautical miles.
def kmetre_to_nmile (value) :
    return metre_to_nmile(value) * 1000

# Converts the given value of nautical miles to kilometres.
def nmile_to_kmetre (value) :
    return nmile_to_metre(value) / 1000

# VOLUME #

# Converts the given value of litres to US gallons.
def litre_to_usgallon (value) :
    return value * LITRE_USG

# Converts the given value of US gallons to litres.
def usgallon_to_litre (value) :
    return value / LITRE_USG

# FUEL #

# Converts the given value of litres of 100LL fuel to kilos.
def litre_to_kg_100LL (value) :
    return value * LITRE_100LL

# Converts the given value of kilos of 100LL to litres.
def kg_100LL_to_litre (value) :
    return value / LITRE_100LL

# Converts the given value of litres of JetA to kilos.
def litre_to_kg_jetA (value) :
    return value * LITRE_JETA

# Converts the given value of kilos of JetA to litres.
def kg_jetA_to_litre (value) :
    return value / LITRE_JETA

# print(round(kg_jetA_to_litre(519), 3))

# PRESSURE #

# Converts the given value of hectopascals to inches of mercury.
def hpa_to_inhg (value) :
    return value * HPA_INHG

# Converts the given value of inches of mercury to hectopascals.
def inhg_to_hpa (value) :
    return value / HPA_INHG

# Converts the given value of hectopascals to torr.
def hpa_to_torr (value) :
    return value * HPA_TORR

# Converts the given value of torr to hectopascals.
def torr_to_hpa (value) :
    return value / HPA_TORR

# Converts the given value of inches of mercury to torr.
def inhg_to_torr (value) :
    return hpa_to_torr(inhg_to_hpa(value))

# Converts the given value of torr to inches of mercury.
def torr_to_inhg (value) :
    return hpa_to_inhg(torr_to_hpa(value))

# SPEED #

# Converts the given value of kilometres per hour to knots.
def kmph_to_knot (value) :
    return value * KMPH_KT

# Converts the given value of knots to kilometres per hour.
def knot_to_kmph (value) :
    return value / KMPH_KT

# Converts the given value of kilometres per hour to miles per hour.
def kmph_to_mph (value) :
    return value * KMPH_MPH

# Converts the given value of miles per hour to kilometres per hour.
def mph_to_kmph (value) :
    return value / KMPH_MPH

# Converts the given value of knots to miles per hour.
def knot_to_mph (value) :
    return kmph_to_mph(knot_to_kmph(value))

# Converts the given value of miles per hour to knots.
def mph_to_knot (value) :
    return kmph_to_knot(mph_to_kmph(value))

print(round(litre_to_kg_jetA(25000), 1))