def sort(num):
    for i in range(len(num)-1):
        t=i
        for j in range(i,len(num)):
            if num[j]>num[t]:
                t=j
        temp=num[i]
        num[i]=num[t]
        num[t]=temp
num1=[12,45,6]
num2=[5,78,45,23]
sort(num1)
sort(num2)
print("the sorted array :")
for i in range(len(num1)):
    print(num1[i])
print("the sorted array")    
for i in range(len(num2)):
    print(num2[i])
