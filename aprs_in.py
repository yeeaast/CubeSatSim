import sys
from os import system
import RPi.GPIO as GPIO
from RPi.GPIO import output

if __name__ == "__main__":
	powerPin = 16
	txLed = 27
	change_mode = False
	debug_mode = False
	if (len(sys.argv)) > 1:
#        	print("There are arguments!")
		if ('d' == sys.argv[1]):
			debug_mode = True
			
	for line in sys.stdin:
		if (debug_mode):
			print(line, end =" ")
			
#			if '^c' == line.rstrip():
#				break

		if ((line.find("MODE=a")) > 0) or ((line.find("DTMF>APDW15:t1#")) > 0):
			system("echo '\nAPRS Mode!!\n'")
			mode = 'a'
			change_mode = True
		if ((line.find("MODE=f")) > 0) or ((line.find("DTMF>APDW15:t2#")) > 0):
			system("echo '\nFSK Mode!!\n'")
			mode = 'f'
			change_mode = True
		if ((line.find("MODE=b")) > 0) or ((line.find("DTMF>APDW15:t3#")) > 0):
			system("echo '\nBPSK Mode!!\n'")
			mode = 'b'
			change_mode = True
		if ((line.find("MODE=s")) > 0) or ((line.find("DTMF>APDW15:t4#")) > 0):
			system("echo '\nSSTV Mode!!\n'")
			mode = 's'
			change_mode = True
		if ((line.find("MODE=m")) > 0) or ((line.find("DTMF>APDW15:t5#")) > 0):
			system("echo '\nCW Mode!!\n'")
			mode = 'm'
			change_mode = True
		if (debug_mode == False)  and (change_mode == True):
			GPIO.setmode(GPIO.BCM)
			GPIO.setwarnings(False)
			GPIO.output(txLed, 0)
			GPIO.output(powerPin, 0)
			system("sudo systemctl stop rpitx")
			try:
				file = open("/home/pi/CubeSatSim/command_count.txt", "r")
				string = file.read()
				file.close()
				command_count = int(string)
				command_count += 1
				filec = open("/home/pi/CubeSatSim/command_count.txt", "w")
				command_count_string = str(command_count)
				print(command_count_string)
				string = filec.write(command_count_string)
				filec.close()
			except:
				print("Can't write command_count file!")
			print("Command_count: ")
			print(command_count)							

			print("\n/home/pi/CubeSatSim/config -" + mode)
			system("/home/pi/CubeSatSim/config -" + mode)
			change_mode = False
	print("Done")
