dic = {'UUU':'Fenil-alanina', 'UUC':'Fenil-alanina',
    'UUA':'Leucina', 'UUG':'Leucina','CUU':'Leucina', 'CUC':'Leucina','CUA':'Leucina', 'CUG':'Leucina',
    'AUU':'Isoleucina', 'AUC':'Isoleucina','AUA':'Isoleucina','AUG':'metionina - start codon',
    'GUU':'Valina', 'GUG':'Valina','GUA':'Valina', 'GUC':'Valina',
    'UCU':'Serina', 'UCC':'Serina','UCA':'Serina','UCG':'Serina',
    'CCU':'Prolina','CCC':'Prolina', 'CCA':'Prolina','CCG':'Prolina',
    'ACU':'Treonina','ACC':'Treonina', 'ACA':'Treonina','ACG':'Treonina',
    'GCU':'Alanina','GCC':'Alanina', 'GCA':'Alanina','GCG':'Alanina',
    'UAU':'Tirosina','UAC':'Tirosina', 'UAA':'Stop codon','UAG':'Stop codon',
    'CAU':'Histidina', 'CAC':'Histidina','CAA':'Glutamina','CAG':'Glutamina',
    'AAU':'Asparagina','AAC':'Asparagina','AAA':'Lisina', 'AAG':'Lisina',
    'GAU':'Acido aspartico', 'GAC':'Acido aspartico','GAA':'Acido Glutamico', 'GAG':'Acido Glutamico',
    'UGU':'Cysteine','UGC':'Cysteine', 'UGA':'Stop codon','UGG':'Tryptophan',
    'CGU':'Arginina','CGC':'Arginina', 'CGA':'Arginina','CGG':'Arginina',
    'AGU':'Serina', 'AGC':'Serina','AGA':'Arginina', 'AGG':'Arginina',
    'GGU':'Glicina', 'GGC':'Glicina','GGA':'Glicina','GGG':'Glicina'}
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
 i4 = i4.upper()
 j=0
 print('Aminoácido(s) sitentizado(s):') 
 for j in range(3, len(i4), 3):
    v1 = ''
    v1 = i4[j-3]
    v1 += i4[j-2]
    v1 += i4[j-1]
    print (dic[v1])
    if j == len(i4)+3:
        break
 a=a+1