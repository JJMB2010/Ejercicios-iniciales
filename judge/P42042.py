a=str(input(""))
if a.isupper():
    print("uppercase")
    if a in "AEIOU":
        print("vowel")
    else:
        print("consonant")
else:
    print("lowercase")
    if a in "aeiou":
        print("vowel")
    else:
        print("consonant")