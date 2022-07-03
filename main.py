import machine
import pycom
import time
from pycoproc_2 import Pycoproc
from SI7006A20 import SI7006A20
from MPL3115A2 import MPL3115A2,PRESSURE
from LTR329ALS01 import LTR329ALS01

pycom.heartbeat(False) # Turn off blinking light

py = Pycoproc() # Init coprocessor
si = SI7006A20(py) # Humidity sensor
mpl = MPL3115A2(py,mode=PRESSURE) # Pressure sensor
li = LTR329ALS01(py) # Ambient light sensor
sleeptime = 60 * 60 # 60 seconds * 60 minutes

# Saving signal numbers to constants dfor easy management
TEMP_SIGNAL = 0
HUMIDITY_SIGNAL = 1
PRESSURE_SIGNAL = 2
BATTERY_SIGNAL = 3
LUX_SIGNAL = 4

pycom.rgbled(0x007f00) # Turn on the LED to show that we are measuring

print("--- reading ---") # Print to console that work has begun

temp1 = si.temperature() # Temp from Humidity sensor
temp2 = mpl.temperature() # Temp from Pressure sensor
tempAvg = round((temp1 + temp2) / 2, 1) # Average temperature

hum = round(si.humidity(), 1) # Relative Humidity
pres = int(mpl.pressure()) # Barometric pressure
lux = li.lux(); # Ambient light

batVolt = py.read_battery_voltage(), 2 # Battery voltage
batPercent = int((min(4, batVolt) - 3.3) / 0.7 * 100)

print("Temperature: {} deg C".format(tempAvg))
print("Relative Humidity: {} %RH".format(hum))
print("Pressure: {}".format(pres))
print("Battery {}%, {}v".format(batPercent, round(batVolt, 2)))
print("Lux: {}".format(lux))

pybytes.send_signal(TEMP_SIGNAL, tempAvg)
pybytes.send_signal(HUMIDITY_SIGNAL, hum)
pybytes.send_signal(PRESSURE_SIGNAL, pres)
pybytes.send_signal(BATTERY_SIGNAL, batPercent)
pybytes.send_signal(LUX_SIGNAL, lux)

print("--- done ---")
pycom.rgbled(False) # Turn off the LED

time.sleep(10) # Time to let the messages get to the server before deep sleep
py.setup_sleep(sleeptime)
py.go_to_sleep()
