#Next: Reconsider enharmonic spellings, ♭IV?, etc...

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

#Generate!
print("\nCHORD PROGRESSION:")
print(random.choice(roman_numeral), "    ", random.choice(roman_numeral),
"    ", random.choice(roman_numeral), "    ", random.choice(roman_numeral))
