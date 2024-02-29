#사전 key와 value 형태

cabinet = {3: "유재석", 100 : "김태호"}  #3번키는 유재석을 정해준다
print(cabinet[3])
print(cabinet.get(3))
#if 없는 key값을 뽑아올 경우 error 발생
# get을 이용할 경우 null값 발생
print(cabinet.get(5))
print(cabinet.get(5,"사용가능")) #nvl 같은거임 null값일 경우 "사용가능" 출력

print(3 in cabinet)
print(10 in cabinet)

#print(cabinet["유재석"]) #value값 넣으면  error

#새 손님
cabinet[3] = "조세호"
cabinet[4] = "김김"
print(cabinet)

# 떠난 손님 del
del cabinet[3]
print(cabinet)

#key 값만 출력
print(cabinet.keys())
#value 만 출력
print(cabinet.values())
#전체 출력
print(cabinet.items())

#폐점의 경우
cabinet.clear() 
print(cabinet)


