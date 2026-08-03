import random
ids = []
titulos = []
numeros = []
analisis_decimal = []
fechas = []
estados = []
observaciones = []
#---------------------------------------#
#--|menu_principal_analizador_decimal|--#
#---------------------------------------#
while True:
    print("menu principal analizador decimal")
    print("1) crear análisis")
    print("2) editar análisis")
    print("3) eliminar análisis")
    print("4) buscar análisis")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_analisis|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_analisis = 1
        else:
            id_analisis = ids[-1] + 1
        titulo = input("título: ")
        numero = float(input("número decimal: "))
        fecha = input("fecha: ")
        estado = input("estado (analizado o pendiente): ")
        observacion = input("observación: ")
        texto = str(numero)
        if "." in texto:
            parte_entera = int(numero)
            parte_decimal = texto.split(".")[1]
            cantidad_decimales = len(parte_decimal)
        else:
            parte_entera = int(numero)
            parte_decimal = "0"
            cantidad_decimales = 0
        redondeado = round(numero)
        resultado = ""
        resultado += "parte entera: " + str(parte_entera) + " "
        resultado += "parte decimal: " + parte_decimal + " "
        resultado += "cantidad de decimales: " + str(cantidad_decimales) + " "
        resultado += "redondeado: " + str(redondeado)
        ids.append(id_analisis)
        titulos.append(titulo)
        numeros.append(numero)
        analisis_decimal.append(resultado)
        fechas.append(fecha)
        estados.append(estado)
        observaciones.append(observacion)
        print("análisis registrado correctamente.")
        print("id:", id_analisis)
    #---------------------#
    #--|editar_analisis|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {numeros[i]} | {fechas[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {titulos[posicion]} | {numeros[posicion]} | {fechas[posicion]} | {estados[posicion]}")
                titulos[posicion] = input("nuevo título: ")
                numeros[posicion] = float(input("nuevo número decimal: "))
                fechas[posicion] = input("nueva fecha: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                texto = str(numeros[posicion])
                if "." in texto:
                    parte_entera = int(numeros[posicion])
                    parte_decimal = texto.split(".")[1]
                    cantidad_decimales = len(parte_decimal)
                else:
                    parte_entera = int(numeros[posicion])
                    parte_decimal = "0"
                    cantidad_decimales = 0
                redondeado = round(numeros[posicion])
                resultado = ""
                resultado += "parte entera: " + str(parte_entera) + " "
                resultado += "parte decimal: " + parte_decimal + " "
                resultado += "cantidad de decimales: " + str(cantidad_decimales) + " "
                resultado += "redondeado: " + str(redondeado)
                analisis_decimal[posicion] = resultado
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_analisis|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar análisis")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {numeros[i]} | {fechas[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {titulos[posicion]} | {numeros[posicion]} | {fechas[posicion]} | {estados[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    titulos.pop(posicion)
                    numeros.pop(posicion)
                    analisis_decimal.pop(posicion)
                    fechas.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_analisis|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar análisis")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("título:", titulos[posicion])
                print("número decimal:", numeros[posicion])
                print("resultado del análisis:")
                print(analisis_decimal[posicion])
                print("fecha:", fechas[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            analizados = 0
            pendientes = 0
            suma = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {titulos[i]} | {numeros[i]} | {estados[i]}")
                suma += numeros[i]
                if estados[i].lower() == "analizado":
                    analizados += 1
                elif estados[i].lower() == "pendiente":
                    pendientes += 1
            promedio = suma / len(numeros)
            mayor = max(numeros)
            menor = min(numeros)
            print("estadísticas analizador decimal")
            print("cantidad de análisis:", len(ids))
            print("análisis completados:", analizados)
            print("análisis pendientes:", pendientes)
            print("promedio de los números:", round(promedio, 2))
            print("mayor número:", mayor)
            print("menor número:", menor)
            posicion = random.randint(0, len(ids) - 1)
            print("análisis seleccionado")
            print("número:", numeros[posicion])
            print("resultado:")
            print(analisis_decimal[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el analizador decimal.")
        break
    else:
        print("opción no válida.")