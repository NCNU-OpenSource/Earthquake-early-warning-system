import RPi.GPIO as GPIO
import time

led_pin3 = 7
buzzer_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin3, GPIO.OUT)

pwm_led3 = GPIO.PWM(led_pin3, 500)
pwm_led3.start(100)

def warning():
    clock_timer = 5
    GPIO.setup(buzzer_pin, GPIO.OUT)
    while clock_timer != 0:
        buzzer()
        clock_timer -= 1

def buzzer():
    timer = 20
    while timer != 0:
        number = 0.05
        GPIO.output(buzzer_pin, True)
        pwm_led3.ChangeDutyCycle(100)
        time.sleep(number)
        GPIO.output(buzzer_pin, False)
        pwm_led3.ChangeDutyCycle(0)
        time.sleep(number)
        timer = timer - 1
        time.sleep(0.005)

