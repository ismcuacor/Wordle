fichero = open('0_palabras_todas.txt', 'r',encoding="utf-8")
diccionario={}
for linea in fichero:
    linea = linea.replace('\n', '')
    linea = linea.replace(' ', '')
    if len(linea)==5:
        diccionario[linea]=0

abecedario={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'ñ':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
def eligePalabraDiccionario(nuevoDiccionario):
    #le asigno a las letras un valor según el número de veces que aparezcan en el diccionario. Una vez por palabra
    for palabra in nuevoDiccionario:
        #le quito a la palabra las letras repetidas
        palabraNoRepe=set(palabra)
        palabraNoRepe="".join(palabraNoRepe)
        for letra in palabraNoRepe:
            aux = abecedario[letra]
            abecedario[letra] = aux + 1
    #le asigno a las palabras (en el diccionario) un valor que es el sumatorio de los valores que tienen asignadas las letras. Sin repetir letra.
    valor=0
    valorPalabra=0
    for palabra in nuevoDiccionario:
        #le quito a la palabra las letras repetidas
        palabraNoRepe=set(palabra)
        palabraNoRepe="".join(palabraNoRepe)
        for letra in palabraNoRepe:
            valor = valor + abecedario[letra]
            valorPalabra=valorPalabra+valor
            valor=0
        diccionario[palabra]=valorPalabra
        valorPalabra=0
    palabraSugeridaPorDef=max(diccionario, key=diccionario.get)
    return(palabraSugeridaPorDef);
palabraSugerida=eligePalabraDiccionario(diccionario)
print("Empieza escribiendo la palabra "+ palabraSugerida + " y ya vamos viendo.")
diccionario.pop(palabraSugerida)

while 1==1: 
    resultado=input("¿Qué tal ha ido? Escribe los fallos con (-), los aciertos en minusculas y las letras correctas en lugar incorrecto en mayusculas: ")
    if resultado==palabraSugerida:#rompe el bucle si pones la misma palabra que te ha sugerido
        break
    if resultado=="0": #le pongo un 0 para quitar esa palabra por si no existe en el juego
        diccionario.pop(palabraSugerida)
    contadorLetra=0
    for letraResultado in resultado:
        diccionarioAux=diccionario.copy()
        for palabra in diccionario:
            if letraResultado=="-" and palabraSugerida[contadorLetra] in palabra:
                #print("- "+palabraSugerida[contadorLetra]+" "+palabra)
                diccionarioAux.pop(palabra)
            elif letraResultado.isupper() and (palabraSugerida[contadorLetra] == palabra[contadorLetra] or not (palabraSugerida[contadorLetra] in palabra)):
                #print("M "+palabraSugerida[contadorLetra]+" "+palabra)
                diccionarioAux.pop(palabra)
            elif letraResultado.islower() and (palabraSugerida[contadorLetra] != palabra[contadorLetra] or not(palabraSugerida[contadorLetra] in palabra)):
                #print("m "+palabraSugerida[contadorLetra]+" "+palabra)
                diccionarioAux.pop(palabra)
        diccionario=diccionarioAux.copy()
        contadorLetra=contadorLetra+1
        #con esto he modificado el diccionario con las pistas que me ha dado el juego
    palabraSugerida=eligePalabraDiccionario(diccionario) #saca la palabra con mas puntos del nuevo diccionario
    print("De acuerdo, ahora prueba con "+ palabraSugerida)
print("Eso significa que hemos acertado,¡Enhorabuena!")

