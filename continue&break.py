absent = [2, 5] #결석
no_book = [7] #책 안가지고옴
for student in range(1, 11): #1~10 출석번호가 있다고 가정
    if student in absent:
        continue # 계속해서 다음 반복을 진행
    elif student in no_book:
        print("책 안가지고 온건 허락을 못한다. {0} 교무실로 따라와".format(student))
        break # 바로 종료
    print("{0}, 책을 읽어봐".format(student))