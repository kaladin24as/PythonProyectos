if __name__ == '__main__':
    n = int(input())
    lista = []
    
    for _ in range(n):
        name = input()
        score = float(input())
        lista.append((name, score))
        
    puntuaciones = [score for _, score in lista]
    puntuacion_minima = min(puntuaciones)
    
    lista_filtrada = [entry for entry in lista if entry[1] != puntuacion_minima]
    
    puntuaciones_filtradas = [score for _, score in lista_filtrada]
    segundo_puntaje_mas_bajo = min(puntuaciones_filtradas)
    
    nombres_segundo_puntaje = [entry for entry in lista_filtrada if entry[1] == segundo_puntaje_mas_bajo]

    nombres_segundo_puntaje_ordenados = sorted(nombres_segundo_puntaje)


    for nombre, calificacion in nombres_segundo_puntaje_ordenados :
        print(f"{nombre}")


##Tomas Farias