import os
import sys
#root_path = os.path.dirname(os.path.abspath(__file__))
#sys.path.appeclearnd(root_path)
import okx # 导入行情数据

if __name__ == '__main__':
    # 行情数据无需添加key、secret与passphrase
    key = ''
    secret = ''
    passphrase = ''
    flag = '0'  # flag = '0' 实盘 flag = '1' 模拟盘

    market = okx.Market()
    # 获取现货交易BTC-USDT的行情信息
    result = market.get_ticker(instId='BTC-USDT')
    print(sys.path)