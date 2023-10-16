
weapon_cut = 2.64
weapon_smash = 2

weapon_level = 20
agile = 70
power = 90

if weapon_cut > weapon_smash:
    majar_damage = 20 + (0.4*weapon_cut*(agile+weapon_level))
    minor_damage = 0 + (0.5*weapon_smash*(power+weapon_level))
else:
    majar_damage = 20 + (0.4*weapon_smash*(power+weapon_level))
    minor_damage = 8 + (0.46*weapon_cut*(agile+weapon_level))

total = majar_damage + minor_damage
print('total:', total)