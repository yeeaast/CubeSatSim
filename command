#!/bin/bash

echo -e "\nCommand and Control script for CubeSatSim v1.3.2\n"

	FILE=/home/pi/CubeSatSim/command_control
	if [ -f "$FILE" ]; then
    		echo "Radio command and control is ON"
#			echo "Turning Command and control to OFF"
#			sudo rm /home/pi/CubeSatSim/command_control
#			echo "rebooting"
#			sudo systemctl stop rpitx
#			sudo reboot now	
#		fi

	else 
    		echo "Radio command and control is OFF"

		while true
		do
			sleep 60
		done

#		exit 1
	fi

echo "Waiting 20 seconds for USB"

sleep 20

FILE=/home/pi/CubeSatSim/command_control_direwolf
if [[ $(arecord -l | grep card) ]] && [ -f "$FILE" ]; then

	echo "Starting Direwolf DTMF and APRS Command and Control"

	if [ "$1" = "d" ]; then
	
		echo "debug mode"
	
		direwolf -c /home/pi/CubeSatSim/direwolf-cc.conf -t 0l | python3 /home/pi/CubeSatSim/dtmf_aprs_cc.py d
	
	else
	
		direwolf -c /home/pi/CubeSatSim/direwolf-cc.conf -t 0l | python3 /home/pi/CubeSatSim/dtmf_aprs_cc.py
	
	fi
else

	if [ -f "$FILE" ]; then

		echo "Direwolf mode set but no USB soundcard detected!"

		echo "Trying RTL-FM for 60 seconds"
		sudo modprobe snd-aloop
		rtl_fm -M fm -f 435M -s 48k | aplay -D hw:2,0,0 -r 48000 -t raw -f S16_LE -c 1 &
		direwolf -r 48000 -c /home/pi/CubeSatSim/groundstation/direwolf/direwolf.conf -t 0 &
		sleep 60
		sudo killall -9 direwolf
		sudo killall -9 rtl_fm

		echo "Starting Carrier (squelch) Command and Control"
	else

		echo "Starting Carrier (squelch) Command and Control"

	fi

	if [ "$1" = "d" ]; then
	
		echo "debug mode"
	
		python3 /home/pi/CubeSatSim/squelch_cc.py d
	
	else
	
		python3 /home/pi/CubeSatSim/squelch_cc.py
	
	fi	 
fi
