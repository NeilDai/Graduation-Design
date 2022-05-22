import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'

du = pd.read_csv('test1.csv')
x = du['PrincipalComponent'].values
a = du['P1'].values
b = du['P2'].values
c = du['P3'].values
d = du['P4'].values
plt.figure(figsize=(16,5))
plt.subplot(1, 1, 1)

plt.bar(x, a, label = '第一次训练',alpha = 0.3,width=0.7,facecolor='red',edgecolor='red')

plt.bar(x, b, label = '第二次训练',alpha = 0.3,width=0.7,facecolor="blue",edgecolor='blue')

plt.bar(x, c,label = '第三次训练',alpha = 0.3,width=0.7,facecolor="yellow",edgecolor='yellow')

plt.bar(x, d,label = '第四次训练',alpha = 0.3,width=0.7,facecolor="green",edgecolor='green')

plt.title('RandomForest Feature Proportion')
plt.tick_params(labelsize=8)
plt.legend()

plt.show()