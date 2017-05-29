# -*- coding: utf-8 -*-

import sys 	
from PyQt5.QtWidgets import QApplication , QMainWindow
from WeatherWin import Ui_Form
import requests

class MainWindow(QMainWindow ):
	def __init__(self, parent=None):    
		super(MainWindow, self).__init__(parent)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
 		
	def queryWeather(self):
		print('* queryWeather  ')
		city = self.ui.weatherComboBox.currentText()
		print(city )
		rep = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
		rep.encoding = 'utf-8'
		print( rep.json() ) 
		
		msg1 = '城市: %s' % rep.json()['weatherinfo']['city'] + '\n'
		msg2 = '风向: %s' % rep.json()['weatherinfo']['WD'] + '\n'
		msg3 = '温度: %s' % rep.json()['weatherinfo']['temp'] + ' 度' + '\n'
		msg4 = '风力: %s' % rep.json()['weatherinfo']['WS'] + '\n'
		msg5 = '湿度: %s' % rep.json()['weatherinfo']['SD'] + '\n'
		result = msg1 + msg2 + msg3 + msg4 + msg5
		self.ui.resultText.setText(result)
		
		
	def clearResult(self):
		print('* clearResult  ')
		self.ui.resultText.clear()	
		
if __name__=="__main__":  
	app = QApplication(sys.argv)  
	win = MainWindow()  
	win.show()  
	sys.exit(app.exec_())  