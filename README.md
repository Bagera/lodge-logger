# Pybytes Home Sensor

**Victor Baquero Wihlborg (vb222pw)**

---

_This project started as a very different beast. It was an esp32 as the device with some sensors, firebase as backend and a simple web app displaying the data. In the end I had to abandon that setup as I was having too many problems with connecting the esp32 and firebase. I had taken on too big a challenge and time ran out and I had to pivot the project to a simpler setup._

The Pybytes Home Sensor is a IoT project sensing temperature, humidity, barometric pressure and ambient light and then logging it on Pybytes via wifi. The data is then displayed on the Pybytes project dashboard.

It uses the FiPy and Pysense 2 board but it could use any Pycom board that can connect to the PySense 2. The project can be completed in about two hours.

## Objective

I made ths project as I want to know and log how the indoor climate of my cabin at Söderåsen. As electric prices skyrocket I want to be able to check that I have the lowest possible temperature for everything to still be ok. In all sincerity it's also a fun project that I have been wanting to do. It's just the beginning of a smart cabin that will have self watering planting beds

The purpose of this project is to explore Pybytes and what can be made with just the devboard and a shield. It's supposed to be an easy introduction to IoT and what it could be used for in everyday life.

I hope this project will give me more knowledge on IoT and the different technologies it encompases. Pycom devices and Pybytes hide a lot of the complexeties but I hope this can be a starting point to learn step by step what I need to build my own backend.

## Material

### FiPy (60€)

<img src="https://i.imgur.com/2jvr4o4.png" alt="FiPy" width="160" style="float: right; margin-left: 1em;"/>

The FiPy is a bit overkill for this kind of project as it is one of PyCom's more advanced devboards. A WiPy would be enough for this project as we are not using any of the extra types of networks other than WiFi.

Pycom has made a lot of things easier with these devboards and the developer experience is much better than with esp32 boards from Adafruit or similar. There are still rough edges but these are more beginner friendly.

### Pysense2.0X (30€)

<img src="https://i.imgur.com/jb1pFRD.png" alt="FiPy" width="160" style="float: left; margin-right: 1em;"/>

To be able to program the devboard we need some kind of shield like the pysense. By chance my order got upgraded to a pysense instead of expansion board and this board has all the sensors I need for this project, and a few more.

The shield also has a JST connector for a battery and a charger so I can connect a battery and have it powered while not plugged in. It turns out that connecting the USB messes with the readings of the temperature sensors.

The sensors on the board are:

- An ambient light sensor
- A combined humidity and temperature sensor
- A combined barometric pressure and temperature sensor that can be used to calculate altitude.
- A 3 axis accelerometer

### LiPo Battery (12€)

I am using a LiPo battery that I had lying around. Its just a 750mAh battery and I will get a bigger one but I want to see how long the device can be run before I have to charge the battery again.

### Where to buy

