#Next: Reconsider enharmonic spellings, ♭IV?, etc. Which to exclude?

import random
roman_numeral = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii',
                 'I⁺', 'II⁺', 'III⁺', 'IV⁺', 'V⁺', 'VI⁺', 'VII⁺', 'iᵒ', 'iiᵒ', 'iiiᵒ', 'ivᵒ', 'vᵒ', 'viᵒ', 'viiᵒ',
                 'I', '♭II', '♭III', 'IV', '♭V', '♭VI', '♭VII', 'i', '♭ii', '♭iii', 'iv', '♭v', '♭vi', '♭vii',
                 'I⁺', '♭II⁺', '♭III⁺', 'IV⁺', '♭V⁺', '♭VI⁺', '♭VII⁺', 'iᵒ', '♭iiᵒ', '♭iiiᵒ', 'ivᵒ', '♭vᵒ', '♭viᵒ',
                 '♭viiᵒ'
                 '♯I', '♯II', '♯III', '♯IV', '♯V', '♯VI', 'VII', '♯i', '♯ii', '♯iii', '♯iv', '♯v', '♯vi', 'vii',
                 '♯I⁺', '♯II⁺', '♯III⁺', '♯IV⁺', '♯V⁺', '♯VI⁺', '♯VII⁺', '♯iᵒ', '♯iiᵒ', '♯iiiᵒ', '♯ivᵒ', '♯vᵒ', '♯viᵒ',
                 'viiᵒ'
                 )
tonics = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
#Generate!
print("\nTONIC:")
print(random.choice(tonics))
print("\nCHORD PROGRESSION:")
print(random.choice(roman_numeral), "    ", random.choice(roman_numeral), "    ", random.choice(roman_numeral), "    ", random.choice(roman_numeral))
