word = input('enter a word:')
letter_count = 0
vowel_count = 0
for char in word:
    if char.isalpha():
        letter_count += 1
        if char.lower() in 'aeiou':
            vowel_count += 1
print(f'the number of letter {letter_count}')
print(f'the number of vowels {vowel_count}')  