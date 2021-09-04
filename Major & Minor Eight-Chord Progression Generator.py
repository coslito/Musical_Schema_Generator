#SOLVE NEXT: prevent duplicate chord output

import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
triad_types = ('', '⁻')
three_string_groups = ('654', '653', '652', '651', '643', '642', '641', '632', '631', '621', '543', '542', '541', '532',
                       '531', '521', '432', '431', '421', '321')

inversion = ("Root Position", "1st Inversion", "Second Inversion")


#Generate!
print("\nTHREE-NOTE TRIADS PROGRESSION:")
print(random.choice(roots), random.choice(triad_types), "    ", random.choice(roots), random.choice(triad_types),
"    ", random.choice(roots), random.choice(triad_types), "    ", random.choice(roots), random.choice(triad_types), "    ",
random.choice(roots), random.choice(triad_types), "    ", random.choice(roots), random.choice(triad_types),
"    ", random.choice(roots), random.choice(triad_types), "    ", random.choice(roots), random.choice(triad_types))
print("\nSTARTING STRING-SET & INVERSION:")
print(random.choice(three_string_groups), ",", random.choice(inversion))


