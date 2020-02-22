```python
import pandas as pd
pd.set_option('display.precision', 2)
pd.set_option('display.float_format', '{:,.2f}'.format)


def highlight_max(s):
    '''
    highlight the maximum in a Series yellow.
    '''
    is_max = s == s.max()
    return ['background-color: yellow' if v else '' for v in is_max]

data_file = "http://dataframe.oss-cn-beijing.aliyuncs.com/banks.xlsx"
dfs = pd.read_excel(data_file, sheet_name=None, na_values='———', index_col=0)
# df = pd.concat(dfs, names=['机构', '指标'])
df = pd.concat(dfs)
df.columns = [pd.Period(d) for d in df.columns] # pd.to_datetime(df.columns, format='%Y%m%d')
# df.columns.name = '期数'
# df.set_index(['指标', '机构'])
# df.set_index(['指标', '期数'], inplace=True)
df.xs('净利差', level=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>2012-12-31</th>
      <th>2013-03-31</th>
      <th>2013-06-30</th>
      <th>2013-09-30</th>
      <th>2013-12-31</th>
      <th>2014-03-31</th>
      <th>2014-06-30</th>
      <th>2014-09-30</th>
      <th>2014-12-31</th>
      <th>2015-03-31</th>
      <th>...</th>
      <th>2015-12-31</th>
      <th>2016-03-31</th>
      <th>2016-06-30</th>
      <th>2016-09-30</th>
      <th>2016-12-31</th>
      <th>2017-03-31</th>
      <th>2017-06-30</th>
      <th>2017-09-30</th>
      <th>2017-12-31</th>
      <th>2018-12-31</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>招商银行</th>
      <td>2.87</td>
      <td>2.78</td>
      <td>2.78</td>
      <td>2.66</td>
      <td>2.65</td>
      <td>2.44</td>
      <td>2.48</td>
      <td>2.30</td>
      <td>2.45</td>
      <td>2.72</td>
      <td>...</td>
      <td>2.59</td>
      <td>2.49</td>
      <td>2.45</td>
      <td>2.43</td>
      <td>2.37</td>
      <td>2.30</td>
      <td>2.31</td>
      <td>nan</td>
      <td>2.29</td>
      <td>2.44</td>
    </tr>
    <tr>
      <th>兴业银行</th>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>...</td>
      <td>2.26</td>
      <td>nan</td>
      <td>2.03</td>
      <td>nan</td>
      <td>2.00</td>
      <td>nan</td>
      <td>1.48</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>平安银行</th>
      <td>2.19</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>2.14</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>2.39</td>
      <td>nan</td>
      <td>...</td>
      <td>2.62</td>
      <td>nan</td>
      <td>2.66</td>
      <td>nan</td>
      <td>2.60</td>
      <td>2.37</td>
      <td>2.29</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>民生银行</th>
      <td>2.75</td>
      <td>nan</td>
      <td>2.24</td>
      <td>nan</td>
      <td>2.30</td>
      <td>nan</td>
      <td>2.42</td>
      <td>nan</td>
      <td>2.41</td>
      <td>nan</td>
      <td>...</td>
      <td>2.10</td>
      <td>nan</td>
      <td>1.88</td>
      <td>nan</td>
      <td>1.74</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>中信银行</th>
      <td>2.61</td>
      <td>nan</td>
      <td>2.39</td>
      <td>nan</td>
      <td>2.40</td>
      <td>nan</td>
      <td>2.14</td>
      <td>nan</td>
      <td>2.19</td>
      <td>nan</td>
      <td>...</td>
      <td>2.13</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>1.89</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>宁波银行</th>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>2.50</td>
      <td>nan</td>
      <td>...</td>
      <td>2.40</td>
      <td>nan</td>
      <td>2.05</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
    <tr>
      <th>农业银行</th>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>...</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
      <td>nan</td>
    </tr>
  </tbody>
</table>
<p>7 rows × 22 columns</p>
</div>




```python
ndf = df['20171231'].unstack()

```


```python
# # 存贷差
# ndf['存贷差'] = ndf['贷款利率'] - ndf['存款利率']

# # 资产
# ndf['贷款占比'] = ndf['贷款平均余额'] / ndf['生息资产余额']
# ndf['公司贷款占比'] = ndf['公司贷款'] / ndf['生息资产余额']
# ndf['零售贷款占比'] = ndf['零售贷款'] / ndf['生息资产余额']
# ndf['票据贴现占比'] = ndf['票据贴现'] / ndf['生息资产余额']

# ndf['投资占比'] = ndf['投资平均余额'] / ndf['生息资产余额']
# ndf['存放央行占比'] = ndf['存放央行平均余额'] / ndf['生息资产余额']
# ndf['同业资产占比'] = ndf['存拆放同业平均余额'] / ndf['生息资产余额']

# # 负债
# ndf['存款占比'] = ndf['存款平均余额'] / ndf['计息负债余额']
# ndf['公司存款占比'] = ndf['公司存款'] / ndf['计息负债余额']
# ndf['公司活期占比'] = ndf['公司活期'] / ndf['计息负债余额']
# ndf['公司定期占比'] = ndf['公司定期'] / ndf['计息负债余额']

# ndf['零售存款占比'] = ndf['零售存款'] / ndf['计息负债余额']
# ndf['零售活期占比'] = ndf['零售活期'] / ndf['计息负债余额']
# ndf['零售定期占比'] = ndf['零售定期'] / ndf['计息负债余额']

# ndf['活期存款占比'] = (ndf['公司活期'] + ndf['零售活期']) / ndf['计息负债余额']

# ndf['发行债券占比'] = ndf['发行债券平均余额'] / ndf['计息负债余额']
# ndf['向央行借款占比'] = ndf['向央行借款平均余额'] / ndf['计息负债余额']
# ndf['同业负债占比'] = ndf['同业存拆放平均余额'] / ndf['计息负债余额']

# ndf[['贷款占比', '公司贷款占比', '零售贷款占比', '票据贴现占比', '投资占比', '存放央行占比', '同业资产占比']].style.apply(highlight_max).format("{:.2%}")
```


```python
# cols = ['贷款占比', '贷款利率', '投资占比', '投资收息率', '存放央行占比', '存放央行收息率', '同业资产占比', '存拆放同业收息率']
# cols1 = [s for s in cols if s.endswith('占比')]
# ndf[cols].style.format("{:.2%}", subset=cols1).highlight_max().highlight_min(color='green')
```


```python
# ndf[['存款占比', '公司存款占比', '公司活期占比', '零售存款占比', '零售活期占比', '活期存款占比', '发行债券占比', '向央行借款占比', '同业负债占比']].style.apply(highlight_max).format("{:.2%}")
```


```python
# ndf[['贷款利率', '公司贷款利率', '零售贷款利率', '存款利率', '公司活期利率', '公司定期利率', '零售活期利率', '零售定期利率', '存贷差', '净利差', '净息差']].style.apply(highlight_max).format("{:.2f}")
```


```python
# df.xs('贷款利率', level=1)
```


```python
# df.xs('存款利率', level=1)
```


```python
# df.xs('贷款利率', level=1) - df.xs('存款利率', level=1)
```
