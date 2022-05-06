import pandas_datareader as pdr
import numpy as np

filecoin = pdr.DataReader(("NBX.OL"),
                       start='2022-1-1', 
                       end='2022-5-1', 
                       data_source='yahoo')['Close']
x = list()
for i in filecoin:
    x.append(i)
x = np.array(x)

dltx = pdr.DataReader(("DLTX.OL"),
                    start='2022-1-1',
                    end='2022-5-1',
                    data_source='yahoo')['Close']

y = list()
for i in dltx:
    y.append(i)

y = np.array(y)


r = np.corrcoef(x, y)
