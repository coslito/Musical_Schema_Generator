#SOLVE NEXT: prevent duplicate chord output

import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
parent_scales = ('Major', 'Melodic Minor', 'Harmonic Minor', 'Half-Whole Diminished', 'Whole-Tone')

caged_position = ("C", "A", "G", "E", "D")



#Parent Scale Transitions Generator (Four-Scales)
print("\nPARENT SCALES:")
print(random.choice(roots), random.choice(parent_scales), "    ", random.choice(roots), random.choice(parent_scales),
"    ", random.choice(roots), random.choice(parent_scales), "    ", random.choice(roots), random.choice(parent_scales))
print("\nSTARTING CAGED POSITION:")
print(random.choice(caged_position))