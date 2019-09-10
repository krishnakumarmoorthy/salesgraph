import pandas as pd
import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
a = pd.read_csv("sales.csv")
b = pd.DataFrame(a)
c = sorted(set(b.year))
d = a.year.tolist()
e = a.sales.tolist()
f = a.month.tolist()
g = e.index(max(e))
fil = open("code/output.txt","w")
y = str(d[g])
fil.write(y)
fil.close()
grouped = b.groupby('year')
'''for year,month,sale in grouped:
        print(year,month,sale)'''
fig , axes = plt.subplots(nrows=6,ncols=2)
i=0
j=0
print(grouped)
for value in c:
        val = grouped.get_group(value)
        axes[i][j].plot(val.month,val.sales)
        axes[i][j].set_title(value)
        print(i,j,value)
        if i>=5:
              i=0
              j=1
        else:
              i+=1
plt.tight_layout()
plt.show()
plt.savefig("sales.png")
