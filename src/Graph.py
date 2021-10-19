import matplotlib.pyplot as plt
import numpy as np

from slope import slope
class Graph:
    def xyPlot(self,xpoints,ypoints):
        plt.plot(xpoints,ypoints)
        plt.show()

    def barChart(self,xpoints,ypoints):
        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        ax.bar(xpoints,ypoints)
        fig.show()

    def linearRegression(self,slopeObj):
        x=list()
        y=list()
        for item in slopeObj.getGraphData():
            x.append(item[1])
            y.append(item[2])
        x = np.array(x)
        y = np.array(y)
        plt.plot(x, y, 'o')
        m, b = np.polyfit(x, y, 1)
        plt.plot(x, m*x + b)
        plt.show()
