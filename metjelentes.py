metAdatok = {}
index = 0

# 1. feladat:
with open("tavirathu13.txt", "r") as file:
    for line in file:
        line = line.rstrip().split(sep = " ")
        adat = {
            'telepules' : line[0],
            'ido' : int(line[1]),
            'szel' : line[2],
            'homerseklet' : int(line[3])
        }
        
        metAdatok[index] = adat
        index += 1

# 2. feladat:
print("2. feladat")
telepules = input("Adja meg a település kódját! ")
utolsoMeres = 0

for i in metAdatok:
    if metAdatok[i]['telepules'] == telepules and metAdatok[i]['ido'] >= utolsoMeres: utolsoMeres = metAdatok[i]['ido']

utolsoMeresString = str(utolsoMeres)
utolsoMeresList = list(utolsoMeresString)
utolsoMeresIdopont = (f"{utolsoMeresString[0]}{utolsoMeresString[1]}:{utolsoMeresString[2]}{utolsoMeresString[3]}")

print(f"Az utolsó mérési adat a megadott településről {utolsoMeresIdopont}-kor érkezett.")

# 3. feladat

print("3. feladat")

maxHomerseklet = 0
maxIndex = 0

for i in metAdatok:
    if metAdatok[i]['homerseklet'] > maxHomerseklet:
        maxHomerseklet = metAdatok[i]['homerseklet']
        maxIndex = i
        

print(metAdatok[maxIndex])

# print(f"A legalacsonyabb hőmérséklet: {} {} {} fok.")
# print(f"A legalacsonyabb hőmérséklet: {} {} {} fok.")
