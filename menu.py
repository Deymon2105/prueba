import csv

inventario = {
    "Abono" : 1200,
    "Tierra" : 1000,
    "Lirio" : 1100,
    "Rosas Rojas" : 1700,
    "Margaritas" : 1100
}
print("********************GREEN GARDEN********************")
def gestion_pedido():

    print("\n*****************Sistema de gestión*****************")
    lista_pedidos = []
    lista_factura = []
    total = 0

    #Registro cliente:
    print("\n**********Datos del cliente**********")
    nombre = str(input("Nombre: "))
    lista_pedidos.append(nombre)
    direccion = str(input("Dirección: "))
    lista_pedidos.append(direccion)
    telefono = int(input("Número de telefono: "))
    lista_pedidos.append(telefono)
    #Registro productos
    lista_pedidos = []
    lista_factura = []
    total = 0
    contador = 0
    print("\n**********Productos disponibles**********")
    for clave, valor in inventario.items():
        print(f"{clave} : ${valor}")
    while True:
        producto = str(input("¿Qué producto desea adquirir? "))
        if producto in inventario:
            cantidad = int(input("¿Cuántas unidades quiere del producto? "))
            lista_pedidos.append((producto, cantidad))
            lista_factura.append((producto, cantidad))
            total += inventario[producto] * cantidad
            opcion = str(input("¿Desea comprar algo más? (si/no) "))
            if opcion == "no":
                break
        else:
            print("No tenemos ese producto. Ingrese uno valido")    

    #Lista pedido:
    print("\n**********Registro Pedido**********")        
    print(lista_pedidos)

    #Generar factura
    print("\n**********Factura**********")    
    contador += 1                    
    factura = {
        "Número de factura" : contador,
        "Productos adquiridos" : lista_factura,
        "Total" : total
    }
    for clave, valor in factura.items():
        print(f"{clave} : {valor}")


    #Archivo CSV:
    with open("menu.csv", mode="w") as archivoCsv:
        escribirCsv = csv.writer(archivoCsv)
        escribirCsv.writerow(["Factura", "Productos adquiridos", "Total"])
        escribirCsv.writerows([
            [contador   ,    lista_factura   ,    total]
        ]) 

    with open("menu.csv", mode="r") as archivoCsv:
        leerCsv = csv.DictReader(archivoCsv)
        for elementos in archivoCsv:
            print(elementos) 
                  
#Salir del programa
while True:
    gestion_pedido()
    salir = input("¿Desea salir del programa? (si/no)")
    if salir == "si":
        break
print("********************Gracias por usar nuestro sistema********************")    
