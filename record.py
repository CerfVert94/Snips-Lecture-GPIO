import os, time, OPiGPIO

#https://www.programcreek.com/python/example/4451/os.O_APPEND
def touch(fname, mode=0o600):
	flags = os.O_CREAT | os.O_APPEND
	with os.fdopen(os.open(fname, flags, mode)) as f:
		try:
                	os.utime(fname, None)
	        finally:
        	        f.close()

fd = None
path = "./journal"
if not os.path.exists(path):
        touch(path)
else :
	fd = os.open(path, os.O_WRONLY | os.O_APPEND) 
	if fd == None :
		quit()

if not OPiGPIO.gpio_export(12):
	print "export failed\r\n"
	os.close(fd)
	quit()
time.sleep(0.05)
if not OPiGPIO.gpio_setAsOuput(12):
	print "output failed\r\n"
        os.close(fd)
        quit()

OPiGPIO.gpio_on(12)
time.sleep(0.0008)
OPiGPIO.gpio_off(12)

if not OPiGPIO.gpio_setAsInput(12):
	print "input failed\r\n"
        os.close(fd)
        quit()

gpio = OPiGPIO.read_gpio(12)
ret = 0

for x in range(10000000):
	time.sleep(0.0001)
	ret += os.write(fd, str(gpio)+" ")

ret /= 2
print ret
os.close(fd)
OPiGPIO.gpio_unexport(12)




