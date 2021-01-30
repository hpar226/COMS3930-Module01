README.md


Required mats:  1 window with blinds, 1 Raspberry pi, 1 LED module, 1 24 inch monitor, 3 f-f wires, 
	  1 plastic baseball (optional)

Installation:  Place a 24 inch monitor facing outward in window, cutout a slit in the baseball and place LED inside baseball (optional). Close blinds behind the screen but place baseball or LED module behind the monitor.

Usage:  To display a processing-java script in full screen while running a python script to control an 8-diode LED strip. The python script has a randomizer using an API to pull the current time and slices for the digits after the seconds-decimal, and starts the LED with one color if even and another color if odd. 
	
To run both programs (Processing and ledtest.py) at boot:
	  Update /home/pi/.bashrc file with these lines:
		processing-java --sketch=/path/to/processing/folder --run
  		sudo python3 /home/pi/[yourdirectory]/ledtest.py
	
For dubugging, if Processing does not start then:
	  Navigate to:
		nano ~/.config/lxsession/LXDE-pi/autostart
	  Add to end:
		@lxterminal  #this automatically starts a command prompt at GUI boot

	

	
