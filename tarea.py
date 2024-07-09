#metodo para mostrar menu de opciones
def menu():
    print('Seleccione el proceso que desea aplicar')
    print('1:Introducir puntos de evaluación y comentarios')
    print('2:Comprueba los resultados hasta ahora.')
    print('3:Terminar.')
    
#metodo para introducir calificaciones y comentarios
def introducirCalificaciones():
    while True:
        print('Por favor, introduzca una puntuación en una escala de 1 a 5')
        point = input()
        if point.isdecimal():
            point = int(point)
            while (point <= 0 or point > 5): # se agrega un bucle while para que verifique el valor
                print('Por favor, introduzca un valor entre el 1 y 5')
                point = input()
                point = int(point)      #se convierte a entero el valor ingresado
                
            else:
                print('Introduzca sus comentarios.')
                comment = input()
                post = f'punto: {point} comentario: {comment}'
                file_pc = open("data.txt", 'a')
                file_pc.write(f'{ post } \n')
                file_pc.close()
                break
        else:
            print('Introduzca los puntos de valoración como números')

#metodo para mostrar calificaciones y comentarios
def mostrarCalificaciones():
    print('Resultados hasta la fecha.')
    read_file = open("data.txt", "r")
    print( read_file.read() )
    read_file.close()

while True:
    menu()                                  #se llama a metodo menu para mostrar opciones
    num = input()

    if num.isdecimal():
        num = int(num)

        if num == 1:
            introducirCalificaciones()      #se llama al metodo para ingresar calificaciones y comentarios            
        elif num == 2:
            mostrarCalificaciones()         #se llama al metodo para mostrar calificaciones y comentarios que se tienen hasta el momento
        elif num == 3:
          print('Terminación.')
          break  # Sintaxis para terminar un proceso repetitivo.
        else:
            print('Por favor, introduzca de 1 a 3')
    else:
        print('Por favor, introduzca de 1 a 3')