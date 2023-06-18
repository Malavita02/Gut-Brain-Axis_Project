# -*- coding: utf-8 -*-

# The following code is written in C and is intended to be used in the Arduino IDE.

"""
const int pumpPin1 = 2; 
const int pumpPin2 = 3;
const int pumpPin3 = 4;
const int pumpPin4 = 5;
const int pumpPin5 = 6;
const int pumpPin6 = 7;

// Setting the default state of the pump to off)

void setup() {
  pinMode(pumpPin1, OUTPUT);
  pinMode(pumpPin2, OUTPUT);
  pinMode(pumpPin3, OUTPUT);
  pinMode(pumpPin4, OUTPUT);
  pinMode(pumpPin5, OUTPUT);
  pinMode(pumpPin6, OUTPUT);

  digitalWrite(pumpPin1, LOW);
  digitalWrite(pumpPin2, LOW);
  digitalWrite(pumpPin3, LOW);
  digitalWrite(pumpPin4, LOW);
  digitalWrite(pumpPin5, LOW);
  digitalWrite(pumpPin6, LOW); 
}

"""

# The following code should be integrated into the PsychoPy software.

# Import necessary packages 

import serial 
import time
import logging 

# logging basic config

logging.basicConfig(
    level=logging.INFO,  
    format='%(asctime)s - [%(levelname)-8s] - %(message)s',  # Define the log message format
)
# Configure Arduino connection

arduino_port = 'COM3'  # Replace with the port where the Arduino is connected (can be found in the Arduino IDE)
baud_rate = 9600  # Number of bits transmitted per second (depends on the device, also visible in the Arduino IDE)

arduino = serial.Serial(arduino_port, baud_rate) 
time.sleep(2)  # Wait for 2 seconds to establish connection with Arduino

# Define the pump names and the pins they are connected to
pump_pins = {
    'pump1': 2,  
    'pump2': 3,  
    'pump3': 4,  
    'pump4': 5,  
    'pump5': 6,  
    'pump6': 7,  
}

# Code for the experiment until the point where pump activation is required
# ...


# When the participant selects an image, call the function activate_pump and write the number of the pump as the parameter

def activate_pump(selected_pump: int) -> None:
  if selected_pump < 1 or selected_pump > 6:
    raise ValueError("This setup only has 6 pumps")
  
  selected_pump = f'pump{selected_pump}'
  pump_pin = pump_pins[selected_pump]

  logging.info(f"Activating pump {selected_pump}...")

  # Activate the selected pump 
  arduino.write(str(pump_pin).encode())  # To communicate with the Arduino, the information needs to be sent in bits

  # Duration of pump activation in seconds
  time.sleep(1.0)  

  # Deactivate the pump
  arduino.write(b'0')

activate_pump(1)
#...

# Close the connection with Arduino at the end of the script
arduino.close()
