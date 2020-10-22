import RPi.GPIO as GPIO
import Adafruit_DHT
import sys

sys.stdout = open ("temperature.txt", "w")


dht_sensor = Adafruit_DHT.DHT11
pin = 5
humidity, temperature = Adafruit_DHT.read_retry(dht_sensor, pin)

print("Temperature:", temperature)
print("Humidity:", humidity)

sys.stdout.close()