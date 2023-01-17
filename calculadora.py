import funciones as func

eleccion = 0
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

# Menu
while eleccion != 5:
    print("""
        1) Suma
        2) Resta
        3) Multiplicación
        4) División
        5) Salir
        """)
    
    eleccion = int(input())
    
    if eleccion == 1:
        func.suma(num1, num2)
        
    if eleccion == 2:
        func.resta(num1, num2)
        
    if eleccion == 3:
        func.multipliacion(num1, num2)
        
    if eleccion == 4:
        func.division(num1, num2)
    
    if eleccion == 5:
        print("Gracias por usar la calculadora, Creada por Kevin Agustin Ruiz")
    