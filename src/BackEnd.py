import Graph
import DataBase
import numpy as np
import myParser
import temperature
import co2
import slope
def xyPlot():
    xyPlotObj = Graph.Graph()
    dataBaseObj=DataBase.DataBase()
    xyPlotObj.xyPlot(np.array(dataBaseObj.fetchYear()),np.array(dataBaseObj.fetchMedian()))
def barChart():
    barChartObj = Graph.Graph()
    dataBaseObj=DataBase.DataBase()
    barChartObj.barChart(np.array(dataBaseObj.fetchYear()),np.array(dataBaseObj.fetchMedian()))
def linearRegression():
    linearRegressionObj = Graph.Graph()
    #parse raw data from html file
    rawParsedCo2 = myParser.myParser("Co2.html")
    rawParsedTemp = myParser.myParser("Temperature.html")

    #create containers to store processed raw data for temperature and Co2 file
    tempObj = temperature.temperature(rawParsedTemp.getRawData())
    co2Obj = co2.co2(rawParsedCo2.getRawData())

    slopeObj = slope.slope(co2Obj.getCo2Dict(),tempObj.getTempDict())
    linearRegressionObj.linearRegression(slopeObj)
