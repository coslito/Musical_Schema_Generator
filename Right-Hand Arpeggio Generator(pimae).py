#SOLVE NEXT:

import random
right_hand_pattern = ("pima", "pime", "piam", "piae", "piem", "piea", "pmia", "pmie", "pmai", "pmae", "pmei", "pmea",
                     "paim", "paie", "pami", "pame", "paei", "paem", "peim", "peia", "pemi", "pema", "peai", "peam",
                      "ipma", "ipme", "ipam", "ipae", "ipem", "ipea", "impa", "impe", "imap", "imae", "imep", "imea",
                      "iapm", "iape", "iamp", "iame", "iaep", "iaem", "iepm", "iepa", "iemp", "iema", "ieap", "ieam",
                      "mpia", "mpie", "mpai", "mpae", "mpei", "mpea", "mipa", "mipe", "miap", "miae", "miep", "miea",
                      "mapi", "mape", "maip", "maie", "maep", "maei", "mepi", "mepa", "meip", "meia", "meap", "meai",
                      "apim", "apie", "apmi", "apme", "apei", "apem", "aipm", "aipe", "aimp", "aime", "aiep", "aiem",
                      "ampi", "ampe", "amip", "amie", "amep", "amei", "aepi", "aepm", "aeip", "aeim", "aemp", "aemi",
                      "epim", "epia", "epmi", "epma", "epai", "epam", "eipm", "eipa", "eimp", "eima", "eiap", "eiam",
                      "empi", "empa", "emip", "emia", "emap", "emai", "eapi", "eapm", "eaip", "eaim", "eamp", "eami")

four_string_groups = ("6543", "6542", "6541", "6532", "6531", "6521", "6432", "6431", "6421", "6321", "5432", "5431",
                      "5421", "5321", "4321")



#Generate!
print("\nRIGHT-HAND ARPEGGIO PATTERN:")
print(random.choice(right_hand_pattern))
print("\nSTRING-SET:")
print(random.choice(four_string_groups))