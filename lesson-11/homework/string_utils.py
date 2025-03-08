def reverse_string(a):
    l=len(a)
    res=''
    for i in range(l-1,-1,-1):
        res+=a[i]
    return res

def count_vowels(a):
    vowel=['a','e','u','i','o']
    cnt=0
    for i in a.lower():
        if i in vowel:
            cnt+=1
    return cnt

# print(reverse_string("yunusbek"))
# print(count_vowels("hello"))
