# import 모듈

# 모듈.price(3)
# 모듈.price_morning(4)
# 모듈.price_soldier(5)

# import 모듈 as m

# m.price(3)
# m.price_morning(4)
# m.price_soldier(5)

# from 모듈 import *

# price(3)
# price_morning(4)
# price_soldier(5)

# from 모듈 import price, price_morning

# price(5)
# price_morning(4)

# from 모듈 import price_soldier as price

# price(5)

# import travel.thailand
# import travel.thailand.ThailandPackage # 불가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from import 구문에는 모듈이나 패키지, 클래스 함수 모두 임포트 할 수 있음
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *
from travel import *
# trip_to = vietnam.VietnamPackage()
trip_to = thailand.ThailandPackage()
trip_to.detail()

import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))