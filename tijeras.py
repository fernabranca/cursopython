#!usr/bin/env python
# -*-coding:utf-8-*-

import time
from time import sleep
import random

sus="-" * 35
depo=["piedra","papel","tijera"]
while True:
	x=input("Que elijes?: ")
	if x not in depo:
		print("no hagas trampa")
		continue
	pc=random.choice(depo)
	sleep(0.5)
	print(("Compu eligió {}.").format(pc))	
	if x==pc:
		print ("\nEmpate")
	elif x=="piedra" and pc=="tijera":
		print ("\nGanaste")
	elif x=="papel" and pc=="piedra":
		print ("\nGanaste")
	elif x=="tijera" and pc=="papel":
		print ("\nGanaste")
	else:
		print (("Perdimos. {} gana {} \n").format(pc,x))
		print (sus)
