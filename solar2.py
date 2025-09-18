panel_watt = 250
panel_efficiency = 0.18
sunlight = 5
time = 4

if 6 > sunlight < 18:
  switch = True
else:
  switch = False

current_generated = panel_watt * panel_efficiency * sunlight * time

if switch:
  print(f"the solar is ON ")
  print(f"estemeeted energy is {current_generated:,.2f}")
else:
  print('the solar is OFF')

