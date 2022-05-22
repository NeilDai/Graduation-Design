import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
from Igem_Sub_Seq2Array import Seq2Array

df = pd.read_excel('Data01.xls')
con = df['Total consensus PRE'].values
_con = df['Number of +consensus PRE'].values
con_ = df['Number of -consensus PRE'].values
X = df['Promoter sequence'].values

x = []
con_base = []
_con_base = []
con__base = []

# 选取127个含有consensus PRE的启动子
for i,o in enumerate(X):
    for n,m in enumerate(con):
        if i == n:
            if m != 0:
                x.append(o)
                con_base.append(m)

# 碱基位置表示算法
x_base = []
x_temp = []
for k in x:
    a_total = k.count('a')
    c_total = k.count('c')
    g_total = k.count('g')
    t_total = k.count('t')
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    for l in k:
        if l == 'a':
            a_count = a_count + 1
            a_temp = a_count / a_total
            x_temp.append(a_temp)
        elif l == 'c':
            c_count = c_count + 1
            c_temp = c_count / c_total
            x_temp.append(c_temp)
        elif l == 'g':
            g_count = g_count + 1
            g_temp = g_count / g_total
            x_temp.append(g_temp)
        elif l == 't':
            t_count = t_count + 1
            t_temp = t_count / t_total
            x_temp.append(t_temp)
    if x_temp != []:
        x_base.append(x_temp)
        x_temp = []

# 仅独热编码的数据x_4
x_4 = Seq2Array(x)
# print(x_4)

x_d_base = DataFrame(x_base)
x_df_base = np.expand_dims(x_d_base,axis=2)

# 独热编码与碱基位置表示的5维数据x_data
x_data = np.concatenate((x_4, x_df_base), axis=2)
# print(np.shape(x_data))

# 单一维度自己增维到5维：total consensus PRE
c = DataFrame(con_base)
c_1 = np.expand_dims(c,axis=2)
c_name = []
for v in range(1,6):
    c_name.append('c_' + str(v))
for p in range(1,len(c_name)):
    cmd = '%s=np.concatenate((l,c_1),axis=2)' % c_name[p]
    cmd_1 = cmd.replace('l',c_name[p-1])
    exec(cmd_1)
# print(c_5[0])

x_df_data = np.concatenate((c_5, x_data), axis=1)
# print(x_df_data)


# 选取127个含有+consensus PRE的启动子
for l,o in enumerate(_con):
    for q,p in enumerate(con_):
        if l == q:
            if o != 0 or p != 0:
                _con_base.append(o)
                con__base.append(p)

# print(np.shape(_con_base))
# print(np.shape(con__base))

# 单一维度自己增维到5维： +consensus PRE
b = DataFrame(_con_base)
b_1 = np.expand_dims(b,axis=2)
b_name = []
for v in range(1,6):
    b_name.append('b_' + str(v))
for p in range(1,len(b_name)):
    cmd = '%s=np.concatenate((l,b_1),axis=2)' % b_name[p]
    cmd_1 = cmd.replace('l',b_name[p-1])
    exec(cmd_1)
# print(np.shape(c_5))

# 包含+consensus和total的复合数据（含nan）
x_df_data_b = np.concatenate((b_5, x_df_data), axis=1)
# print(np.shape(x_df_data_b))

# 单一维度自己增维到5维： -consensus PRE
a = DataFrame(con__base)
a_1 = np.expand_dims(a,axis=2)
a_name = []
for v in range(1,6):
    a_name.append('a_' + str(v))
for p in range(1,len(a_name)):
    cmd = '%s=np.concatenate((l,a_1),axis=2)' % a_name[p]
    cmd_1 = cmd.replace('l',a_name[p-1])
    exec(cmd_1)
# print(np.shape(c_5))

# 包含nan值，独热，碱基位置编码，consensusPRE信息的数据集
x_dt = np.concatenate((a_5, x_df_data_b), axis=1)

# 最终综合独热，碱基位置编码，consensusPRE信息的去除nan的数据集
x_dt_fin = np.nan_to_num(x_dt)
# print(x_dt_fin[0][3])

# 加卷积壳，由于数据后方0过多所以只在前面加一个卷积核的卷积壳
z = np.zeros((127,30,5))
x_z = np.concatenate((z, x_dt_fin), axis=1)
print(np.shape(x_z))
