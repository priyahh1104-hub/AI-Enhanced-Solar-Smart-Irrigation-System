#AI-Enhanced Solar Smart Irrigation Syatem
def monitor_soil_moisture():
    moisture_level = 35  # Sample value
    return moisture_level

def weather_prediction():
    weather = "No Rain Expected"
    return weather

def control_water_pump(moisture_level):
    if moisture_level < 40:
        print("Water Pump ON")
    else:
        print("Water Pump OFF")

# Main Program
moisture = monitor_soil_moisture()
weather = weather_prediction()

print("Soil Moisture Level:", moisture)
print("Weather Forecast:", weather)

control_water_pump(moisture)
