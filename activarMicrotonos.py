import winsound #Libreria que permite activar sonidos
import time
print("Simulador de microtonos ===")
maximo_microtonos = 25
microtonos_libres = 25
microtonos_activos = 0
ejecutando = True
while ejecutando:
    print("\n=== Panel de microtonos ===")
    print("1.- Ver cuántos microtonos quedan libres")
    print("2.- Activar microtonos (Activación de sonido)")
    print("3.- Recuperar microtonos")
    print("4.- Monitorear el sonido actual")
    print("5.- Salir")
    opcion = int(input("Elige una opción(1-5): "))
    if opcion == 1:
        print(f"\n[INFO] Tienes {microtonos_libres} microtonos disponibles para usar")
    elif opcion == 2:
        print(f"\n ACTIVAR MICROTONOS (Disponibles: {microtonos_libres})")
        if microtonos_libres == 0:
            print("Ya no se pueden emitir mas microtonos, sonido al límite")
        else:
            try:
                cantidad = int(input("¿Cuántos microtonos quieres activar?: "))
                if cantidad <= 0:
                    print("Tienes que activar al menos 1 microtono")
                else:
                    microtonos_libres -= cantidad
                    microtonos_activos += cantidad
                    print("Reproduciendo microtonos")
                    #for i in range (1, cantidad +1):
                    #    print(f"Microtono {i} activado...")
                    #    winsound.Beep (440,300) #440 HZ por 300 miilesimas de segundo
                    #    time.sleep(0.05)
                    frecuencias = [440,440,440,587,880,
                                    784,740,659,1174,880,
                                    784,740,659,1174,880,
                                    784,740,784,659,523,
                                    587]
                    duraciones = [250,250,250,600,600,
                                    180,180,180,600,300,
                                    180,180,180,600,300,
                                    180,180,180,600,300,
                                    180,180,180,500,250,
                                    800]
                    for i in range (1, cantidad +1):
                        nota_actual = frecuencias[(i-1) % len(frecuencias)]
                        duracion_actual = duraciones[(i -1) % len(duraciones)]
                        winsound.Beep(nota_actual,duracion_actual)
                        time.sleep(0.05)
            except ValueError:
                print("Error")
    elif opcion == 3:
        try:
            print(f"\n Recuperar microtonos, actualmente hay {microtonos_activos}  microtonos activos")
            cantidad = int(input("¿Cuantos microtonos quieres recuperar?: "))
            if cantidad <= 0:
                print("Error, la cantidad de microtonos a recuperar debe ser mayor a 0")
            elif microtonos_libres + cantidad > maximo_microtonos:
                print(f"Error: no puedes apagar tantos microtonos porque el maximo es {maximo_microtonos}")
            else:
                microtonos_libres += cantidad
                microtonos_activos -= cantidad
                print(f"Recuperaste {cantidad} de microtonos para ser usados en otro momento")
                winsound.beep(440,150)
        except ValueError:
            print("Error, debes colocar un numero entero")                               
    else:
        print("Error")