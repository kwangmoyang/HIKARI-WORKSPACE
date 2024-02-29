# score_file = open("score.txt", "w", encoding="utf8") #파일을 열어보자
# print("수학 : 0", file=score_file)
# print("영어 : 50", file=score_file)
# score_file.close() #이렇게 하고 나면 score.txt 파일이 생기게 됨



# score_file = open("score.txt", "a", encoding="utf8") #파일을 열어보자
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()



########파일을 불러와보자

score_file = open("score.txt", "r", encoding="utf8")
#print(score_file.read()) #파일 읽기
score_file.close()


########다른 방법으로 불러와서 수정하기
score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
score_file.close()



############라인이 몇줄인지 모를떄
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line :
        break
    print(line, end=" ")
score_file.close()
