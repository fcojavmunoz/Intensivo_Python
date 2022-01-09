
empezar = True
formato_numero = "000000000"
agenda = {"Javier": 111111111,
          "María": 222222222,
          "Lukas": 333333333,
          "Juan" : 444444444}

#1 Buscar contacto

def busqueda_contacto():
    if bool(agenda) == False:
        print("Eres un forever alone: no tienes contactos en la agenda.")
        print()
    else:
        nombre_a_buscar = (input(
            "Escribe el nombre de la persona\n")).title()
        if nombre_a_buscar not in agenda:
            print("Ese contacto no existe")
            agenda_funcion()

        else:
            telefono = agenda[nombre_a_buscar]
            print(nombre_a_buscar,":", telefono)




#2 Añadir nuevo contacto

def nuevo_contacto():
    # formato_numero = "000000000"
    nuevo_contacto_nombre = str(input("Indica su NOMBRE \n")).title()
    if nuevo_contacto_nombre in agenda:
        print("Ese nombre ya existe en la agenda")
        nuevo_contacto()
    else:
        nuevo_contacto_numero = str(input("Indica su NÚMERO DE TELÉFONO (9 dígitos)\n"))

    if len(nuevo_contacto_numero) != len(formato_numero):
        print("Solo puedo guardar números con 9 dígitos.")
        print("Por favor, comprueba que el número es correcto.")
        nuevo_contacto()
    else:
        agenda[nuevo_contacto_nombre] = nuevo_contacto_numero
        print("Contacto añadido correctamente.")
        otro_contacto = int(input("Pulsa 1 si quieres guardar un nuevo contacto.\n"
                                  "Pulsa cualquier otro número para volver al menú principal.\n"))
        if otro_contacto == 1:
            nuevo_contacto()
        else:
            agenda_funcion()


#3 Modificar / borrar contacto


def borrar_contacto():
    if bool(agenda) == False:
        print("Forever alone, que no tienes contactos en la agenda.")
    else:
        print(f"Estos son los contactos que tienes en la agenda\n")
        for k in agenda.keys():
            print(f"---> {k}.")

        nombre_a_borrar = input(
            "Escribe el nombre de la persona que deseas borrar de tu agenda.\n").title()
        try:
            agenda.pop(nombre_a_borrar)
            print(f"El teléfono de {nombre_a_borrar} ha sido borrado correctamente.")
        except KeyError:
            print("El nombre que intentas borrar no existe.")


def editar_contacto():
    if bool(agenda) == False:
        print("Eres un forever alone: no tienes contactos en la agenda.")
        print()
    else:

        nombre_a_editar = str(input(
            "Escribe el nombre de la persona:\n"))
        if nombre_a_editar not in agenda:
            a = int(input("No tienes a ese contacto en la agenda.\n¿Quieres añadirlo? (1=sí)"))
            if a == 1:
                nuevo_contacto()


        else:
            formato_numero = "000000000"

            telefono_editado = input("Escribe el nuevo número de teléfono.\n")
            if len(telefono_editado) != len(formato_numero):
                print("Solo puedo guardar números con 9 dígitos.")
                print("Por favor, comprueba que el número es correcto.")
                print()
                editar_contacto()
            else:
                agenda[nombre_a_editar] = telefono_editado
                print("Contacto modificado correctamente.")
                print()
                otro_contacto = int(input("Pulsa 1 si quieres modificar otro contacto.\n"
                                          "Pulsa cualquier otro número para volver al menú principal.\n"))
                if otro_contacto == 1:
                    editar_contacto()
                else:
                    agenda_funcion()







def modificar_contacto():
    if bool(agenda) == False:
        print("Eres un forever alone: no tienes contactos en la agenda.")
        print()
    else:
        edicion = int(input(
        "Pulse 3 para modificar un contacto existente.\nPulse 8 para borrar un contacto existente\n"))
        if edicion == 3:
            editar_contacto()

        if edicion == 8:
            borrar_contacto()


#4 Ver toda la agenda
def ver_agenda():
    if bool(agenda) == False:
        print("Vaya, al parecer no tienes contactos en la agenda.")
        print()
    else:

        agendaOrdenada = sorted(agenda.items(), key=lambda x: x[0])
        print(agendaOrdenada)


#5 Borrar toda la agenda

def borrar_todo ():
    print("¿Seguro que quieres borrar todos los contactos?")
    seguro = int(
        input("Pulsa 7 si quieres borrar toda la agenda.\n"
                                  "Pulsa cualquier otro número para volver al menú principal.\n"))
    if seguro == 7:
        agenda.clear()
        print("Los contactos han sido borrados correctamente.")
        print()
    else:
        print("La operación ha sido cancelada correctamente.")
        print("Tus contactos siguen guardados en la agenda")
        print()

#6 y #9 (inicio) Salir de la agenda y cerrar la aplicación

def salir_funcion():
    print("La agenda se ha cerrado de manera segura.")
    quit()




def agenda_funcion():
    arrancamos = True
    while arrancamos:
        print()
        print("A  G  E  N  D  A  D  O")
        print()
        print("agenda telefónica de Mercadona")
        print("______________________________")
        print("Selecciona una de las opciones")
        seleccion = int(input(
            ("* 1. Buscar un contacto. \n* 2. Añadir un nuevo contacto. \n* 3. Modificar / Borrar algún contacto."
             "\n* 4. Ver todos los contactos. \n* 5. Borrar toda la agenda. \n* 6. Salir de la agenda. \n")))

        if seleccion == 1: # OK
            busqueda_contacto()

        elif seleccion == 2: # OK
            nuevo_contacto()

        elif seleccion == 3: # OK (o casi, ver si puedo editar el nombre del contacto!!)
            modificar_contacto()

        elif seleccion == 4: # OK
            ver_agenda()

        elif seleccion == 5: # OK
            borrar_todo()

        elif seleccion == 6: # OK
            salir_funcion()
        else:
            print("La opción marcada no está habilitada.")





while empezar:
    try:
        inicio = int(input("Presiona 0 para abrir la agenda o 9 para cerrar la aplicación. \n"))
        if inicio == 0:
            agenda_funcion()
        if inicio == 9:
            salir_funcion()
        else:
           print("Para iniciar la agenda debes pulsar 0. Para cerrarla, el 9.")

    except ValueError:
        print("Sólo puedes elegir entre la opción 0 o 9.")
