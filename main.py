from okx.app import OkxSWAP
from okx.app.utils import eprint
import user
import check_bs
import time

# 永续合约行情不需要秘钥
user = user.user( 
    
)
count = 0
while True:
    
    #打印时间戳
    timestamp = time.time()
    local_time = time.localtime(timestamp)
    local_time_str = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    #print(f"本地时间: {local_time_str}")
    
    # 获取1分钟KDJ
    kdj_1m = check_bs.get_1m_kdj(user, n=9, m1=3, m2=3)

    # 获取15分钟KDJ
    if(count % 15 == 0):
        count = 0
        kdj_15m = check_bs.get_15m_kdj(user, n=9, m1=3, m2=3)
        #print("\nget 15min kdj \n" + kdj_15m.to_string() + "\n1min kdj \n" + kdj_1m.to_string())

        #刷新 上一个 15 kdj
    #else:
        #print("\nget 1min kdj \n"+ kdj_1m.to_string())
   
    if(kdj_15m['j'] == kdj_15m['d'] and kdj_1m['j'] < 0 ):
        print("本地时间: {local_time_str} 满足买入条件 \n\
                        15分钟KDJ: {kdj_15m[k]} {kdj_15m[d]} {kdj_15m[j]}\n\
                        1分钟KDJ: {kdj_1m[k]} {kdj_1m[d]} {kdj_1m[j]}")
        # 执行买入操作
        # 这里可以调用交易API进行实际的买入操作

    # 等待60秒后再次获取
    time.sleep(60)
    count = count + 1