python = "Python is Amazing"
print(python.lower()) # 소문자로 만들기
print(python.upper()) # 대문자로 만들기
print(python[0].isupper()) #특정 문자 대문자 확인
print(len(python)) # 문자열 길이 확인
print(python.replace("Python", "Java")) # 문장 바꾸기

index = python.index("n") # 문자 위치 확인
print(index)

index = python.index("n", index + 1 ) #다음 위치부터 찾기
print(index)

print(python.find("Java")) #원하는 값이 없는 경우 -1을 반환
# print(python.index("Java")) #오류를 뱉고 종료됨

print(python.count("n")) # 몇번 등장하는지 갯수 세기
