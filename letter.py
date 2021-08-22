def charcount(string):
    return {letter: string.count(letter) for letter in string}
sonuc = charcount("kaan")
print(sonuc)