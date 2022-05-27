import math
import xbox
import RPi.GPIO as GPIO
 
GPIO_SPEAKER = 21
GPIO_LED_R   = 26
GPIO_LED_B   = 17
 
 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
GPIO.setup(GPIO_SPEAKER, GPIO.OUT)
GPIO.setup(GPIO_LED_R, GPIO.OUT)
GPIO.setup(GPIO_LED_B, GPIO.OUT)

 
if __name__ == '__main__':
    gamepad = xbox.Joystick()   
    
    while not gamepad.Back():        

        #fake shoot(red light and sound)    
        speaker_state    = GPIO.LOW if gamepad.rightTrigger() else GPIO.HIGH        
        led_state_red    = GPIO.HIGH if gamepad.rightTrigger() else GPIO.LOW   
        
        led_state_blue   = GPIO.HIGH if gamepad.X() else GPIO.LOW
            
        GPIO.output(GPIO_SPEAKER, speaker_state)
        GPIO.output(GPIO_LED_R, led_state_red)       
        GPIO.output(GPIO_LED_B, led_state_blue)
        
           
    gamepad.close()
