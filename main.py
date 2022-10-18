laks = input("Kor mange laks ønsker du? ")


def sei_antal_laks(laks):
    if (laks == 1):
        print("1 laks")
        return

    print(laks, "laksar")


for i in range(int(laks)):
    sei_antal_laks(i+1)

