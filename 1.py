def Count_vowels(s):
    v="aeiouAEIOU"
    c=0    #count
    for char in s:
        if char in v:
            c+=1
    return c
s="bhuvana"
print(Count_vowels(s)) 


