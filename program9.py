def clean_text(text):
    return ''.join(ch.lower() for ch in text if ch.isalnum())

def sorting_key(text):
    cleaned = clean_text(text)
    return tuple(sorted(cleaned))


def counting_key(text):
    cleaned = clean_text(text)

    count = {}

    for ch in cleaned:
        if ch in count:
            count[ch] += 1
        else:
            count[ch] = 1
    return tuple(sorted(count.items()))

def are_anagrams(text1, text2):
    return sorting_key(text1) == sorting_key(text2)

# Main Program
print("===== Text Anagram and Pattern Matcher =====")

text1 = input("Enter first word/phrase: ")
text2 = input("Enter second word/phrase: ")

print("\n--- Anagram Checking ---")

if are_anagrams(text1, text2):
    print("The given texts are Anagrams.")
else:
    print("The given texts are NOT Anagrams.")

# Display cleaned text
print("\nCleaned First Text:", clean_text(text1))
print("Cleaned Second Text:", clean_text(text2))

# Display sorted keys
print("\nSorted Key 1:", sorting_key(text1))
print("Sorted Key 2:", sorting_key(text2))

# Display character frequency
print("\nCharacter Frequency Key 1:", counting_key(text1))
print("Character Frequency Key 2:", counting_key(text2))

# Pattern matching using immutable tuple keys
patterns = {}

words = int(input("\nHow many words/phrases do you want to store? "))

for i in range(words):
    text = input("Enter text " + str(i + 1) + ": ")

    key = counting_key(text)

    if key not in patterns:
        patterns[key] = []

    patterns[key].append(text)

print("\n===== Anagram Groups =====")

for key, group in patterns.items():
    if len(group) > 1:
        print(group)