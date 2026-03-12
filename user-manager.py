salir = 1
lista_usuarios = []

#Esta funcion crea al usuario
def crear_usuario():
    usuario = {
        "nombre": input("Ingrese su nombre de usuario: "),
        "edad" : int(input("Ingrese su edad: ")),
        "email" : input("Ingrese su email: ")
    }
    lista_usuarios.append(usuario)
    return lista_usuarios
#Esta funcion te hace elegir si ver los usuarios o buscar uno en especifico
def usuarios_mostrar(lista_usuarios):
        elija = int(input("1-Para ver usuarios\n2-Para buscar usuarios\n"))
        if elija == 1:
            for usuario in lista_usuarios:
                print(usuario["nombre"],"|", usuario["edad"],"|", usuario["email"])
        elif elija == 2: 
            buscar_usuarios(lista_usuarios)
        else:
            print("Dato erroneo")
#Esta funcion busca a los usuarios
def buscar_usuarios(lista_usuarios):
        busqueda = input("Escriba el nombre a buscar: ")
        encontrado = 0
        for usuario in lista_usuarios:
            if usuario["nombre"] == busqueda:
                print(usuario["nombre"],"|", usuario["edad"],"|", usuario["email"])
                encontrado = 1
                cambiar = int(input("Desea cambiar el email?\n1-Si\n2-no\n"))
                if cambiar == 1:
                    usuario["email"] = input("Ingrese el email: ")
                borrar = int(input("Desea borrar el usuario?\n1-Si\n2-No\n"))
                if borrar == 1:
                    lista_usuarios.remove(usuario)
                    print("Usuario borrado")
                    break
        if encontrado != 1:
            print("No se encontro")

while salir != 0:
    
    #selecciona que operacion se realizara
    eleccion = int(input("seleccione una accion usando el valor numerico correspondiente:\n1-Crear Usuario\n2-Usuarios\n3-Salir\n"))
    if eleccion == 1:
        crear_usuario()
    elif eleccion == 2:
        usuarios_mostrar(lista_usuarios)
    elif eleccion == 3:
        salir = 0
    else:
        print("Dato erroneo")
    
    
    
    
    
    