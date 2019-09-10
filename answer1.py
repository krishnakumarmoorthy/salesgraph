import pandas as pd
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt 
#Read the input file
h=pd.read_csv("sales.csv")
d=h.year.tolist()
x=len(d)
e=h.sales.tolist()
f=h.month.tolist()
g=(e.index(max(e)))
fil=open("code/output.txt","w")
y=str(d[g])
fil.write(y)
fil.close()
fig, axis= plt.subplots(nrows=12, ncols=1)
j=0
for i in range(1949,1961):
	axis[j].set_title(i)
	v=[]
	w=[]
	x=0
	for ax in d:
		if ax == i:	
			v.append(f[x])
			w.append(e[x])
		x+=1
	axis[j].plot(v,w)
	j+=1
plt.grid(True)
plt.show()
plt.savefig("code/salesoutput.png")
