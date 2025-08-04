from okx.app import OkxSWAP
from okx.app.utils import eprint
import user
import get_kdj

# 永续合约行情不需要秘钥
user = user.user( 
    
)
result = get_kdj.get_15m_kdj(user, n=9, m1=3, m2=3)
result = get_kdj.get_1m_kdj(user, n=9, m1=3, m2=3)