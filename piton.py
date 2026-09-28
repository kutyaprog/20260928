import math as uwu

#tizedespont - tizdesvessző
valos = float(input("Kérek egy valós számot"))
print(f"A szám kerekítve egészre: {round(valos)}")
print(f"A szám 2 tizedes kerekítve: {round(valos, 2)}")

szam1 = int(input("kerem az első szamot"))
szam2 = int(input("kerem az masodik szamot"))

print(f"A {szam1} és {szam2} közöl a nagyobb: {max(szam2, szam1)}")
print(f"A {szam1} és {szam2} közöl a kisebb: {min(szam2, szam1)}")

tavolsag = int(input("Kérem a távolságot: "))
print(f"A megadott távolság: {abs(tavolsag)}")

print(f"a szam felfelé kerekítve: {uwu.ceil(valos)}")
print(f"a szam felfelé kerekítve: {uwu.floor(valos)}")
print(valos)
kerekitett = round(valos, 3)
print(kerekitett)
valos = round(valos, 1)
print(valos)

sugar = float(input("Sugár: "))
kerület = 2*sugar*uwu.pi
print(f"kerület: {round(kerület, 2)}")
terület = uwu.pow(sugar, 2) * uwu.pi
print(f"terület: {round(terület, 2)}")
alap = int(input("Kérek egy számot, megmondom a négyzetgyökét"))
gyok = uwu.sqrt(alap)
print(f"{alap} négyzetgyöke: {gyok}")