#1
'''s="Python Programming"
c=s.split()
for i in c:
    print(i)'''

#2
'''s=input("Введите строку: ")
if s.replace(" ","")==s.replace(" ","").lower()[::-1]:
    print(True)
else:
    print(False)'''

#3
'''s=input("Введите строку: ")
result=[]
for char in s:
    if char not in result:
        result.append(char)
print(''.join(result))'''

#4
'''s=input("Введите строку: ")
k=0
maximum=0
podstroka=0

for i in range(len(s)):
    flag=False
    for j in range(i-k, i):
        if j>=0 and s[j]==s[i]:
            flag=True
            break

    if flag:
        k=i-j
    else:
        k+=1

    if k>maximum:
        maximum=k
        podstroka=i-k+1

print(s[podstroka:podstroka+maximum])'''

#5
'''s=input("Введите строку: ")
result=""
i=0

while i<len(s):
    count = 1
    while i+1<len(s) and s[i]==s[i+1]:
        count+=1
        i+=1
    result+=s[i]+str(count)
    i+=1

if len(result)<len(s):
    print(result)
else:
    print(s)'''