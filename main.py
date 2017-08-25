from lcd import *
lcd_init()	

lcd_cmd(0x01)
time.sleep(1)
lcd_string(0x80," Akshay's ",16)
lcd_string(0xC0,"  RASPBERRY PI  ",16)

while True:

	lcd_string(0x80," Akshay's  ",16)
	lcd_string(0xC0,"  RASPBERRY PI  ",16)
		

GPIO.cleanup()	
