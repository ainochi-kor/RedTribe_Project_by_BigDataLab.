#!/usr/bin/env python3
#아질산질소 그래프 시각화, 표 합치기
import pandas as pd
import matplotlib.pyplot as plt

#해역별 csv파일 불러오기
df1 = pd.read_csv('output02-1.csv', index_col = None, encoding='cp949')
df2 = pd.read_csv('output02-2.csv', index_col = None, encoding='cp949')
df3 = pd.read_csv('output02-3.csv', index_col = None, encoding='cp949')
df4 = pd.read_csv('output02-4.csv', index_col = None, encoding='cp949')

#데이터 입력
date = df1['Date']
data1 = df1['Nitrous Acid Nitrogen_avg'].astype('float')
data2 = df2['Nitrous Acid Nitrogen_avg'].astype('float')
data3 = df3['Nitrous Acid Nitrogen_avg'].astype('float')
data4 = df4['Nitrous Acid Nitrogen_avg'].astype('float')

#선 그래프
plt.figure(figsize=(20,8))
plt.plot(date, data1, 'g', label='East')
plt.plot(date, data2, 'r', label='South')
plt.plot(date, data3, 'b', label='West')
plt.plot(date, data4, 'y', label='East China')
#plt.grid()
plt.legend()
plt.xlabel('Month')
plt.ylabel('Nitrous Acid Nitrogen_avg')
plt.title('Sea area Nitrous Acid Nitrogen_avg')
plt.show()

#막대 그래프
plt.style.use('ggplot')
fig = plt.figure(figsize=(20,8))
ax1 = fig.add_subplot(1,1,1)
ax1.bar(date, data1, align='center', color='g', label='East')
ax1.bar(date, data2, align='center', color='r', label='South')
ax1.bar(date, data3, align='center', color='b', label='West')
ax1.bar(date, data4, align='center', color='y', label='East China')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Nitrous Acid Nitrogen_avg')
plt.title('Sea area Nitrous Acid Nitrogen_avg')
plt.show()

#점 그래프
plt.figure(figsize=(20,8))
plt.scatter(date, data1, s=50, color='g', label='East')
plt.scatter(date, data2, s=50, color='r', label='South')
plt.scatter(date, data3, s=50, color='b', label='West')
plt.scatter(date, data4, s=50, color='y', label='East China')
plt.legend()
plt.xlabel('Month')
plt.ylabel('Nitrous Acid Nitrogen_avg')
plt.title('Sea area Nitrous Acid Nitrogen_avg')
plt.show()

#상자그림 그래프 (전체 해역 기준)
data_frame = pd.read_csv('output01.csv', index_col = None, encoding='cp949')
plt.figure(figsize=(20,8))
plt.boxplot((data_frame.loc[data_frame['Observation Date']==1, 'Nitrous Acid Nitrogen'].dropna(), 
             data_frame.loc[data_frame['Observation Date']==2, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==3, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==4, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==5, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==6, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==7, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==8, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==9, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==10, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==11, 'Nitrous Acid Nitrogen'].dropna(),
             data_frame.loc[data_frame['Observation Date']==12, 'Nitrous Acid Nitrogen'].dropna()))
plt.xlabel('Month')
plt.ylabel('Nitrous Acid Nitrogen')
plt.title('Sea area Nitrous Acid Nitrogen')
plt.show()

#표 합치기
df = pd.concat([df1, df2, df3, df4])

#출력
df.to_csv('output03.csv', index= None, encoding='cp949')
