import mraa
import time
import math
from firebase import firebase

B=3975
temperatureSensor = mraa.Aio(2)
weightSensor = mraa.Aio(1)
touchSensor = mraa.Aio(0)
var = 1
firebase = firebase.FirebaseApplication('https://smarthomealert-60878.firebaseio.com/',None)
while var==1:
	tempData = temperatureSensor.read()
	weightData = weightSensor.read()
	touchData = touchSensor.read()
	resistance = (1023-tempData)*10000.0/tempData
	temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15
	tempValue = (temp*0.48828125)+4

	temperature = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','temperatureValue',tempValue)

	if touchSensor==0
		door = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','open','Open')
	else
		door = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','open','Close')

	voltage = float(weightSensor*0.00322)
	if voltage>0.0 and voltage<=0.1:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',0)
	elif voltage>0.1 and voltage<=0.3:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',12)
	elif voltage>0.3 and voltage<=0.8:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',30)
	elif voltage>0.8 and voltage<=1.1:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',55)
	elif voltage>1.1 and voltage<=1.6:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',80)
	elif voltage>1.6 and voltage<=2:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',105)
	elif voltage>2 and voltage<=2.4:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',130)
	elif voltage>2.4 and voltage<=2.8:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',155)
	else:
		weight = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',180)

	print temperature
	print door
	print weight
