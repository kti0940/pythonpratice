# from random import *

# day = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다")

url = "http://naver.com"

my_str = url.replace("http://", "")
my_str = my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(password)

print(url[7:].split(".")[0][:3] + str(len(my_str)) + str(my_str.count("e")) + "!")