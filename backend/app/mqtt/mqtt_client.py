import paho.mqtt.client as mqtt
import logging

logger = logging.getLogger(__name__)

class MQTTClient:
    def __init__(self, broker: str, port: int, topic: str):
        self.broker = broker
        self.port = port
        self.topic = topic
        self.client = mqtt.Client(mqtt.CallbackAPIVersion.V1)
        self.connected = False
    
    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            logger.info("✅ MQTT connected")
            self.connected = True
            self.client.subscribe(self.topic)
        else:
            logger.error(f"❌ MQTT connection failed: {rc}")
    
    def on_message(self, client, userdata, msg):
        logger.info(f"📨 MQTT message: {msg.topic} = {msg.payload.decode()}")
    
    def connect(self):
        try:
            self.client.on_connect = self.on_connect
            self.client.on_message = self.on_message
            self.client.connect(self.broker, self.port, 60)
            self.client.loop_start()
        except Exception as e:
            logger.error(f"MQTT connection error: {e}")
    
    def publish(self, message: dict):
        if self.connected:
            import json
            self.client.publish(self.topic, json.dumps(message))
    
    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()
