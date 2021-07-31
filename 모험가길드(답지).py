import time

n = int(input())
data = list(map(int, input().split()))
data.sort()

result =0
count =0

start_time = time.time()
for i in data:
    count +=1
    if count >= i:
        result +=1
        count =0

end_time = time.time()
print(result)
print('time : ', end_time - start_time) 
