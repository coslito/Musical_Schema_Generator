#SOLVE NEXT:

import random
right_hand_pattern = ("pima", "piam", "pmia", "pmai", "paim", "pami", "ipma", "ipam", "impa", "imap", "iapm", "iamp",
                      "mpia", "mpai", "mipa", "miap", "mapi", "maip", "apim", "apmi", "aipm", "aimp", "ampi", "amip")

four_string_groups = ("6543", "6542", "6541", "6532", "6531", "6521", "6432", "6431", "6421", "6321", "5432", "5431",
                      "5421", "5321", "4321")



#Generate!
print("\nRIGHT-HAND ARPEGGIO PATTERN:")
print(random.choice(right_hand_pattern))
print("\nSTRING-SET:")
print(random.choice(four_string_groups))