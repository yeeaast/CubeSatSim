"""Sample code and test for adafruit_in219"""
# Reads all voltage and current sensors for two I2C buses
import time
import sys
#import board
import busio
from adafruit_extended_bus import ExtendedI2C as I2C
from adafruit_ina219 import INA219
from adafruit_ina219 import ADCResolution, BusVoltageRange

if __name__ == "__main__":
#	    print 'Length: ', len(sys.argv)
  
  buses = [1, 3] # default I2C buses
  config = False
  one = two = three = four = five = six = seven = eight = 0
  
  if (len(sys.argv)) > 1:
#   print("There are arguments!", file=sys.stderr)
#   if (('a' == sys.argv[1]) or ('afsk' in sys.argv[1])):
    buses[0] = int(sys.argv[1], base=10)
    if (len(sys.argv)) > 2:
      buses[1] = int(sys.argv[2], base=10)
      if (len(sys.argv)) > 3:
        if sys.argv[3] == "c":
          config = True
          
  print(buses[0])
  print(buses[1])

  addresses = [0x40, 0x41, 0x44, 0x45] #INA219 addresses on the bus
#  print("buses: ", buses, " addr: ", addresses, file=sys.stderr)

# config

#  for x in buses:
#    try:
#      i2c_bus = I2C(x) # Device is /dev/i2c-x
#      for y in addresses:
#        print(x,y)
#        try:
  # Create library object using  Extended Bus I2C port
#          print("bus: ", x, " addr: ", y)
#          if x == 0 and y == 0x45:
#           print("Reading INA219 in MoPower Board")
#            i2c_bus = I2C(1)
#            ina219 = INA219(i2c_bus, 0x4a)
#          else:
#            ina219 = INA219(i2c_bus, y)
#          print("ina219 test")
  
#          print("Configuring")
# optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
#          ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
#          ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
# optional : change voltage range to 16V
#          ina219.bus_voltage_range = BusVoltageRange.RANGE_16V
#        except:
#          print("Python Error 2", file=sys.stderr, flush=True)
#    except:
#      print("Python Error 1", file=sys.stderr, flush=True)
# No try checking yet
  
#  if buses[0] == 0 and addresses[0] == 0x45:
#    print("Reading INA219 in MoPower Board")
#    ina219_one = INA219(I2C(1), 0x4a) 
#  else:
  if (buses[0] != -1):
    try:
      i2c_one = I2C(buses[0])
      try:
        ina219_one = INA219(i2c_one, addresses[0])
        ina219_one.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_one.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_one.bus_voltage_range = BusVoltageRange.RANGE_16V
        one = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
      try:  
        ina219_two = INA219(i2c_one, addresses[1])
        ina219_two.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_two.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_two.bus_voltage_range = BusVoltageRange.RANGE_16V
        two = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
      try:  
        ina219_three = INA219(i2c_one, addresses[2])
        ina219_three.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_three.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_three.bus_voltage_range = BusVoltageRange.RANGE_16V
        three = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
      try:  
        ina219_four= INA219(i2c_one, addresses[3])
        ina219_four.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_four.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_four.bus_voltage_range = BusVoltageRange.RANGE_16V
        four = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
    except:
      print("Python Error 5",  file=sys.stderr, flush=True)
      
  if (buses[1] != -1):
    try:
      i2c_two = I2C(buses[1])
      print(i2c_two)
      try:  
        ina219_five = INA219(i2c_two, addresses[0])  
        ina219_five.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_five.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_five.bus_voltage_range = BusVoltageRange.RANGE_16V
        five = 1  
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
      try:  
        ina219_six = INA219(i2c_two, addresses[1]) 
        ina219_six.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_six.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_six.bus_voltage_range = BusVoltageRange.RANGE_16V
        six = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
      try:  
        ina219_seven = INA219(i2c_two, addresses[2]) 
        ina219_seven.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_seven.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_seven.bus_voltage_range = BusVoltageRange.RANGE_16V
        seven = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
      try:  
        ina219_eight = INA219(i2c_two, addresses[3]) 
        ina219_eight.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S   # 1S
        ina219_eight.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S     # 1S
        ina219_eight.bus_voltage_range = BusVoltageRange.RANGE_16V
        eight = 1
      except:
        print("Python Error 3", file=sys.stderr, flush=True)
    except:
      print("Python Error 5",  file=sys.stderr, flush=True)

  while (True):
    if (oneF == 1):
      print("{:6.3f} ".format(ina219_one.bus_voltage), "{:6.3f} ".format(ina219_one.current) , end = '')
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (two == 1):  
      print("{:6.3f} ".format(ina219_two.bus_voltage), "{:6.3f} ".format(ina219_two.current) , end = '') 
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (three == 1):  
      print("{:6.3f} ".format(ina219_three.bus_voltage), "{:6.3f} ".format(ina219_three.current) , end = '') 
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (four == 1): 
      print("{:6.3f} ".format(ina219_four.bus_voltage), "{:6.3f} ".format(ina219_four.current) , end = '') 
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (five == 1): 
      print("{:6.3f} ".format(ina219_five.bus_voltage), "{:6.3f} ".format(ina219_five.current) , end = '') 
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (six == 1): 
      print("{:6.3f} ".format(ina219_six.bus_voltage), "{:6.3f} ".format(ina219_six.current) , end = '')       
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (seven == 1): 
      print("{:6.3f} ".format(ina219_seven.bus_voltage), "{:6.3f} ".format(ina219_seven.current) , end = '') 
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    if (eight == 1): 
      print("{:6.3f} ".format(ina219_eight.bus_voltage), "{:6.3f} ".format(ina219_eight.current) , end = '') 
    else:
      print("{:6.3f} ".format(0),  "{:6.3f} ".format(0), end = '') 
    print(" ")
    inp = input()
#   print(inp)
