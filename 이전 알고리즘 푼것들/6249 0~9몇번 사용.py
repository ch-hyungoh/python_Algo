array = [0]*10
num = int(input())
result = ""

while num:
    array[num%10] +=1
    num //= 10

for i in range(0, 10):
    result += "%d" % i

print(result[0:len(result)-1])

result =""
for i in range(0, 10):
    result += "%d" % array[i]
print(result[0:len(result)-1])