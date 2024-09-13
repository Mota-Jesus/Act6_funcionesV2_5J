print("Funciones version 2")
print("Jesus Mota")
# zona de tuplas, set y diccionario
celulares=["Samsung S24 Ultra","Iphone 15 Pro Max","Chafa"]
BENCHPRESS=["Roger","Top globales","Un haitiano"]
SET={"Tadeo","David","Sergio"}
DICK={
    "DODGE":"Charger",
    "FORD":"Mustang",
    "CHEVY":"Camaro"
}

# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print("--",uncelular,"--")

def verBanca(pressbanca):
    for banca in pressbanca:
        print("🔱🔱",banca,"🔱🔱")

def integrantesSi14(si14):
    for INTE in si14:
        print("--",INTE,"--")
        
# Llamadas a funciones
print("~~ IMPRIME CELULARES ~~")
verlista(celulares) 
print("~~ IMPRIME LOS MEJORES EN PRESS BANCA ~~")
verBanca(BENCHPRESS) 
print("~~ IMPRIME EL DICCIONARIO DE CARROS~~")
for x in DICK:
    print(DICK[x])
print("~~ IMPRIME INTEGRANTE DE 'Si 14' ~~")
integrantesSi14(SET)