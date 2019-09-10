import pandas as pd
import numpy as np
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('seaborn')
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
d = {"January":'01',"February":"02","March":"03","April":'04',"May":'05',"June":'06',"July":'07','August':'08',"September":'09',"October":'10',"November":'11',"December":'12'}
print(d)
b.month.replace(d,inplace=True)
grouped = b.groupby('year')
fig , axes = plt.subplots(nrows=6,ncols=2,figsize = (17,15))
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
