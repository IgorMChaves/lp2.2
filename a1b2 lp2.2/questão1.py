with open('bases_nitrogenadas.txt', 'r') as var:
    recebevar = var.readlines()
print (recebevar)
print('\n')
a = 0
while a < len(recebevar):
 b = recebevar[a]
 print(("Na"),('linha'),(a+1),(", "),("ADENINA aparece"),(b.count('A')),('vez(es);'))
 print(("Na"),('linha'),(a+1),(", "),("TIMINA aparece"),(b.count('T')),('vez(es);'))
 print(("Na"),('linha'),(a+1),(", "),("CITOSINA aparece"),(b.count('C')),('vez(es);'))
 print(("Na"),('linha'),(a+1),(", "),("GUANINA aparece"),(b.count('G')),('vez(es);'))
 print('\n')
 a=a+1