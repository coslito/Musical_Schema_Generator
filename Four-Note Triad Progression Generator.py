#SOLVE NEXT: prevent duplicate chord output

import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
triad_types = ('', '⁻', '⁺', 'ᵒ')

four_string_groups = ("6543", "6542", "6541", "6532", "6531", "6521", "6432", "6431", "6421", "6321", "5432", "5431",
                      "5421", "5321", "4321")
inversion = ("Root Position", "1st Inversion", "Second Inversion")



#Generate!
print("\nFOUR-NOTE TRIADS PROGRESSION:")
print(random.choice(roots), random.choice(triad_types), "    ", random.choice(roots), random.choice(triad_types),
"    ", random.choice(roots), random.choice(triad_types), "    ", random.choice(roots), random.choice(triad_types))
print("\nSTARTING STRING-SET & INVERSION:")
print(random.choice(four_string_groups), ",", random.choice(inversion))