import time

num = list(map(int, input()))
sum1=sum2 =0



for i in range(len(num)//2):
    sum1 += num[i]
    #print(sum1)


for i in range((len(num)//2),len(num)):
    sum2 += num[i]
    #print(sum2)

if sum1 == sum2 :
    print("LUCKY")
else:
    print("READY")
