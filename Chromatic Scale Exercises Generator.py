#SOLVE NEXT:

import random
left_hand_pattern = ("1234", "1243", "1324", "1342", "1423", "1432", "2134", "2143", "2314", "2341", "2413", "2431",
                     "3124", "3142", "3214", "3241", "3412", "3421", "4123", "4132", "4213", "4231", "4312", "4321")
right_hand_pattern = ("pi", "pm", "pa", "ip", "im", "ia", "mp", "mi", "ma", "ap", "ai", "am")
string = ("1", "2", "3", "4", "5", "6")
position = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII", "XIII", "XIV", "XV", "XVI")


#Generate!
print("\nLEFT-HAND PATTERN:")
print(random.choice(left_hand_pattern))
print("\nRIGHT-HAND PATTERN:")
print(random.choice(right_hand_pattern))
print("\nSTRING:")
print(random.choice(string))
print("\nPOSITION:")
print(random.choice(position))