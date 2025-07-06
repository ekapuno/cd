import RPi.GPIO as GPIO
import time

# GPIO pin where relay is connected
RELAY_PIN = 17  # Change if connected to a different pin

def setup():
    GPIO.setmode(GPIO.BCM)       # Use BCM numbering
    GPIO.setup(RELAY_PIN, GPIO.OUT)
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Default off (relay is active LOW)

def turn_on_cd_player():
    print("Turning on the CD player...")
    GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn on relay (active low)

def cleanup():
    print("Cleaning up GPIO...")
    GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn relay off
    GPIO.cleanup()

if __name__ == '__main__':
    try:
        setup()
        turn_on_cd_player()
        # Keep it on for 10 seconds, adjust as needed
        time.sleep(10)
    except KeyboardInterrupt:
        print("Interrupted by user.")
    finally:
        cleanup()
