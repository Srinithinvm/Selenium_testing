import paho.mqtt.client as mqttClient
import threading
import time
import json


broker = "mqtt.univa.cloud"
port = 1883
sub_topic = "device1response"
pub_topic = "device1request"
client_id = "mqttx_65e39f07"

# Initialize MQTT client with client ID
client = mqttClient.Client(client_id)

# Define the callback function for receiving messages
def on_message(client, userdata, message):
    print(f"Received message: {message.payload.decode()} on topic: {message.topic}")

# Assign callback function
client.on_message = on_message

# Subscriber function
def subscriber():
    # client.connect(broker, port)
    
    client.subscribe(sub_topic)
    client.loop_forever()

# Publisher function
def publisher():
    time.sleep(2)  # Give the subscriber some time to connect
    client.connect(broker, port)
    print("Connected to broker...")
    timestamp = time.time()
    print(timestamp)
    # Example JSON payloads to publish
    payloads = [
        {"timestamp": 1721813901, "device_token": "device-token-10", "machineid-1": 85 },
        {"timestamp": 1721813881, "device_token": "device-token-10", "machineid-1": 7 },
        {"timestamp": 1721813882, "device_token": "device-token-100", "machineid-1": 82 },
        {"timestamp": 1721813874, "device_token": "device-token-10", "machineid-1": 83 },
        {"cmd": "TIMESTAMP", "device_token": "device-token-10" },
        
    ]
    
    for payload in payloads:
        client.publish(pub_topic, json.dumps(payload))  # Publish each payload



publisher()
subscriber()