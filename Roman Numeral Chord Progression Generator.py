#Next: Reconsider enharmonic spellings, ♭IV?, #iii, etc. Which to exclude/include?
#Remove duplicates in roman_nemrals!
#Prevent duplicates in output


import random
roman_numeral = ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii',
                 'I⁺', 'II⁺', 'III⁺', 'IV⁺', 'V⁺', 'VI⁺', 'VII⁺', 'iᵒ', 'iiᵒ', 'iiiᵒ', 'ivᵒ', 'vᵒ', 'viᵒ', 'viiᵒ', '♭II',
                 '♭III', 'IV', '♭V', '♭VI', '♭VII', 'i', '♭ii', '♭iii', 'iv', '♭v', '♭vi', '♭vii',
                 'I⁺', '♭II⁺', '♭III⁺', 'IV⁺', '♭V⁺', '♭VI⁺', '♭VII⁺', '♭iiᵒ', '♭iiiᵒ', '♭vᵒ', '♭viᵒ',
                 '♭viiᵒ', '♯II', '♯IV', '♯V', '♯VI', 'VII', '♯ii', '♯iii', '♯iv', '♯v', '♯vi', '♯II⁺', '♯IV⁺',
                 '♯V⁺', '♯VI⁺', '♯iiᵒ', '♯ivᵒ', '♯vᵒ', '♯viᵒ')
tonics = ("A", "A♯", "B", "B♯", "C", "C♯", "D", "D♯", "E", "E♯", "F", "F♯", "G", "G♯", "A♭", "B♭", "C♭", "D♭", "E♭",
         "F♭", "G♭")
#Generate!
print("\nTONIC:")
print(random.choice(tonics))
print("\nCHORD PROGRESSION:")
print(random.choice(roman_numeral), "    ", random.choice(roman_numeral), "    ", random.choice(roman_numeral), "    ", random.choice(roman_numeral))
