import kivy
kivy.require('1.9.0')
from math import floor
from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Label

class Floater(FloatLayout):

	def calculate(self, calculation):
		
		if calculation:
			try:
				numWeight = calculation
				w = int(calculation) - 45
				#Math Calculation for the weights - Barbells are 45lbs
				#Counts 45, 35, 25, 10, 5, and 2.5lbs plates
				fullWeight = 5 * round(int(w+45)/5)
				a = floor(w/90.0)
				b = floor((w-(90.0*a))/70.0)
				c = floor((w-(90.0*a)-(70.0*b))/50.0)
				d = floor((w-(90.0*a)-(70.0*b)-(50.0*c))/20.0)
				e = floor((w-(90.0*a)-(70.0*b)-(50.0*c)-(20.0*d))/10.0)
				f = floor((w-(90.0*a)-(70.0*b)-(50.0*c)-(20.0*d)-(10.0*e))/5.0)

				if w <= 0:
					self.ids.output.text = 'Use fixed weights'
				else:
					self.ids.output.text = 'Plates Per \nSide:'
					self.ids.total.text = "Total Weight: {}".format(int(fullWeight))
					self.ids.pps.text = "45's:   {}\n35's:   {}\n25's:   {}\n10's:   {}\n5's:   {}\n2.5's:   {}".format(a,b,c,d,e,f)
			except Exception:
				self.ids.output.text = "Error"
	
	def delete(self, weight):
		newWeight = weight[:-1]
		self.ids.entry.text = newWeight

	def panda(self, weight):
		pandaSplit = weight.split(':')
		if "Total Weight" in pandaSplit[0]:
			try:
				justInt = weight.split(':')
				intWeight = int(justInt[-1])
				#The average weight of a female panda is 220 lbs.
				pandaWeight = round(intWeight/ 220.0, 2)
				self.ids.total.text = 'Pandas: {}'.format(pandaWeight)
			except Exception:
				self.ids.total.text = 'Error'
		elif "Bellas" in pandaSplit[0]:
			try:
				justInt = pandaSplit[1]
				intWeight = float(justInt) * 4.7
				bellaWeight = round(intWeight/ 220, 2)
				self.ids.total.text = 'Pandas: {}'.format(bellaWeight)
			except Exception:
				self.ids.total.text = 'Error (Code 3)'

	def bella(self, weight):
		bellaSplit = weight.split(':')
		if 'Total Weight' in bellaSplit[0]:
			try:
				justInt = weight.split(':')
				#the conversion. This could be cleaned up to look like below
				intWeight = int(justInt[-1])
				#The weight of my girlfriend's dog, Bella, is 4.7 lbs
				bellaWeight = round(intWeight/ 4.7, 2)
				self.ids.total.text = 'Bellas: {}'.format(bellaWeight)
			except Exception:
				self.ids.total.text = 'Error (Code 1)'
		elif 'Pandas' in bellaSplit[0]:
			try:
				justInt = bellaSplit[1]
				intWeight = float(justInt) * 220
				bellaWeight = round(intWeight/ 4.7, 2)
				self.ids.total.text = 'Bellas: {}'.format(bellaWeight)
			except Exception:
				self.ids.total.text = 'Error (Code 2)'

class WeightsApp(App):
	def build(self):
		return Floater()

calcApp = WeightsApp()

if __name__ == "__main__":
	calcApp.run()