I bought everything through [Electokit](https://www.electrokit.com/) but it was a special package for this course. Pycom sells their devices through [their web store](https://pycom.io/product-category/shop/) and LiPos can be fond wherever electronics are sold.

## Seting up the developer environment

Theres some setting up that needs to be done and as is often the case, it was a bit harder on a Windows machine.

The boards have to be updated to work with the latest software.

### Flashing the firmware

Pycom has a desktop prohhram that flashes the devboard with the firmware you want, in my case with Pybytes, fairly easy. It is a very much better experience than flashing some other kind of esp32 board.

When you flash the board it also sets up wifi and the connection to Pybytes, making the connection to the backend almost too easy.

[Flashing devboards official docs](https://docs.pycom.io/updatefirmware/device/)

The harder part was flashing the firmware on the Pysense that was needed in order to use the Pycoproc_2 library. It was not very well documented and some steps are quite time sensitive.

[Flashing shields official docs](https://docs.pycom.io/updatefirmware/expansionboard/)

When the docs mention pressing the "button", it's the MCLR button that need to be pushed, just as the next step. At times the docs are not that clear about it. The Pysense has two buttons so just saying button doesn't help that much.

### Setting up the IDE

In the end this was a fairly simple thing to set up, it was just a bit frustrating until I arrived at the best combination of tools.

#### [Visual Studio Code](https://code.visualstudio.com/)

I started with VSCode as it is my main IDE for web development. I installed the Pymakr plugin to connect to the board. It was all going ok until it wasn't. It could be hard to connect to the board at times and getting to the REPL was sometimes imposible. In the end I could never upload my code to the device.

#### [Thonny](https://thonny.org/)

I then installed Thonny as it was better at setting up a connection with the board. But Thonny is not a very advanced IDE and it lacks many features that makes coding easier. I would go back and forth between Thonny and VSCode as bth had big flaws that I had to work around.

#### [Atom](https://atom.io/)

Enter Atom. I had not used Atom since VSCode was released and was hesitant to go back. The Pymakr plugin works so much better in Atom and development was fun again. As Atom is dying this year I hope Pycom will focus on making the VSCode version of Pymakr as good as it is in Atom.

#### Pymakr

This little plugin makes it a lot easier to work with micropython on devices like these. It gives you a serial monitor, a REPL and a way to upload files to the device. I would not have wanted to do all of this in a CLI. It is a little buggy though and can have a hard time finding the device at first. Updating the Pysense firmware seems to have made this better.

## Connecting the board

This is very straight forward, once you know what way to plug in the board to the shield. There is a pin 1 marking on the shield but not on the board. I looked at images to find out and later found that they had a notice about it in their web store (shoul have been in the docs too). The LED should be on the same side as the USB connector.

Once the board is connected to the shield you just have to connect the USB and start coding. All the sensors I use are on the shield.

<img src="https://i.imgur.com/gK4iTFJ.jpg" alt="All components connected" width="480" align="center" style="display:block;margin: auto;"/>

## Platform

For this project I chose the [Pybytes](https://pybytes.pycom.io/) platform. It is made by Pycom and is very easy to use with their boards. When making such a starter project I felt it was logical to use the service built specifically for the hardware and Pybytes is easy to setup and get started with. A free account lets you connect three devices.

Pybytes is a cloud platform that helps you set up the boards, has a MQTT broker to process the data from the device and helps you visualize the data on a dashboard.

In my next iteration of this project I want to have a MQTT broker in the cabin making the internet connection less vital.

The setup I'm thinking about is a Raspberry Pi with the TIG-stack that we learned about and several devices measuring things in different parts of the cabin and sending the data to the RPi.

## The Code

The Pycom boards are programmed with [MicroPython](https://micropython.org/), a slimmed down version of Python 3.

The code for this project is quite straight forward and I will just highlight some sections. All the code can be found on the [project GitHub page](https://github.com/Bagera/lodge-logger).

### Temperature

As the Pysense2.0 include two temperature sensors, one in the humidity sensor and one in the barometric pressure sensor, I use both readings. They often show different readings and I don't know which one is more correct so I just take the average.

I have noticed that while charging the board it will heat up a bit and skew the readings by around 3 degrees celsius.

```javascript=
temp1 = si.temperature() # Temp from Humidity sensor
temp2 = mpl.temperature() # Temp from Pressure sensor
tempAvg = round((temp1 + temp2) / 2, 1) # Average temperature
```

### Battery

The battery value is a bit special. Reading it, you get the voltage of the battery but while it is charging you get a 5v reading. It makes the reading a bit unreliable and I had to take that into mind.

Pybytes interprets it as a percentage and not a voltage. This made me have to know what voltage the board needs to run. The board shuts down at about 3.29v so I set 3.3 as the floor to have a itty bitty margin.

I also dont want the dashboard to report 150% as the value when charging so I set 4v as max and clamped it.

```javascript=
batVolt = py.read_battery_voltage(), 2 # Battery voltage
batPercent = int((min(4, batVolt) - 3.3) / 0.7 * 100)
```

### Sending the data

Pybytes makes this very easy. I just round the values to one decimal and send them through the built in library. I had to ectend the sleep before deep sleep a bit as it was kicking in before the transmissions were done.

```javascript=
# Saving signal numbers to constants dfor easy management
TEMP_SIGNAL = 0
HUMIDITY_SIGNAL = 1
PRESSURE_SIGNAL = 2
BATTERY_SIGNAL = 3
LUX_SIGNAL = 4

pybytes.send_signal(TEMP_SIGNAL, tempAvg)
pybytes.send_signal(HUMIDITY_SIGNAL, hum)
pybytes.send_signal(PRESSURE_SIGNAL, pres)
pybytes.send_signal(BATTERY_SIGNAL, batPercent)
pybytes.send_signal(LUX_SIGNAL, lux)
```

## Transmitting

I send the data once every hour. This is "live" enough for me and saves battery energy. Each packet sent is 8 bytes and it is four packets in total. A future version could maybe just send data if it was changed to save more energy. I would have to persist the data somehow then as the Pyproc deep sleep resets the devboard. I would also have to control the WiFi connection and skip it if no data has to be sent.

### WiFi

As the device will be sitting indoors in range of a WiFI router it made sense to use that wireless protocol. The drawbacks are energy consumption that will affect battery life. In the future I would like to test other protocols as LoRa and SigFox.

### MQTT

The Pybytes libraries make the use of MQTT automatic and easy. I send my MQTT messages, every measurement seperately, to Pybytes and they are saved there to be interpreted in the dashboard. The data sent is signal number and a value that I have rounded to two decimals.

## The Dashboard

Whenever Pybytes receives a signal it is saved in the device database and can be accessed for 30 days on a free account.

I made the dashboard in Pybytes with their ready-made widgets. The widgets are not the best as they do not even include a widget corresponding to every sensor on the shields and they are not very responsive. Sometimes the numbers overflow because they have 10 or more decimals even though the number sent from the device only has 2. The graphs available seem to be very buggy and hard to use.

<img src="https://i.imgur.com/TRw2iFp.png" alt="IoT device in a window with potted plants" align="center" style="display:block;margin: 1em  auto 0;"/>

## Final Thoughts

<figure>
  <img src="https://i.imgur.com/R6Lkqet.jpg" alt="IoT device in a window with potted plants" align="center" style="display:block;margin: 1em  auto 0;"/>
  <figcaption>The device being tested in a real environment before cabin deployment.</figcaption>
</figure>

This project did not go as planned and I had to scrap everything I had on friday morning to make a much simpler project. I want to revisit this in a few different ways in the future.

- I want to make the device with a Raspery Pi Pico W and sensors soldered to a board. I will also look into ESPNow and ESPHome to see if these could be interesting projects for me.
- Make a custom backend with a gateway that connects to several devices and keeping my data more private. Maybe Home Assistant for Raspberry Pi could be of interest here.
- I want to make a nice 3d printed case for the device. I think this will be the first thing I do after this course ends. Preferably it will be a case that can be used by others that have Pycom devices.
