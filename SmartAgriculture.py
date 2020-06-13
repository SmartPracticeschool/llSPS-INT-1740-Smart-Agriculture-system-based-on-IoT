import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device
#provide your IBM Watson Device Credentials
organization = "09sf66"#replace the ORG ID
deviceType = "IOTDevice"#replce the device type
deviceId = "Motor"#replace device ID
authMethod = "token"
authToken = "hQh4@8a6HQ?l*6FX*K"#replace the authToken
# function for Callback

def myCommandCallback(cmd): # function for Callback
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='motoron':
                print("MOTOR ON IS RECEIVED")
        elif cmd.data['command']=='motoroff':
                print("MOTOR OFF IS RECEIVED")
        if cmd.command == "setInterval":
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)
try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()
# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()
while True:
        deviceCli.commandCallback = myCommandCallback
# Disconnect the device and application from the cloud
deviceCli.disconnect()
