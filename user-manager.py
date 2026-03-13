lista_usuarios = []

#Esta funcion crea al usuario
def crear_usuario():
    usuario = {
        "nombre": input("Ingrese su nombre de usuario: "),
        "email" : input("Ingrese su email: ")
    }
    try:
        edad =int(input("Ingrese la edad: "))
    except: 
        print("Dato erroneo") 
        edad = "No especificada"
    usuario["edad"] = edad
    lista_usuarios.append(usuario)

#Esta funcion contiene el menu de usuarios
def menu_usuarios(lista_usuarios):
    try:
        elija = int(input("1-Para ver usuarios\n2-Para buscar usuarios\n"))
    except:
        elija = 0
    if elija == 1:
        for usuario in lista_usuarios:
            mostrar_usuarios(usuario)
    elif elija == 2: 
        buscar_usuarios(lista_usuarios)
    else:
        print("Dato erroneo")

#Esta funcion busca a los usuarios
def buscar_usuarios(lista_usuarios):
        busqueda = input("Escriba el nombre a buscar: ")
        encontrado = False
        for usuario in lista_usuarios:
            if usuario["nombre"] == busqueda:
                mostrar_usuarios(usuario)
                encontrado = True
                try:
                    cambiar = int(input("Desea cambiar el email?\n1-Si\n2-no\n"))
                except: cambiar=0
                if cambiar == 1:
                    usuario["email"] = input("Ingrese el email: ")
                try:
                    borrar = int(input("Desea borrar el usuario?\n1-Si\n2-No\n"))
                except:
                    borrar = 0
                if borrar == 1:
                    lista_usuarios.remove(usuario)
                    print("Usuario borrado")
                    break
        if not encontrado:
            print("No se encontro")

#Esta funcion muestra los datos de usuario
def mostrar_usuarios(usuario):
    print(f'{usuario["nombre"]} | {usuario["edad"]} | {usuario["email"]}')

#Esta funcion define la eleccion del usuario
def menu_principal():
    print("1-Crear Usuario")
    print("2-Usuarios")
    print("3-Salir")
    try:
        return int(input("Seleccione una accion usando el valor numerico correspondiente:\n"))
    except:
            return 0


if __name__ == "__main__":
    while True:
        
        eleccion = menu_principal()
        if eleccion == 1:
            crear_usuario()
        elif eleccion == 2:
            menu_usuarios(lista_usuarios)
        elif eleccion == 3:
            break
        else:
            print("Dato erroneo")
        
    
