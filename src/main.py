import myParser
import temperature
import co2
import slope
'''parse raw data from html file'''
rawParsedCo2 = myParser.myParser("Co2.html")
rawParsedTemp = myParser.myParser("Temperature.html")

'''create containers to store processed raw data for temperature and Co2 file'''
tempObj = temperature.temperature(rawParsedTemp.getRawData())
co2Obj = co2.co2(rawParsedCo2.getRawData())

'''create slope object and output linear regression line'''
slopeObj = slope.slope(co2Obj.getCo2Dict(),tempObj.getTempDict())
print(slopeObj.getLinearRegressionGraph())