input_text: str = input("Enter a string: ").strip()
vowels = "aeiouAEIOU"
vowel_count: int = 0

for character in input_text:
    if character in vowels:
        vowel_count += 1

print(f"The number of vowels in the input string is: {vowel_count}")

