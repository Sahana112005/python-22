
#string

#frequency of each char
"""
s="programming"
result=""
for i in s:
    if i not in result:
        result=result+i
for j in result:
    count=0
    for i in s:
        if i==j:
            count=count+1
    print(j,":",count, end=",")        
        
"""
#remove duplicatees

"""
s="programming"
result=""
for i in s:
    if i not in result:
        result=result+i
print("without duplicate:",result)        

"""
#check if two strings are anagrams

"""
string1="listen"
string2="silent"
is_anagram=True
if len(string1)!=len(string2):
    is_anagram=False
else:
    list2=list(string2)
    for i in string1:
        if i in list2:
            list2.remove(i)
        else:
            is_anagram=False
            break
print(is_anagram)        

"""

#first unique one

"""
s="twist"
first_unique="none"
for i in range(len(s)):
    char=s[i]
    left=s[0:i]
    right=s[i+1:]
    if(char not in left) and (char not in right):
        first_unique=char
        break
print(first_unique)

"""


#reversing each word in sentence
"""

sentence="python programming"
words=sentence.split(" ")
reverse=[word[::-1]for word in words]
final=" ".join(reverse)
print(final)



"""
"""
s=("python programming")
print(s[::-1])







































