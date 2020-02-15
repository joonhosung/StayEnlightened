import mraa 
print(mraa.getVersion())

light=mraa.Gpio(29)
light.dir(mraa.DIR_IN)


while True:

	light_val=int(light.read())
	print(light_val)




