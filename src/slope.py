from collections import namedtuple
from typing import NamedTuple
import co2
import temperature
import math
class slope:
    graphDataItem = namedtuple('graphDataItem',['year','x','y'])
    __graphData = list()
    '''constructor: create a list for the linear regreassion graph with Co2 value as the x value and y is the temperature
    for each year'''
    def __init__(self,co2Obj,tempObj):
        for a in co2Obj.keys():
            for b in tempObj.keys():
                if (a == b):
                    tempGraphData = self.graphDataItem(a,co2Obj[a],tempObj[b])
                    self.__graphData.append(tempGraphData) 

    def getLinearRegressionGraph(self):
        '''find means of all x and y values'''
        sumOfX = 0
        sumOfY = 0
        tempSum = 0
        for item in self.__graphData:
            sumOfX += item.x
            sumOfY += item.y
        meanOfX =  sumOfX/len(self.__graphData)
        meanOfY =  sumOfY/len(self.__graphData)
        '''find standard deviation of x and y'''
        for item in self.__graphData:
            tempSum += ((item.x - meanOfX))**2
        SDofX = math.sqrt(tempSum/(len(self.__graphData)-1))
        
        tempSum = 0
        
        for item in self.__graphData:
            tempSum += ((item.y - meanOfY))**2
        SDofY = math.sqrt(tempSum/(len(self.__graphData)-1))

        tempSum = 0
        '''find correlation value r'''
        for item in self.__graphData:
            tempSum += (item.x - meanOfX)*(item.y - meanOfY)
        
        r = (1/(len(self.__graphData)-1))*(tempSum/(SDofX*SDofY))
        '''get slope using correlation r'''
        slope = r*SDofY/SDofX
        '''get y-intercept'''
        c = self.__graphData[0].y - slope * self.__graphData[0].x
        '''returns slope formula in string'''
        slopeFormula = "y = " + str(slope) + " x + " + str(c)
        return slopeFormula
