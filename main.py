

def main():
    stitches = reader()
    yarn_weight(stitches)


def reader():
    print("How many stitches in 4inch/10cm?")
    stitches = int(input())
    return stitches


def yarn_weight(stitches):
    print("The yarn weight are:")
    if stitches <= 6:
        print("Jumbo")
    elif 7 <= stitches <= 12:
        print("Super Bulky")
    elif 14 <= stitches <= 15:
        print("Bulky")
    elif 16 <= stitches <= 17:
        print("Between Bulky and Aran")
    elif stitches == 18:
        print("Aran")
    elif stitches == 19:
        print("Between Aran and Worsted")
    elif stitches == 20:
        print("Worsted")
    elif stitches == 21:
        print("Between Worsted and DK")
    elif stitches == 22:
        print("DK")
    elif stitches == 23:
        print("Between DK and Sport")
    elif 24 <= stitches <= 26:
        print("Sport")
    elif stitches == 27:
        print("Between Sport and Fingering")
    elif stitches == 28:
        print("Fingering")
    elif 29 <= stitches <= 31:
        print("Between Fingering and Light Fingering")
    elif stitches == 32:
        print("Light Fingering")
    elif 33 <= stitches <= 34:
        print("Lace")
    else:
        print("No known weight")

main()