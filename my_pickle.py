import pickle
# profile_file = open("profile.pickle", "wb") # w 쓰고 b 바이너리, utf8 설정은 필요없고 wb는 반드시 해주어야 한다
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 profile_file에 저장함
# profile_file.close()

profile_file = open("profile.pickle", "rb") # r 로 읽고 b 바이너리 지정
profile = pickle.load(profile_file) # 파일에 있는 정보를 profile 에 불러오기
print(profile)
profile_file.close()