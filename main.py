from okx.app import OkxSWAP
from okx.app.utils import eprint
import user
import get_kdj
import time

# 永续合约行情不需要秘钥
user = user.user( 
    
)
count = 0
last_15m_j = 0
last_1m_j = 0
while True:
    
    #打印时间戳
    timestamp = time.time()
    local_time = time.localtime(timestamp)
    local_time_str = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
    print(f"本地时间: {local_time_str}")
    
    # 获取1分钟KDJ
    kdj_1m = get_kdj.get_1m_kdj(user, n=9, m1=3, m2=3)

    # 获取15分钟KDJ
    if(count % 15 == 0):
        count = 0
        kdj_15m = get_kdj.get_15m_kdj(user, n=9, m1=3, m2=3)
        print("get 15min kdj " + kdj_15m.to_string() + " 1min kdj " + kdj_1m.to_string())

        #刷新 上一个 15 kdj
        last_15m_j = kdj_15m
    else:
        print("get 1min kdj "+ kdj_1m.to_string())
   
    # 等待60秒后再次获取
    time.sleep(60)
    count = count + 1