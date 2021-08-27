arquivo = open("notas.csv", "r")
arquivo.seek(0,0)
mod = []
a = arquivo.readlines()
arquivo.seek(0,0)
cont = len(arquivo.read().split())
arquivo.seek(0,0)
str_arquivo = arquivo.read()
arquivo.seek(0,0)
aux = []
vet = []
n = 0
aux_medias = []
adicao = []
for m in range(0, cont, 6):
    vet.append(arquivo.read().split()[m])
    arquivo.seek(0,0)
    altera = "".join(vet[n])
    str_arquivo = str_arquivo.replace(altera, "")
    arquivo.seek(0,0)
    n = n+1
for m in range(0, n):
    aux_total = a[m].replace(vet[m], "").replace(",","").split()
    maximo = max(aux_total)
    minimo = min(aux_total)
    mod.append(a[m].replace(maximo, "").replace(minimo, ""))
vet_aux = vet
vet = sorted(set(vet))
for m in range(0, len(vet)):
    for n in range(0, len(mod)):
        if vet[m] in mod[n]:
            aux.append(mod[n])
aux_medias = "".join(aux)
for m in range(0, len(vet)):
    aux_medias = aux_medias.replace(vet[m],"")
split_aux = aux_medias.replace(",","").split()
for m in range(0, len(split_aux), 3):
    compilador = 0
    for n in range(m, m+3):
        compilador = float(split_aux[n]) + compilador
    adicao.append(round(compilador/3, 2))
vet_aux = sorted(vet_aux)
tentativa = []
var_media = []
ajuda = []
for m in range(0, len(vet_aux)):
    testando = vet_aux[m], adicao[m]
    tentativa.append(testando)
tentativa = list(tentativa)
for m in range(0, len(vet)):
    for n in range(0, len(tentativa)):
        if vet[m] in tentativa[n]:
            var_media.append(tentativa[n][1])
        if n == len(tentativa)-1:
            var_media.append("\n")
for m in range(0, len(var_media)):
    notas = [str(i) for i in var_media]
var_media = " ".join(notas).split("\n")
resultado = 0
i = 0
tentativa.clear()
print('---TOTAL---')
for m in range(0, len(var_media)-1):
    var_media[m] = sorted(var_media[m].split())[len(var_media[m].split())-2:len(var_media[m].split())]
    resultado = 0
    for n in range(0,2):
        resultado = float(var_media[m][n]) + resultado
    if m != len(var_media)-1:
        print("".join(vet[i]).replace(",", " ->"), round(resultado, 2))
    i = i+1