# Mall-Customer-Segmentation K-Means

```
# Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go
```

```
# Import data
mall = pd.read_csv('./Mall_Customers.csv')
mall.head()
```


```
fig = plt.figure(figsize = (10,6))
sns.barplot(x = 'Gender', y = 'Annual Income (k$)', data = mall)
```
![image](https://user-images.githubusercontent.com/25868126/121405227-699caa00-c97a-11eb-9092-51eba0134764.png)


```
sns.scatterplot(data =mall,x="Annual Income (k$)",y="Spending Score (1-100)")
```
![image](https://user-images.githubusercontent.com/25868126/121405414-a8cafb00-c97a-11eb-8104-a4a5281387a5.png)


```
plt.figure(1 , figsize = (15 , 7) )
plt.clf()
Z2 = Z2.reshape(xx.shape)
plt.imshow(Z2 , interpolation='nearest', 
           extent=(xx.min(), xx.max(), yy.min(), yy.max()),
           cmap = plt.cm.Pastel2, aspect = 'auto', origin='lower')

plt.scatter( x = 'Annual Income (k$)' ,y = 'Spending Score (1-100)' , data = mall , c = labels2 , 
            s = 200 )
plt.scatter(x = centroids2[: , 0] , y =  centroids2[: , 1] , s = 300 , c = 'red' , alpha = 0.5)
plt.ylabel('Spending Score (1-100)') , plt.xlabel('Annual Income (k$)')
plt.show()
```
![image](https://user-images.githubusercontent.com/25868126/121405606-dd3eb700-c97a-11eb-9344-a8ce44d498fb.png)
