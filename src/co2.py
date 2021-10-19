import myParser
from collections import namedtuple
class co2:
    co2DataOfYear = namedtuple('co2DataOfYear',['year','month','deciaml','average','interpolated','trend','days'])
    __listOfCo2Data = list()
    __Co2Dict = dict()
    '''constructor: creates list of Co2 data with namedTuples and a dictionary for Co2 with year as key \
    and median as value '''
    def __init__(self,tempRawData):
        for s in tempRawData:
            tempNamedTupleOfCo2Data = self.co2DataOfYear(s[0],s[1],s[2],s[3],s[4],s[5],s[6])
            self.__listOfCo2Data.append(tempNamedTupleOfCo2Data)
        tempSumOfAverage = 0
        counter = 0
        for listOfData in self.__listOfCo2Data:
            if counter == 0:
                tempYear = int(listOfData[0])
            tempSumOfAverage += listOfData[3]
            counter += 1
            if counter == 12:
                yearAverage = tempSumOfAverage/12
                self.__Co2Dict[tempYear] = yearAverage 
                tempYear = 0
                tempSumOfAverage = 0
                counter = 0
            if int(tempYear) == 2019 and counter==11:
                yearAverage = tempSumOfAverage/11
                self.__Co2Dict[tempYear] = yearAverage 
    '''getter for dictionary for Co2 data'''
    def getCo2Dict(self):
        return self.__Co2Dict

