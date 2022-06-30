#2022-07-01
L=int(input())
a=input() #문자열
b=0 #해시 함수 총 합을 위한 변수
for i in range(L):
    b+=(ord(a[i])%96)*31**i
print(b%1234567891)

#2022-07-01