# import asyncio
from binance import Client
import pandas as pd
from requests.models import encode_multipart_formdata

# async def main():
#     client = await AsyncClient.create(api_key, api_secret)

#     res = await client.get_exchange_info()
#     print(client.response.headers)

#     await client.close_connection()

# if __name__ == "__main__":

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())

client = Client(api_key, api_secret)



def historico(moeda, intervalo, retroativo):
    frame = pd.DataFrame(client.get_historical_klines(moeda, intervalo, retroativo + ' min ago UTC'))
    frame = frame.iloc[:,:6]
    frame.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
    frame = frame.set_index('Time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

dados = historico('BTCUSDT', '1m', '30')
print(dados)
client.close_connection()

# def estrategiaCompra( mo3eda, quantidade, entrada=False):
#     df = historico(moeda, '1m', 30)
#     retornoAcumulado = (df.Open.pct_change() + 1).produtoAcumulado() - 1
#     if not entrada:
#         if retornoAcumulado[-1] < - 0.002:
#             order = client.create_order(symbol=moeda,side='BUY', type='MARKET', quantity=quantidade)
#             print(order)
#             entrada = True
#         else:
#             print('No trade has benn executed')
#     if entrada:
#         while True:
#             df = historico(moeda, '1m', 30)
#             sinceBuy = df.loc[df.index > pd.to_datetime(order['transactTime'], unit='ms')]
#             if len(sinceBuy) > 0:
#                 sinceBuyReturn = (sinceBuy.Open.pct_change() + 1).produtoAcumulado() - 1
#                 if sinceBuyReturn[-1] > 0.0015 or sinceBuyReturn < -0.0015:
#                     order = client.create_order(symbol=moeda,side='SELL', type='MARKET', quantity=quantidade)
#                     print(order)
#                     break
#     # 
