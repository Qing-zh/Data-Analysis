# -*- coding: utf-8 -*-
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as tls
import matplotlib.pyplot as plt
import plotly.io as pio
import plotly
pio.renderers
file_path=''
data=pd.read_csv(file_path)
data.head()


'''描述性统计分析'''
prevalence_stats=data['2.1.1 Prevalence of undernourishment'].dexcribe()
print(prevalence_stats)

#创建直方图和箱线图
fig = tls.make_subplots(rows=1, cols=2, subplot_titles=('Distribution of Prevalence of Undernourishment', 'Boxplot of Prevalence of Undernourishment'))
# 直方图
fig.add_trace(go.Histogram(x=data['2.1.1 Prevalence of undernourishment'], marker_color='blue', opacity=0.7), row=1, col=1)
fig.update_xaxes(title_text='Prevalence (%)', row=1, col=1)
fig.update_yaxes(title_text='Frequency', row=1, col=1)
# 箱线图
fig.add_trace(go.Box(x=data['2.1.1 Prevalence of undernourishment'], marker_color='blue', boxmean=True), row=1, col=2)
fig.update_xaxes(title_text='Prevalence (%)', row=1, col=2)
# 调整布局并显示图表
fig.update_layout(title_text='Distribution and Boxplot of Prevalence of Undernourishment', height=600, width=1000)
fig.show()


'''流行率分析'''
highest_prevalence = data.nlargest(5, '2.1.1 Prevalence of undernourishment')
lowest_prevalence = data.nsmallest(5, '2.1.1 Prevalence of undernourishment')
# 准备数据
highest_prevalence_data = highest_prevalence[['Entity', '2.1.1 Prevalence of undernourishment']].drop_duplicates()
lowest_prevalence_data = lowest_prevalence[['Entity', '2.1.1 Prevalence of undernourishment']].drop_duplicates()

# 创建子图
fig = go.Figure()
# 添加最高患病率图
fig.add_trace(go.Bar(x=highest_prevalence_data['Entity'], y=highest_prevalence_data['2.1.1 Prevalence of undernourishment'], marker_color='red', name='Regions with Highest Prevalence'))
# 添加最低患病率图
fig.add_trace(go.Bar(x=lowest_prevalence_data['Entity'], y=lowest_prevalence_data['2.1.1 Prevalence of undernourishment'], marker_color='green', name='Regions with Lowest Prevalence'))

# 更新布局
fig.update_layout(title='Regions with Highest and Lowest Prevalence of Undernourishment',
                  xaxis_title='Region',
                  yaxis_title='Prevalence of Undernourishment (%)',
                  barmode='group')
# 显示图表
fig.show()

'''全球营养不良流行率随时间的变化趋势'''
recent_year=data['Year'].max()
recent_data=data[data['Year']==recent_year]
print(recent_year)
recent_data=pd.read_excel('D:/resource/数据分析/全球营养不良流行率趋势与地区差异分析/最新一年（2022年）各个地区的营养不良流行率.xlsx')

global_data = data[data['Entity'] == 'World']
fig = px.line(global_data, x='Year', y='2.1.1 Prevalence of undernourishment', title='Global Undernourishment Over Time')
fig.update_traces(line_color='red')
fig.update_layout(xaxis_title='Year', yaxis_title='Prevalence of Undernourishment (%)')
fig.update_layout(plot_bgcolor='black', paper_bgcolor='black', font_color='red')
fig.update_xaxes(showgrid=True, gridwidth=0.5, gridcolor='gray')
fig.update_yaxes(showgrid=True, gridwidth=0.5, gridcolor='gray')
fig.show()


'''最新一年（2017年）各个地区的营养不良流行率'''
# 创建条形图
fig = go.Figure(data=go.Bar(x=recent_data['Entity'], y=recent_data['2.1.1 Prevalence of undernourishment'], marker_color='red'))
# 更新布局
fig.update_layout(title='Regional Undernourishment Comparison (Most Recent Year)',
                  xaxis_title='Region',
                  yaxis_title='Prevalence of Undernourishment (%)',
                  xaxis_tickangle=-45,
                  plot_bgcolor='black',
                  paper_bgcolor='black',
                  font=dict(color='red'),
                  yaxis=dict(gridcolor='gray', gridwidth=0.5),
                  showlegend=False)
# 显示图表
fig.show()

#绘图1
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
bars=plt.bar(recent_data['Entity'],recent_data['2.1.1 Prevalence of undernourishment'],color='red')
# 添加标题和标签
ax.set_xlabel('Region', color='red')
ax.set_ylabel('Prevalence of Undernourishment(%)', color='red')
# 设置横坐标和列坐标的刻度标签
ax.set_xticklabels(recent_data['Entity'], rotation=45, ha="right", color='red')
ax.set_yticklabels(ax.get_yticks(), color='red')
plt.title('Regional Undernourishment Comparison(Most Recent Year) ', color='red')
plt.show()

