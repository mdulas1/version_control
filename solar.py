import datetime

panel_watt = 500
sunlight = datetime.datetime.now().hour
panel_efficiency = 0.36


if 6 > sunlight < 18:
  switch = True
else:
  switch = False

daily_generated_charge = panel_efficiency * panel_watt * sunlight
 
if switch:
  print(f"estemated energy is {daily_generated_charge:,.2f}")
  print("the solar is ON (daytime)")
else:
  print(f"the solar is OFF {daily_generated_charge * 0}")