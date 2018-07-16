import os, time
gpio_path = "/sys/class/gpio"
"""
sys/class/gpio/export : (Write only)
Writing to this file generates new temporary files that 
allow to modify GPIO pin configurations.
For example, writing 12 allows user to configure the GPIO pin 12.

/sys/class/gpio/gpioXX/direction : (Write and read)
This file indicates whether the GPIO pin XX is an input or an output.
'out' : output
'in' : input

/sys/class/gpio/gpioXX/value : (Write and read)
This file indicates whehter the GPIO pin XX is on or off
1 : on
0 : off

/sys/class/gpio/unexport : (Write only)
Writing to this file deletes the files generated to 
modify GPIO pin configurations.
For example, writing 12 deletes files that configure GPIO pin 12

$GPIO = /sys/class/gpio
"""
	
def gpio_config_out(gpio_pin_num) :
	"""
	Call gpio_export(gpio_pin_num) and gpio_setAsOuput(gpio_pin_num)
	If they all return True, return True.
	Otherwise return False
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if gpio_export(gpio_pin_num) == False :
		return False
	# Wait a bit for the generation of GPIO pin config files.
	time.sleep(0.05)
	if gpio_setAsOuput(gpio_pin_num) == False :
		return False
	return True
	
def gpio_config_in(gpio_pin_num) :
	"""
	Call gpio_export(gpio_pin_num) and gpio_setAsInput(gpio_pin_num)
	If they all return True, return True.
	Otherwise return False
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if gpio_export(gpio_pin_num) == False :
		return False
	# Wait a bit for the generation of GPIO pin config files.
	time.sleep(0.05)
	if gpio_setAsInput(gpio_pin_num) == False :
		return False
	return True
def gpio_export(gpio_pin_num) :
	""" 
	Check the accessibility of export with write permission.
	If true, open the file with write permission.
	Write GPIO pin number to prompt the generation of GPIO pin cofig files.
	Close after writing, then return True.
	Otherwise, return False
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/export", os.W_OK):
		gpio_pin = os.open(gpio_path + "/export", os.O_WRONLY)
		os.write(gpio_pin, str(gpio_pin_num))
		os.close(gpio_pin)
		return True
	return False
		
def gpio_setAsOuput(gpio_pin_num) :
	""" 
	Check the accessibility of $GPIO/gpioXX/direction with write permission
	If true, open the file with write permission.
	Write 'out' to set the GPIO pin as an output.
	Close after writing, then return True.
	Otherwise, return False.
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/direction", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/direction",os.O_WRONLY)
		os.write(gpio_pin, 'out')
		os.close(gpio_pin)
		return True
	return False

def gpio_setAsInput(gpio_pin_num) :
	""" 
	Check the accessibility of $GPIO/gpioXX/direction with write permission
	If true, open the file with write permission.
	Write 'in' to set the GPIO pin as an input.
	Close after writing, then return True.
	Otherwise, return False.
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/direction", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/direction",os.O_WRONLY)
		os.write(gpio_pin, 'in')
		os.close(gpio_pin)
		return True
	return False
		
def gpio_unexport(gpio_pin_num) : 
	"""
	Check the accessibility of $GPIO/unexport with write permission
	If true, open the file with write permission.
	Write GPIO pin number to prompt the deletion of GPIO pin config files.
	Close after writing, then return True.
	Otherwise, return False.
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/unexport", os.W_OK):
		gpio_pin = os.open(gpio_path + "/unexport", os.O_WRONLY)
		os.write(gpio_pin, str(gpio_pin_num))
		os.close(gpio_pin)
		return True
	return False
def read_gpio(gpio_pin_num) :
	"""
	Check the accessibility of $GPIO/gpioXX/value with read permission.
	If true, open the file with read permission.
	return the first byte of the gpio
	Otherwise, return '2'
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/value", os.R_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/value",os.O_RDONLY)
		value = os.read(gpio_pin, 1)
		os.close(gpio_pin)
		return value
	return 2

def gpio_on(gpio_pin_num) :
	"""
	Check the accessibility of $GPIO/gpioXX/value with write permission.
	If true, open the file with write permission.
	Write 1 to turn on the GPIO pin XX
	Close after writing, then return True.
	Otherwise, return False
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/value", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/value",os.O_WRONLY)
		os.write(gpio_pin, '1')
		os.close(gpio_pin)
		return True
	return False

def gpio_off(gpio_pin_num) :
	"""
	Check the accessibility of $GPIO/gpioXX/value with write permission.
	If true, open the file with write permission.
	Write 0 to turn on the GPIO pin XX
	Close after writing, then return True.
	Otherwise, return False
	
	gpio_pin_num (integer type) : Specifies the pin number to configure
	"""
	if os.access(gpio_path + "/gpio" + str(gpio_pin_num) + "/value", os.W_OK) :
		gpio_pin = os.open(gpio_path + "/gpio" + str(gpio_pin_num) + "/value",os.O_WRONLY)
		os.write(gpio_pin, '0')
		os.close(gpio_pin)
		return True
	return False
