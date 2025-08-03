import os
import sys
import okx 
from okx.app.candle_server import CandleRule,CandleServer
from okx import OkxLite

if __name__ == 'download_candle_history.py':
    # 币币交易：SPOT；永续合约：SWAP；交割合约：FUTURES；期权：OPTION
    instType = 'SWAP' # 永续合约，默认规则
    candleServer = CandleServer(
        instType=instType,
        rule=CandleRule,
        proxies={}, # 使用http和https代理，proxies={'http':'xxxxx','https:':'xxxxx'}，通requests中的proxies参数规则相同
        proxy_host=None,    # 转发：需搭建转发服务器，可参考：https://github.com/pyted/okx_resender
    )
    # 下载2024-01-01 ~ 2024-01-02 全部instType的历史K线
    candleServer.download_candles_by_date(
        start='2024-01-01',
        end='2024-01-02',
        replace=True,  # 如果历史K线存在则替换
    )
    okxlite = OkxLite()
    # 读取指定产品的历史K线
    candle = okxlite.load_candle_by_date(
        instType='SWAP',
        symbol='BTC-USDT-SWAP',
        start='2024-01-01',
        end='2024-01-02',
        bar='1m',
        timezone='Asia/Shanghai',
    )
    candle