#SOLVE NEXT: prevent duplicate scale output

import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")

superimposition = ('Whole-Step Below', 'Half-Step Above', 'Perfect 4th Above', 'Perfect Fifth Above')

caged_position = ("C", "A", "G", "E", "D")



#Generate!
print("\nDominant 7th Chord:")
print(random.choice(roots), "7")
print("\nSTARTING CAGED POSITION:")
print(random.choice(caged_position))
print("\nMelodic Minor Superimposition:")
print(random.choice(superimposition))
