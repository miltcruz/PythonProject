import string

# Prompt the user for a block of text
text: str = input("Enter a block of text: ")

# Normalize the text
# 1. Convert to lowercase
text: str = text.lower()

# 2. Remove leading and trailing whitespace
text: str = text.strip()

# 3. Remove basic punctuation
translator: dict = str.maketrans("", "", string.punctuation)
cleaned_text: str = text.translate(translator)

# Split the cleaned text into words
words: list = cleaned_text.split()

# Compute statistics
total_words: int = len(words)
average_word_length: float = 0

if total_words > 0:
    total_length: int = sum(len(word) for word in words)
    average_word_length: float = total_length / total_words

# Display the results
print("\nText Analysis Summary")
print("---------------------")
print(f"Total number of words: {total_words}")
print(f"Average word length: {average_word_length:.2f}")