# Import the required 'libraries' for pin definitions and PWM
from machine import Pin, PWM

# Also import a subset for sleep and millisecond sleep. If you just import
# the utime you will have to prefix each call with "utime."
from utime import sleep, sleep_ms

# Define what the buzzer object is - a PWM output on pin 15
buzzer = PWM(Pin(15))

# A list of frequencies
tones = (200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000, 1100, 1200, 1400, 1500)

# Define the function to play a single tone then stop
def buzz(freq):
    # Set the frequence
    buzzer.freq(freq)
    # Set the duty cycle (affects volume)
    buzzer.duty_u16(15000);
    # Let the sound continue for X milliseconds
    sleep_ms(30);
    # Now switch the sound off
    buzzer.duty_u16(0);
    # And delay a small amount (gap between tones)
    sleep_ms(20);

# Define a similar functionm with no delay between tones
def buzz2(freq):
    buzzer.freq(freq)
    buzzer.duty_u16(15000);
    
# Now sound the tones, one after the other
for tone in range(len(tones)):
    buzz(tones[tone])

# Small gap in SECONDS after the ascending tones
sleep(1)

# Don't do this, it puts the device to Seep Sleep but it reboots on wakeup just
# like the ESP8266
#machine.deepsleep(1)
    
# Now sound the tones IN REVERSE ORDER ie descending
for tone in range(len(tones) -1, -1, -1):
    buzz(tones[tone])

# Another delay
sleep(1)

# Now sound ALL the frequencies from X to Y
for tone in range(500, 2500):
    buzz2(tone)
    sleep_ms(5)
    buzzer.duty_u16(0);

# And repeat in reverse order
for tone in range(2500, 500, -1):
    buzz2(tone)
    sleep_ms(4)
    buzzer.duty_u16(0);   