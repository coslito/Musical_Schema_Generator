import random
roots = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")

parent_scales = ('Major', 'Melodic Minor', 'Harmonic Minor', 'Half-Whole Diminished', 'Whole-Tone')

intervals = ["Melodic 2nds", "Harmonic 2nds", "Melodic 3rds", "Harmonic 3rds", "Melodic 4ths", "Harmonic 4ths",
             "Melodic 5ths", "Harmonic 5ths", "Melodic 6ths", "Harmonic 6ths", "Melodic 7ths", "Harmonic 7ths",
             "Melodic Octaves", "Harmonic Octaves", "Melodic 9ths", "Harmonic 9ths", "Melodic 10ths", "Harmonic 10ths",
             "Melodic 11ths", "Harmonic 11ths", "Melodic 12ths", "Harmonic 12ths", "Melodic 13ths", "Harmonic 13ths",
             "Melodic 14ths", "Harmonic 14ths", "Melodic 15ths", "Harmonic 15ths"]

#Generate!
print("\nDIATONIC MELODIC & HARMONIC INTERVALS:")
print(random.choice(roots), random.choice(parent_scales), random.choice(intervals), "    ", random.choice(roots),
      random.choice(parent_scales), random.choice(intervals))
