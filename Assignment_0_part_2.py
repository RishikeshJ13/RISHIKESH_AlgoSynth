#Part2

arr=[]
count = 0
while(count<5):
    num = int(input(f"Enter number {count+1}: "))
    arr.append(num)
    count+=1

for i in arr:
    if(i%2==0):
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
