#SOLVE NEXT: prevent duplicate chord output

import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
triad_types = ('', '⁻', '⁺', 'ᵒ')

#Generate!
print("\nTRIADS OVER BASS NOTES:")
print("    ", random.choice(roots), random.choice(triad_types))
print("    ", "—")
print("    ", random.choice(roots))