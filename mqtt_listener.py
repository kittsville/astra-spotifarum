import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    if rc != 0:
        print("Failed to connect to broker :'(")

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(client.topic)

def start_listener(config, on_message):
    client = mqtt.Client(client_id = config['client_id'])
    client.on_connect = on_connect
    client.on_message = on_message
    client.topic = config['topic']
    client.username_pw_set(config['username'], config['password'])

    client.connect(config['host'])

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()
