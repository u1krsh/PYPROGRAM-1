def tower_of_hanoi(initial,aux,final):
    print("Initial: ",initial,"\nAuxiliary: ",aux,"\nFinal: ",final)

    final.append(initial.pop(0))
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)

    aux.append(initial.pop(0))
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)

    aux.insert(0,final.pop())
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)

    final.append(initial.pop())
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)

    initial.append(aux.pop(0))
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)

    final.insert(0,aux.pop())
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)

    final.insert(0,initial.pop())
    print("Initial: ", initial, "\nAuxiliary: ", aux, "\nFinal: ", final)
initial = ["A","B","C"]
aux = []
final = []
tower_of_hanoi(initial,aux, final)