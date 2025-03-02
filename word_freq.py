word_freq = dict()
another_str = ""
try:
    with open("pg16317.txt", "r", encoding="utf8") as file:
        file_contents = file.read()

        # Standardize all characters to lower case
        file_contents = file_contents.lower()

        for char in file_contents:
            # Only consider words has all lower case alphabets
            if "a" <= char <= "z":
                another_str += char
            # Append the word to the list of words when terminal is met (no more following lower case alphabet)
            elif len(another_str.strip()) > 0:
                word_freq[another_str] = word_freq.get(another_str, 0) + 1
                another_str = ""

except FileNotFoundError:
    print("Error: 'pg16317.txt' not found.")

# Sort the keys in descending number of occurences
word_freq_sorted_keys = sorted(word_freq, key=word_freq.get, reverse=True)

# Create a new dictionary with the sorted keys
word_freq_sorted = {key: word_freq[key] for key in word_freq_sorted_keys[9:19]}

print("Words ranked from 10th to 20th by frequency:")
for word in word_freq_sorted:
    print(f"{word}: {word_freq_sorted[word]}")
