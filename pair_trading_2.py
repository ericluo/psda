# %% 
from jqdatasdk import *
auth('18986290611', 'Wenbl0821')
code = normalize_code('601601')
sec = get_security_info(code)
# get_price(sec, start_date='2019-01-01', end_date='2020-02-28')
code = normalize_code('601601')
stk= finance.STK_AH_PRICE_COMP
q = query(stk).filter(stk.a_code == code).order_by(stk.day)
df = finance.run_query(q)
df[h_a_comp]
# %%
import cufflinks as cf
df[['day', 'h_a_comp']].iplot(x='day', y='h_a_comp')

df['h_a_comp'].describe()

# %%
import pandas_datareader as pdr
df = pdr.get_data_yahoo("600036.SS", '2017-01-01', '2019-12-31')
type(df)

#%%
import pandas as pd
import cufflinks as cf

def bolling(periods = 20, boll_std = 2):
  df = pd.read_excel("./ah_pair_trading.xls", parse_dates=['day'], index_col='day')
  df['SMA'] = df['h_a_comp'].rolling(periods).mean()
  df['UPPER'] = df['SMA'] + df['h_a_comp'].rolling(periods).std() * boll_std
  df['LOWER'] = df['SMA'] - df['h_a_comp'].rolling(periods).std() * boll_std
  return df.dropna()
bolling()
# df['ma5'] = df['h_a_comp'].rolling(5).mean()
# df['ma20'] = df['h_a_comp'].rolling(20).mean()
# df.iplot(bestfit=True)
# df.ffill(inplace=True)
# annotations = {'2020-01-03': '卖A买H', '2020-01-20': '卖A买H', '2020-02-06': '卖H买A', '2020-02-12': '卖H买A', '2020-02-26': '卖A买H'}
# df.ta_plot(study='boll', periods=20, dimensions=(1600,900), annotations=annotations)
# %%
df = bolling()
df['a2h'] = df['h_a_comp'] > df['UPPER']
df['h2a'] = df['h_a_comp'] <= df['LOWER']
# df.to_excel("trading.xls")

positions = {'A': 5000, 'H': 0, 'cash': 0}
import logging
import sys
logger = logging.getLogger()
logger.setLevel(logging.INFO)
if not logger.handlers: 
  logger.addHandler(logging.StreamHandler())

for row_index, row in df.iterrows():
  a_price = row['a_price']
  h_price = a_price / row['h_a_comp']

  # 如果持有A股仓位，且A股溢价20%以上，当出现A股换H股信号时，调仓
  # 由于A股持仓具有免红利税，或红利税低于港股，以及底仓打新的效用，因此A股估值上可以溢价20%
  # 即A股溢价20%（含）以内，不调仓。
  if row['a2h'] and positions['A'] > 0 and row['h_a_comp'] > 1.2:
      # 调仓
    cash = positions['A'] * a_price
    positions['H'] = cash / h_price
    logger.info(f"On {row_index:%Y%m%d} A2H, 卖出A {positions['A']:.0f}, 买入H {positions['H']:.0f},溢价率{row['h_a_comp']:.0%}")
    positions['A'] =0
  # 如果持有H股仓位，当出现H股换A股信号时，调仓
  if row['h2a'] and positions['H'] > 0:
    # 调仓
    cash = positions['H'] * h_price
    positions['A'] = cash / a_price
    logger.info(f"On {row_index:%Y%m%d} H2A, 卖出H {positions['H']:.0f}, 买入A {positions['A']:.0f}, 溢价率{row['h_a_comp']:.0%}")
    positions['H'] = 0

print(positions)

# Parameters:
#   direction: 'a2h' or 'h2a'
#   strategy: 'value' or 'amount'
def pair_trade(direction, strategy = 'value'):
  if 'a2h'.casefold() == 'a2h':
    cash = positions['A'] * a_price
    positons['H'] = cash / h_price
    positions['A'] = 0
  elif 'h2a'.casefold() == 'h2a':
    cash = positions['H'] * h_price
    positions['A'] = cash / a_price
    positions['H'] = 0

def trade_by_cash():
  pass
