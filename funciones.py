import os
import funciones as fun
#NI SE ATREVA NADIE A MODIFICAR ESTA FUNCIÓN----------------------------------------------------
def tomar_usuarios():
    '''Esta función no requiere de variables. Lee el archivo "admin/login.txt" y la separa en listas
    No fué sino hasta después de terminar que me enteré de que haber incluido el paso de usuario=usuario.split(':') hubiera sido más cómodo'''
    file = open('admin/login.txt', mode='r', encoding='utf8')
    list_usuarios = file.readlines()
    file.close()
    i=0
    for usuario in list_usuarios:
        correccion = usuario.strip() #el .strip() elimina el "\n" de los datos
        list_usuarios[i]= correccion
        i=i+1 #Al hacer usuario=usuario.strip() no funcionaba así que aquí hay un bonito contador para reescribir a la fuerza
    return list_usuarios
#-----------------------------------------------------------------------------------------------
#OTRA PROHIBIDA---------------------------------------------------------------------------------
def comprobar_datos(user:str, password):
    '''user: usuario
    password: contraseña
    Esta función puede recibir los datos de usuario y/o contraseña. De necesitar comprobar que ambos estén relacionados en la base de datos añadir los dos
    en caso de que no, poner None en el dato que no necesite'''
    list_usuarios= tomar_usuarios()
    for usuario in list_usuarios:
        usuario=usuario.split(':')
        if user is not None and password is not None: #Con esta parte se vinculan usuario y contraseña en a bd de login
            if user == usuario[0] and password == usuario[1]:
                return True
        elif user is not None and password is None: #Este solo para saber si ya está el usuario
            if user == usuario[0]:
                return True
        elif user is None and password is not None: #Este solo para saber si ya está la contraseña (si de algo te sirviera)
            if password == usuario[1]:
                return True
    return False #Así se ahorra un poquito de trabajo la máquina
#print(comprobar_datos('a',None))
#login------------------------------------------------------------------------------------------
def login(user, password):
    '''user: usuario
    password: contraseña
    Comprueba si los datos de inicio de sesión son iguales a alguno del archivo login.txt.
    Era útil hasta que se creó comprobar datos. Ahora está aquí sólo por nostalgia'''
    list_usuarios=fun.tomar_usuarios()
    datos_usuario=f'{user}:{password}'
    ingreso =False
    if datos_usuario in list_usuarios:        
        ingreso = True
    return ingreso
#print(login('Admin', 'Admin123'))
#-----------------------------------------------------------------------------------------------
def mostrar_usuarios(): #Si se pregunta porqué solo salen los usuarios y no la contraseña, privacidad
    '''Función que no requiere valores anteriores. Muestra los usuarios de login.txt de una forma fácil de leer. Con orden de antigüedad y todo'''
    list_usuarios=fun.tomar_usuarios()
    print('----LOS USUARIOS SON----')
    i=1
    for usuario in list_usuarios:
        datos=usuario.split(':')
        print(f'''Usuario {i}: {datos[0]}''')
        i+1
    
    print('----USUARIOS ARRIBA----')
    return None
#mostrar_usuarios()
#-----------------------------------------------------------------------------------------------
def nuevo_usuario(user,password):
    '''user: usuario
    password: contraseña
    Añade un nuevo usuario (una linea independiente) a login.txt con la estructura key:value de los diccionarios como user:password. Pero sin serlo'''
    file =open('admin/login.txt', mode='a', encoding='utf8')
    file.write(f'\n{user}:{password}')
    file.close()
    return None
#nuevo_usuario('a','b')
#-----------------------------------------------------------------------------------------------
def nueva_contrasena(user, password):
    '''user: usuario
    password: contraseña
    Lee el archivo login.txt y lo guarda como lista. Luego, compara cada primer dato de la lista. Si coincide, cambia el segundo dato por password'''
    list_usuarios = fun.tomar_usuarios()
    #Hacer el cambio en el texto
    list_usuarios_final=[]
    for usuario in list_usuarios:
        usuario = usuario.split(sep=':')
        if user == usuario[0]: #compara
            usuario[1]=password
        usuario=':'.join(usuario) #Esto permite recobrar la estructura key:value
        list_usuarios_final.append(usuario)
    txt_usuario= '\n'.join(list_usuarios_final) #con esta línea se vuelve a tener un archivo de texto con los datos
    
    #Reescribir el archivo login.txt
    file=open('admin/login.txt', mode='w', encoding='utf8')
    file.write(txt_usuario)
    return None
#nueva_password('a','pepe')
#-----------------------------------------------------------------------------------------------
def eliminar_usuario(user):
    '''user= usuario
    Compara el user con cada primer dato de los objetos de la lista guardando su indice. Cuando coincide, usar el método pop() con el índice que tiene guardado. Eliminando esa parte
    Luego vuelve a reescribir el archivo txt'''
    list_usuarios= fun.tomar_usuarios()
    list_usuarios_final=[]
    i=0
    for usuario in list_usuarios:
        usuario = usuario.split(':')
        if user==usuario[0]:
            j=i
        usuario=':'.join(usuario)
        i=i+1
        list_usuarios_final.append(usuario)
    try:
        list_usuarios_final.pop(j)
    except:
        print('no se halla dicho usuario\n')
    txt_usuario= '\n'.join(list_usuarios_final)
    #Reescribir el archivo login.txt
    file=open('admin/login.txt', mode='w', encoding='utf8')
    file.write(txt_usuario)
    return None
#eliminar_usuario('a')
