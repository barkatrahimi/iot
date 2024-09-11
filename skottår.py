def är_skottår(år):
    if (år % 4 == 0 and år % 100 != 0) or (år % 400 == 0):
        return True
    else:
        return False

år = int(input("skriv ett år: "))

if är_skottår(år):
    print("skottår.".format({år}))
else:
    print(" inte skottår.".format({år}))