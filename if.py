# weather = input("오늘의 날씨는 어떤가요?")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("아무것도 안챙겨도 되요")

temp = int(input("기온은 어때요?"))
if 30 <= temp:
    print("너무 더우니 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추우니 집에 있는게 좋겠어요")