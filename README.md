# micropython-ESP8266-wiegand-card-reader
Read MiFare Classic RFID Card data with Wiegand Protocol using ESP8266 (NodeMCU) Board

## Requirement

* NodeMCU board with ESP8266
* a wiegand compatible card reader (Promag MF7 is used with the example code)

## Installation

* First you have to flash micropython firmware to your ESP8266 board with esptool.py if you did not before. (to download the firmware go to https://micropython.org/download/?port=esp8266)
* Clone the project (git clone https://github.com/omur-dalan/micropython-ESP8266-DS18B20.git)
* Use any ide or cli to upload project files to the board (https://code.visualstudio.com, https://marketplace.visualstudio.com/items?itemName=pycom.Pymakr)

## Features

* Board will read the card id, facility number and prints out the card id, facility number and read count to the console
* It will blink a led if the card id is known
