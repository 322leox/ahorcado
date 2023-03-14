

import random
palabras = ["casa","camioneta","globo","juego","tenedor","avioneta","asteroide","ladrillo","maquina","herramienta","libros","perro","pizarra","caja","ventana","cristal","silla","cesped","lavadora","espejo","caracol"]
mododejuego=("Intenta adivinar la palabra secreta. Cadavez que adivines una letra el juego te dira en que posicion se encuentra, siendo 0 la primera. Buena suerte")
def aleatorio(palabras):
  return random.choice(palabras)

elegida=aleatorio(palabras)
dichas=[]
N=[]
vidas= 6
if __name__=="__main__":
    print(mododejuego)
    print(" _ " * len(elegida))
while True:
    letra = input("Dime una letra: ")
    if letra.lower() in dichas:
        print("Ya habias aintentado con esa letra")
    else:
        dichas.append(letra)
        if letra.lower() in elegida:
            print("Adivinaste una letra")
            for pos,char in enumerate(elegida):
                if(char==letra):
                    N.append(pos)
            print("Has adivinado estas letras: {} de {}".format(N,len(elegida)))
        else:
            vidas=vidas-1
            print("Te quedan {} vidas".format(vidas))
        if vidas==0:
            print("La palabra correcta era {}".format(elegida))
            break

    responder=input("Deseas adivinar: ")
    if(responder=="si"):
        respuesta=input("¿Cual es?: ")
        if respuesta==elegida:
            print("Felicidades ganaste")
            break
        else:
          print("Error")