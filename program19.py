def count_consonant(s):
    consonant=''
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            consonant+=i
    return consonant

str1=input()
a=count_consonant(str1)
print(" no of consonants in:'",str1,"' is",a)
