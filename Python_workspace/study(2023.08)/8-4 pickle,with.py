import pickle
# profile_file = open("profile.pickle", "wb") #피클은 인코딩 필요 없단다
# profile = {"이름" : "박명수", "나이":30, "취미" : ["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()



# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()




# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


#with 를 활용해서 파일을 수정하고 열고 할수있다



#with open("test.txt", "w", encoding="utf-8") as study_file:
#    study_file.write("파이썬을 열심히 공부하고 있어요")



for i in range(1,10) :
    with open(str(i)+"주차 주간보고.txt", "w", encoding="utf-8") as newFile:
        newFile.write(f'''
        "--- {i}주차 주간보고 ---"
         부서 :
         이름 :
         업무 요약 :
        
        '''
        )

print("파일 생성이 전부 완료 되었습니다.")

