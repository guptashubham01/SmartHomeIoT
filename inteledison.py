import mraa
import time
import math
from firebase import firebase

B=3975
an = mraa.Aio(2)
wn = mraa.Aio(1)
atn = mraa.Aio(0)
var = 1
firebase = firebase.FirebaseApplication('https://smarthomealert-60878.firebaseio.com/',None)
while var==1:
	w = wn.read()
	a = an.read()
	t = atn.read()
	resistance = (1023-a)*10000.0/a
	temp = 1/(math.log(resistance/10000.0)/B+1/298.15)-273.15
	finaltemp = (temp*0.48828125)+4

	result = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','temperatureValue',finalttemp)

	if t==0
		res = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','open','Open')
	else
		res = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','open','Close')

	voltage = float(w*0.00322)
	if voltage>0.0 and voltage<=0.1:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',0)
	elif voltage>0.1 and voltage<=0.3:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',12)
	elif voltage>0.3 and voltage<=0.8:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',30)
	elif voltage>0.8 and voltage<=1.1:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',55)
	elif voltage>1.1 and voltage<=1.6:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',80)
	elif voltage>1.6 and voltage<=2:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',105)
	elif voltage>2 and voltage<=2.4:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',130)
	elif voltage>2.4 and voltage<=2.8:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',155)
	else:
		wght = firebase.put('TL6TF3Lam1eDN4xUaYgHiBssuAI2','weightValue',180)

	print result
	print res
	print wght