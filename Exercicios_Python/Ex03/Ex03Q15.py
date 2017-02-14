def ehVogal(b):
    if((b=='a') or (b=='e') or (b=='i') or (b=='o') or (b=='u')):
        return 'Verdadeiro'
    else:
        return ' '

letra = input('digite uma letra: ')
x = letra.lower()

print(ehVogal(x))
