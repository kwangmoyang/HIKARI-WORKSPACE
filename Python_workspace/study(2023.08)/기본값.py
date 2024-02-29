
############## 기본값을 만들자 ##################

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#           .format(name, age, main_lang))


#profile("유재석", 20, "파이썬")
#profile("양광모", 28, "자바")

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
          .format(name, age, main_lang))

#profile("유재석")
    

# 같은 학교 같은 학년 같은 반 같은 수업

############## 키워드를 만들자 ##################

def profile(name, age, main_lang) :
    print(name, age, main_lang)

# profile(name="양광모",age = 28, main_lang = "자바")
# profile(name="양광모",main_lang = "자바", age = 28, )

############## 가변인자가 뭐냐 ##################

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" "는 이어서 밑에줄을 이어나간다는 뜻이다
#     print(lang1, lang2, lang3, lang4, lang5)


def profile(name, age, *language): #넣고싶은 만큼 값을 넣을수 있다. 
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end=" "는 이어서 밑에줄을 이어나간다는 뜻이다
    for lang in language :
        print(lang, end=" ")

profile("유재석", 20, "Python", "Jaba", "C", "C++", "C#", "일어")

 