#Alexa Bravo 
#18831
#Matematica discreta
#Seccion 20

import numpy

opcion = 0
while (opcion != "fin"):
    if (opcion != "fin"):
        cantidad = int(opcion)
#Opciones.        
        print ("1. Multiplicacion de Matrices.")
        print ("2. Interseccion de Matrices.") 
        print ("3. Precedencia de dos Matrices.")
        print ("4. Propiedades de la matriz.")
        print ("5. Salir.")
        
#Ingrese la opción.
        eleccion = input("Ingrese su opciòn: ")
        eleccion = int(eleccion)

        if (eleccion == 1):

            fR1 = int(input("Ingrese el numero de filas de la matriz R1: "))
            cR1 = int(input("Ingrese el numero de columnas de la matriz R1: "))
            fR2 = int(input("Ingrese el numero de filas de la matriz R2: "))
            cR2 = int(input("Ingrese el numero de columnas de la matriz R2: "))               

            matrizR1 = numpy.zeros((fR1,cR1))
            matrizR2 = numpy.zeros((fR2,cR2))
            matrizMR = numpy.zeros((fR1,cR2))

            print("Ingrese los valores de la matriz R1")
            for r in range(0, fR1):
                for c in range(0, cR1):
                    matrizR1[r,c] = input("Valor: ")


            print("Ingrese los valores de la matriz R2")
            for r in range(0, fR2):
                for c in range(0, cR2):
                    matrizR1[r,c] = input("Valor: ")

            for r in range (0, fR1):
                for c in range (0, cR2):
                    for k in range (0, fR2):
                        matrizMR[r,c]+= matrizR1[r,k]*matrizR2[k,c]
                        if (r > 1):
                            c = 1
            print (matrizMR)

        elif (eleccion == 2):
            
            fR1 = int(input("Ingrese el numero de filas de la matriz R1: "))
            cR1 = int(input("Ingrese el numero de columnas de la matriz R1: "))
            fR2 = int(input("Ingrese el numero de filas de la matriz R2: "))
            cR2 = int(input("Ingrese el numero de columnas de la matriz R2: "))               

            matrizR1 = numpy.zeros((fR1,cR1))
            matrizR2 = numpy.zeros((fR2,cR2))
            matrizMR = numpy.zeros((fR1,cR2))

            print("Ingrese los valores de la matriz R1")
            for r in range(0, fR1):
                for c in range(0, cR1):
                    matrizR1[r,c] = input("Valor: ")


            print("Ingrese los valores de la matriz R2")
            for r in range(0, fR2):
                for c in range(0, cR2):
                    matrizR1[r,c] = input("Valor: ")

            for r in range (0, fR1):
                for c in range (0, cR2):
                    for k in range (0, fR2):
                        matrizMR[r,c]+= matrizR1[r,k]
                        if (r == 0 or c == 0):
                            MatrizMR(r,c) = 0
                        else:
                            MatrizMR(r,c) = 1

                            print (matrizMR)
             


        elif (eleccion == 3):
            
            fR1 = int(input("Ingrese el numero de filas de la matriz R1: "))
            cR1 = int(input("Ingrese el numero de columnas de la matriz R1: "))
            fR2 = int(input("Ingrese el numero de filas de la matriz R2: "))
            cR2 = int(input("Ingrese el numero de columnas de la matriz R2: "))               

            matrizR1 = numpy.zeros((fR1,cR1))
            matrizR2 = numpy.zeros((fR2,cR2))
            matrizMR = numpy.zeros((fR1,cR2))

            print("Ingrese los valores de la matriz R1")
            for r in range(0, fR1):
                for c in range(0, cR1):
                    matrizR1[r,c] = input("Valor: ")


            print("Ingrese los valores de la matriz R2")
            for r in range(0, fR2):
                for c in range(0, cR2):
                    matrizR1[r,c] = input("Valor: ")

                    
            k = True 
            for r in range (0, fR1):
                for c in range (0, cR2):
                    for k in range (0, fR2):
                        matrizMR[r,c]+= matrizR1[r,k]
                        if (r > c):
                            k = False
                            print (matrizMR)

         elif (eleccion == 5):
             opcion ="fin"
         else:
             print("La opción no es valida.")





             
            

             
                        

            
                        
