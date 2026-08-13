import string
from collections import Counter

def analyze_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Remove extra whitespace and split into words
    words = text.split()

    # Total word count
    total_words = len(words)

    # Frequency table
    frequency = Counter(words)

    # Find palindrome words
    palindromes = sorted(set(word for word in words if len(word) > 1 and word == word[::-1]))

    # Display report
    print("\n===== TEXT ANALYSIS REPORT =====")
    print("Total words:", total_words)

    print("\nWord Frequency:")
    for word, count in frequency.items():
        print(word, ":", count)

    print("\nPalindrome Words:")
    if palindromes:
        print(", ".join(palindromes))
    else:
        print("No palindrome words found.")


# Multiline string input
text = """
Madam went to the market.
She saw a level table.
The table was clean and the level was high.
Madam came back home.
"""

analyze_text(text)