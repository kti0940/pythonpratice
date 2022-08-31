# from random import *

# day = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월" + str(day) + "일로 선정되었습니다")

# url = "http://naver.com"

# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")]
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

# print(password)

# print(url[7:].split(".")[0][:3] + str(len(my_str)) + str(my_str.count("e")) + "!")

# from random import *
# users = range(1,21) # 1부터 20까지 숫자를 생성
# users = list(users)
# print(users)
# shuffle(users)
# print(users)
# winners = sample(users, 4) # 4명중에서 1명은 치킨 3명은 커피
# print(winners)
# print(" -- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("치킨 당첨자 : {0}".format(winners[1:]))

# from random import *

# count = 0
# for i in range(1, 51):
#     time = randrange(5, 51)
#     if 5 <= time <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
#         count += 1
#     else: # 매칭 실패한 경우
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        
# print("총 탑승 승객 : {0}분".format(count))

# def std_weight(height, gender):
#     if gender == "남자":
#         return(height * height * 22)
#     else:
#         return(height * height * 21)

# height = 175
# gender = "남자"
# weight = std_weight(height / 100, gender)
# weight = round(weight, 2)
# print(f"키 {height}cm {gender}의 표준 체중은 {weight}입니다")

# for i in range(1,51):
#     with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간 보고 - ".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")
        