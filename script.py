#Kevin Daniel Gaviria Vallejo
#Evellyn Daniela
#Isabella
#ᵃ
import funciones as fun
import os

#Ingreso
i=1
print('tiene 5 intentos')
#Cant de intentos
while True:
    #los superuser y supercontrasena son variables específicas del usuario actualmente activo. Después va a saber por qué están ahí
    superuser = input('Ingrese su usuario: ')
    supercontrasena = input('Ingrese su contraseña: ')
    prove=fun.comprobar_datos(superuser,supercontrasena)
    
    #Esta línea de código decide si se puede acceder al menú principal con el resultado de la función comprobar_datos
    if prove==True:
        print('''
--------------------------------
--------USUARIO CORRECTO--------
--------INGRESANDO--------------''')
        break
    #Para no hacer jartica la vaina, hay un límite de 5 intentos fallidos
    elif i==5:
        print('--------INTENTELO MÁS TARDE-----')
        exit()
    elif prove==False:
        print(f'tiene otros {5-i} intentos más')
        i=i+1

#menú principal
while True:
    menu = input('''--------------------------------
1. Gestión de usuarios. 
2. Gestión de hemocomponentes. 
3. Salir
-------------------------escoge:  ''')
    if menu =='1':
#Este es el submenú de Gestión de usuarios
        while True:
            menu_gestion = input('''--------ESCOJA UNA OPCIÓN-------

1. Insertar nuevo usuario. 
2. Mostrar todos los usuarios. 
3. Modificar contraseña. 
4. Eliminar usuario 
5. Volver al menú anterior.
-------------------------escoge: ''')
            #Insertar nuevo usuario............................
            if menu_gestion=='1':
                while True:
                    #De nuevo, nuestro amigo comprobar_datos para comprobar que el usuario que se quiere añadir NO esté en la base de datos de login
                    user=input('Nuevo usuario: ')
                    if fun.comprobar_datos(user,None)==True:
                        print('Este nombre de usuario ya está tomado')
                    else:
                        contrasena=input('contraseña: ')
                        fun.nuevo_usuario(user,contrasena)
                        print('--------USUARIO GUARDADO--------')
                        break
            #mostrar usuarios.................................
            elif menu_gestion=='2':
                fun.mostrar_usuarios()
            #modificar contraseña.............................
            elif menu_gestion=='3':
                while True:
                    #Debido a que, por privacidad, cambiar o eliminar contraseñas debe requerir de acceso, puse este *exit para evitar atrancarse
                    user=input('Cuál es el usuario. (Si escribe "*exit" saldrá de este menú):')
                    if user=='*exit':
                        break
                    #again, comp_datos. Esta vez para confirmar el usuario existe
                    elif fun.comprobar_datos(user,None)!=True:
                        print('Ese usuario no se encuentra registrado')
                    else:
                        #y una vez más para confirmar que la contraseña sí le pertenece
                        contrasena=input('la contraseña actual del usuario: ')
                        if fun.comprobar_datos(user,contrasena)!=True:
                            #esto si no pertenece
                            print('Necesita el acceso a su contraseña para cambiarla')
                        else:
                            #esto si sí. Yupi! Se cambió la contraseña
                            nueva_contrasena=input('Ingrese la nueva contraseña: ')
                            fun.nueva_contrasena(user,nueva_contrasena)
                            print(f'----CONTRASEÑA DEL USUARIO {user} CAMBIADA CON ÉXITO----')
                            break
            #Eliminar usuario.................................
            elif menu_gestion=='4':
                while True:
                    #Debido a que, por privacidad, cambiar o eliminar contraseñas debe requerir de acceso, puse este *exit para evitar atrancarse
                    user=input('Usuario que desea eliminar: ')
                    contrasena=input('Contraseña del usuario (Si escribe "*exit" saldrá de este menú): ')
                    comp=fun.comprobar_datos(user,contrasena)
                    if contrasena=='*exit':
                        break
                    elif comp!=True:
                        #una medida de seguridad adicional
                        print('si el usuario y contraseña no coinciden, no se puede eliminar')
                    else:
                        print('---USUARIO ELIMINADO CON ÉXITO--')
                        if user==superuser:
                            #Ni modo de seguir teniendo acceso si tu usuario ya no existe ¿verdad?
                            fun.eliminar_usuario(user)
                            print('--------NO HAY SESIÓN-----------')
                            exit()
                        else:
                            fun.eliminar_usuario(user)
                            break
            #Salir............................................
            elif menu_gestion=='5':
                break
            else:
                print('por favor ingrese una opción válida')
    elif menu =='2':
#Gestión de hemocomponentes.........................................        
        while True:
            menu_hemo=input('''....ESCOJA UNA OPCIÓN....
1. Ingresar una unidad en forma manual 
2. Ingresar unidades sanguíneas desde archivos (automático) 
3. Consultar todas las unidades. 
4. Consultar la información de una unidad. 
5. Modificar información de una unidad. 
6. Eliminar un registro de unidad. 
7. Volver al menú anterior.''')
            #Ingresar manual..................................
            if menu_hemo=='1':
                pass
            #Ingresar automático..............................
            elif menu_hemo=='2':
                pass
            #Consultar todas..................................
            elif menu_hemo=='3':
                pass
            #Consultar una....................................
            elif menu_hemo=='4':
                pass
            #Modificar una....................................
            elif menu_hemo=='5':
                pass
            #Eliminar un registo..............................
            elif menu_hemo=='6':
                pass
            #Salir............................................
            elif menu_hemo=='7':
                break
            else:
                print('por favor ingrese una opción válida')
    elif menu =='3':
        exit()
    else:
        print('por favor ingrese una opción válida')