from os import replace
with open('bases_nitrogenadas.txt', 'r') as var:
    recebevar = var.readlines()
print (recebevar)
a=0
while a < len(recebevar):
 b = recebevar[a]
 i1 = b.replace("C","g")
 i2 = i1.replace("G","c")
 i3 = i2.replace("A","u")
 i4 = i3.replace("T","a")
 print('\n')
 print(('Linha'),(a+1),('\nSequência de bases nitrogenadas original:'),b)
 print(('Fita de RNA equivalente:'),(i4.upper()))
 a=a+1