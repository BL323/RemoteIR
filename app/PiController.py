import os

def PiOn():
        print "Turning On..."
	os.system("irsend SEND_ONCE PanasonicTV KEY_VOLUMEUP")
	os.system("irsend SEND_ONCE PanasonicTV KEY_VOLUMEUP")

	

def PiOff():
        print "Turning Off.."
	os.system("irsend SEND_ONCE PanasonicTV KEY_VOLUMEDOWN")
	os.system("irsend SEND_ONCE PanasonicTV KEY_VOLUMEDOWN")

def PiSchedule():
        print "To Schedule"
