import myParser
import temperature
import DataBase
rawParsedTemp = myParser.myParser("Temperature.html")
tempObj = temperature.temperature(rawParsedTemp.getRawData())

dataBaseObj = DataBase.DataBase(tempObj.getTempData())