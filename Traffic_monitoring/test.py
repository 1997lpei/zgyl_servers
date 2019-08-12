import pandas as pd
import datetime


df = pd.read_excel('/home/liu/Downloads/test.xlsx')
data = df.sample(3).values
for a in data:
    print(a[1])
    b = str(a[1])
    print(b)
    print(type(b))

    # b = datetime.datetime.strptime(str(a[1]),'%H:%M:%S')

    # print(type(b))
