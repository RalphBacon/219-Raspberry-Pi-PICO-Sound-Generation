# Import the required 'libraries' for pin definitions and PWM
from machine import Pin, PWM

# Also import a subset for sleep and millisecond sleep. If you just import
# the utime you will have to prefix each call with "utime."
from utime import sleep, sleep_ms

# Define what the buzzer object is - a PWM output on pin 15
buzzer = PWM(Pin(15))

# A list of frequencies
tones = (200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000)

# Define the function to play a single tone then stop
def buzz(freq):
    # Set the frequence
    buzzer.freq(freq)
    # Set the duty cycle (affects volume)
    buzzer.duty_u16(15000);
    # Let the sound continue for X milliseconds
    sleep_ms(100);
    # Now switch the sound off
    buzzer.duty_u16(0);
    # And delay a small amount (gap between tones)
    sleep_ms(20);
    
for tone in range(len(tones)):
    buzz(tones[tone])
    
sleep(1)
    
for tone in range(len(tones)-1, -1, -1):
    buzz(tones[tone])