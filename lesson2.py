from num2words import num2words
from transliterate import translit
print(translit("""Ladies and gentlemen, I'm 78 years old and I finally got 15 minute same once in a lifetime and i guess that this is mine.\
People have also old me to make these next fes minutes escruciatingly embarrassing and to take vengeance of my enemies. Neither will happen. 
                
More than 3 years ago I moved to Novo-Novsk, but worked on enw Magnetic Storage for last 40. When I was 8...""", 'ru'))
print()
print("78 -", translit(num2words(78),'ru'))
print("15 -", translit(num2words(15), 'ru'))
print("3 -", translit(num2words(3),'ru'))
print("40 -", translit(num2words(40), 'ru'))
print("8 -", translit(num2words(8), 'ru'))
