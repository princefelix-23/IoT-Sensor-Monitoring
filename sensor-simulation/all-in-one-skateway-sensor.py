import time
import random
import os
from azure.iot.device import IoTHubDeviceClient, Message
from datetime import datetime 
from dotenv import load_dotenv

# This script simulates sensor data for three Rideau Canal locations (Dow's Lake, Fifth Avenue, NAC)
# and sends updates every 10 seconds to Azure IoT Hub, monitoring ice thickness, temperature, and snow conditions

#Load dotenv
load_dotenv()


# Intialize a connection strings map <location, Connection String>
# The connection string must be stored in a .env file
# install dotenv package then use os.getenv(<keyname>) to access your KEY
CONNECTION_STRINGS = {
    "Dow's Lake": os.getenv('DL_CONNECTION_STRING'),
    "Fifth Avenue": os.getenv('FA_CONNECTION_STRING'),
    "NAC": os.getenv('NAC_CONNECTION_STRING')
}

# Generates simulated telemetry data for a given location on the Rideau Canal, 
# Data includes ice thickness, surface temperature, snow accumulation, external temperature, and a timestamp.
# Generate random range from actual expected number for each data
def get_telemetry(location):
    return {
        "location": location,
        "iceThickness": random.uniform(20, 40),
        "surfaceTemperature": random.uniform(-15, 0),
        "snowAccumulation": random.uniform(5, 20),
        "externalTemperature": random.uniform(-25, 5),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }

def main():
    # Create IoT Hub clients for each location using for loops
    clients = {
        location: IoTHubDeviceClient.create_from_connection_string(conn_str)
        for location, conn_str in CONNECTION_STRINGS.items()
    }

    print("Sending telemetry to IoT Hub...")
    try:
        while True: #Infinite loop
            for location, client in clients.items(): # For each client (sensor) take the location name
                telemetry = get_telemetry(location) # set telemtry for the location
                message = Message(str(telemetry)) # create the message to process
                client.send_message(message) # send the message containing data for the location
                print(f"Sent message from {location}: {message}")
            time.sleep(10) # Send evrty 10 seconds
    except KeyboardInterrupt: 
        print("Stopped sending messages.")
    finally:
        for client in clients.values(): # Disconnect each connection using for loops
            client.disconnect()

if __name__ == "__main__":
    main()