#绘图2
plt.figure(figsize=(10, 6), facecolor='black')
# 绘制柱状图
bars = plt.bar(recent_data['Entity'],recent_data['2.1.1 Prevalence of undernourishment'], color='red')
# 设置坐标轴的背景颜色
plt.gca().set_facecolor('black')
# 设置x轴和y轴的颜色和刻度标签颜色
plt.xticks(rotation=45,color='red')
plt.yticks(color='red')
# plt.gca().spines['bottom'].set_color('red')
# plt.gca().spines['left'].set_color('red')
# 添加标题和标签
plt.title('Regional Undernourishment Comparison(Most Recent Year) ', color='red')
plt.xlabel('Region', color='red')
plt.ylabel('Prevalence of Undernourishment(%)', color='red')
# 显示图形
plt.show()


'''不同年份的营养不良流行率'''
# 创建散点图
fig = go.Figure(data=go.Scatter(x=data['Year'], y=data['2.1.1 Prevalence of undernourishment'], mode='markers', marker=dict(color='red')))
# 更新布局
fig.update_layout(title='Scatter Plot of Undernourishment vs Year',
                  xaxis_title='Year',
                  yaxis_title='Prevalence of Undernourishment (%)',
                  plot_bgcolor='black',
                  paper_bgcolor='black',
                  font=dict(color='red'),
                  yaxis=dict(gridcolor='gray', gridwidth=0.5),
                  showlegend=False)

# 显示图表
fig.show()

#绘制折线统计图
import warnings
warnings.filterwarnings('ignore')

# 计算移动平均值
data['Moving Average'] = data['2.1.1 Prevalence of undernourishment'].rolling(window=5).mean()

# 创建图表
fig = go.Figure()
# 添加年度数据
fig.add_trace(go.Scatter(x=data['Year'], 
                         y=data['2.1.1 Prevalence of undernourishment'],
                         mode='lines', 
                         name='Annual Data', 
                         line=dict(color='red')))
# 添加5年移动平均值
fig.add_trace(go.Scatter(x=data['Year'], 
                         y=data['Moving Average'],
                         mode='lines', 
                         name='5-Year Moving Average', 
                         line=dict(color='yellow')))
# 更新布局
fig.update_layout(title='Global Undernourishment with Moving Average',
                  xaxis_title='Year',
                  yaxis_title='Prevalence of Undernourishment (%)',
                  plot_bgcolor='black',
                  paper_bgcolor='black',
                  font=dict(color='red'),
                  yaxis=dict(gridcolor='gray', gridwidth=0.5),
                  legend=dict(font=dict(color='red')),
                  showlegend=True)
# 显示图表
fig.show()

recent_data = data[data['Year'] == recent_year]
recent_data = recent_data[recent_data['Entity'] != 'World']  # Exclude global total
# 创建条形图
fig = go.Figure(data=[go.Bar(x=recent_data['Entity'], 
                             y=recent_data['2.1.1 Prevalence of undernourishment'], 
                             marker_color='red')])

# 更新布局
fig.update_layout(title='Undernourished Population by Region (Most Recent Year)',
                  xaxis_title='Region',
                  yaxis_title='Prevalence of Undernourishment (%)',
                  xaxis_tickangle=-45,
                  plot_bgcolor='black',
                  paper_bgcolor='black',
                  font=dict(color='red'),
                  yaxis=dict(gridcolor='gray', gridwidth=0.5),
                  showlegend=False)
fig.show()
# 显示图表
plotly.offline.plot(fig)


'''显示不同地区在不同年份的营养不良流行率'''
heatmap_data = data.pivot_table(index='Entity', columns='Year', values='2.1.1 Prevalence of undernourishment')
fig = go.Figure(data=go.Heatmap(
    z=heatmap_data.values,
    x=heatmap_data.columns,
    y=heatmap_data.index,
    colorscale='Reds',
    colorbar=dict(title='Prevalence (%)')
))

fig.update_layout(
    title='Heatmap of Undernourishment Over Time by Region',
    xaxis_title='Year',
    yaxis_title='Region',
    xaxis=dict(tickangle=90),
    height=800,  # 设定图形高度
    margin=dict(l=100, r=20, t=50, b=100),  # 设置边距
)
fig.update_xaxes(tickmode='linear', dtick=1)  # 设置 x 轴刻度间隔

fig.show()

















