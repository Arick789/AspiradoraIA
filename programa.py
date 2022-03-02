# Colocar la ubicacion en mayusculas A/B
# Pner estado 0/1 con 0 limpio y 1 sucio

def vacuum_cleaner():
    # Iniciar el estado que deseamos
    # 0 es limpio y 1 es sucio
    goal_state = {'A': '0', 'B': '0'}

    # el usuario pone donde esta la aspiradora
    location_input = input("Ubicacion de aspiradora: [A o B]\n")
    # el usuario dice si esta sucia o limpia
    status_input = input("Estado de " + location_input + " [1 sucio, 0 limpio]\n")
    status_input_complement = input("Estado de la otra habitacion [1 sucio, 0 limpio]\n")
    print("Deben quedar asi: " + str(goal_state))

    if location_input == 'A':
        # Habitacion A esta limpia
        print("Aspiradora en habitacion A")
        if status_input == '1':
            print("Habitacion A sucia.")
            # aspirar y marcar como limpio
            goal_state['A'] = '0'
            print("Habitacion A limpia.")

            if status_input_complement == '1':
                # si B esta sucia
                print("Habitacion B sucia.")
                print("Moviendo a la habitacion B. ")
                # aspirar y marcar como limpia
                goal_state['B'] = '0'
                print("Habitacion B limpia. ")
            else:
                # aspirar y marcar como limpio
                print("Habitacion B ya esta limpia.")

        if status_input == '0':
            print("Habitacion A ya esta limpia")
            if status_input_complement == '1':  # si B esta sucio
                print("Habitacion B is sucia.")
                print("Moviendo a la habitacion B. ")
                # aspirar y marcar como limpio
                goal_state['B'] = '0'
                print("Habitacion B limpia.")
            else:
                # aspirar y marcar como limpio
                print("Habitacion B ya esta limpia")

    else:
        print("Aspiradora en habitacion B")
        # Habitacion B esta sucia
        if status_input == '1':
            print("Habitacion B sucia.")
            # aspirar y marcar como limpio
            goal_state['B'] = '0'
            print("Habitacion B limpia.")

            if status_input_complement == '1':
                # si A esta sucio
                print("Habitacion A sucia.")
                print("Moviendo a habitacion A.")
                # aspirar y marcar como limpio
                goal_state['A'] = '0'
                print("Habitacion A limpia")

        else:
            # aspirar y marcar como limpio
            print("Habitacion B ya esta limpia")

            if status_input_complement == '1':  # si A esta sucio
                print("Habitacion A sucia")
                print("Moviendo a habitacion A")
                # aspirar y marcar como limpio
                goal_state['A'] = '0'
                print("Habitacion A limpia")
            else:
                # aspirar y marcar como limpio
                print("Habitacion A ya esta limpia.")

    # limpieza terminada
    print("Objetivo: ")
    print(goal_state)


vacuum_cleaner()
