#                                                     Toppelever
# Lærer Timur sjekket matematikkprøver i flere klasser på nettskolen BEEGEEK og ønsket å forsikre seg om at det var
# minst én toppelev i hver klasse – en elev med karakteren 5 på prøven.
# Skriv et program med bruk av de innebygde funksjonene all() og any() for å hjelpe Timur med kontrollen.

#                                                   Format for inndata
# Programmet mottar et naturlig tall n – antall klasser. Deretter for hver klasse angis en informasjonsblokk i
# følgende format:
#
# et naturlig tall k – antall elever i klassen;
# deretter angis k linjer i formatet: etternavn karakter.
#                                                      Format for utdata
# Programmet skal skrive ut YES hvis det er minst én toppelev i hver klasse, og NO i motsatt fall.

def filling_data():
    number_klasses = int(input())
    klasses = {}
    for i in range(1,number_klasses + 1):
        number_students = int(input())
        students = []
        for k in range(number_students):
            input_data = input().split()
            data = (input_data[0], int(input_data[1]))
            students.append(data)
        klasses[i] = students
    return klasses


def is_five(user_list):
    return any(map(lambda x: x[1] == 5, user_list))


if __name__ == "__main__":
    classes = filling_data()
    is_all_five = []
    for data in classes.values():
        is_true = is_five(data)
        is_all_five.append(is_true)
    result = "YES" if all(is_all_five) else "NO"
    print(result)
            