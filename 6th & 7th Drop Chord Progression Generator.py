#SOLVE NEXT: prevent duplicate chord output

import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
chord_types = ('Maj 7', 'Maj 6', 'Maj 7♯4', 'Maj 7♯5', 'Maj 7 sus4', 'Min 7', 'Min Maj 7', 'Min 7 sus4', 'Min 7♭5',
            'Min 6', '7', '7♯5', '7♭5', '7 sus4', 'ᵒ 7', 'ᵒ Maj 7')

drop_voicing_type_and_string_groups = ('Drop 3 6432', 'Drop 3 5321', 'Drop 2 4321', 'Drop 2 5432', 'Drop 2 6543',
                                       'Drop 2&3 6542', 'Drop 2&3 5431', 'Drop 2&4 6532', 'Drop 2&4 5421',)
inversion = ("Root Position", "1st Inversion", "Second Inversion", "Third inversion")



#Generate!
print("\n6th & 7th CHORD PROGRESSION:")
print(random.choice(roots), random.choice(chord_types), "    ", random.choice(roots), random.choice(chord_types),
"    ", random.choice(roots), random.choice(chord_types), "    ", random.choice(roots), random.choice(chord_types))
print("\nSTARTING DROP CHORD TYPE/STRING-SET & INVERSION:")
print(random.choice(drop_voicing_type_and_string_groups), ",", random.choice(inversion))