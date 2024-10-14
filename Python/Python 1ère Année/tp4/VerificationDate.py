while True:
    date = input("Entrez la date sous la forme jjmmaaaa : ")

    d = int(date[0] + date[1])
    m = int(date[2] + date[3])

    y = str()
    for i in range(4, len(date)):
        y = y + date[i]
    y = int(y)

    if m == 2:
        if (((y % 4) != 0) | ((y % 100) == 0) | ((y % 400) != 0)) & (d > 28):
            print(f"La date est fausse, il n'y a que 28j dans le mois de février de l'année {y}")
        elif d > 29:
            print(f"La date est fausse, il n'y a que 29j dans le mois de février de l'année {y}")
        else:
            print(f"La date {d}/{m}/{y} est correcte")
            break
    elif (m > 12) | (d > 31):
        print("La date est fausse, un mois ne peut contenir plus que 31j")
    elif (1 <= m <= 7) & (m % 2 == 0) & (d > 30):
        print("La date est fausse, il n'y a que 30j dans le mois indiqué")
    elif (8 <= m <= 12) & (m % 2 != 0) & (d > 30):
        print("La date est fausse, il n'y a que 30j dans le mois indiqué")
    else:
        print(f"La date {d}/{m}/{y} est correcte")
        break