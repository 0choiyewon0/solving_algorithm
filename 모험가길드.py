import time


n = int(input())
pa = list(map(int, input().split()))

pa = sorted(pa, reverse = True)
count =0
i =0

start_time = time.time()
while i < len(pa):
    count += 1
    #print("pa[",i,"] : " , pa[i] , "count : ", count)
    i += pa[i]



end_time = time.time()
print(count)
print('time : ', end_time - start_time) 

