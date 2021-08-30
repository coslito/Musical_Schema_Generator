#SOLVE NEXT:

import random
left_hand_pattern = ("12", "13", "14", "21", "23", "24", "31", "32", "34", "41", "42", "43", "123", "124", "132",
                     "134", "142", "143", "213", "214", "231", "234", "241", "243", "312", "314", "321", "324",
                     "341", "342", "412", "413", "421", "423", "431", "432")
string = ("1", "2", "3", "4", "5", "6")
position = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI")


#Generate!
print("\nLEFT-HAND SLUR PATTERN:")
print(random.choice(left_hand_pattern))
print("\nSTRING:")
print(random.choice(string))
print("\nPOSITION:")
print(random.choice(position))