#Pump controller module
def control_pump(moisture):
    if moisture < 40:
      return "Pump ON"
    else:
      return "Pump OFF"
