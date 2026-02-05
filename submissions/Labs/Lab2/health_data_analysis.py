# 1. Reading file into a string 
fhandle = open(
    # 2. Resorted to using file path as initial example yielded errors
    r"C:\Users\Jones\Documents\Data Science\SAT4650\submissions\Labs\Lab2\electronic_healthcare_record.txt",
    "r"
)
# 3. Content stored in variable named 'raw_text'
raw_text = fhandle.read()
fhandle.close()

# 4. Text converted to lowercase
raw_text = raw_text.lower()

# 5. New string variable creation
clean_text = " "

raw_text = (raw_text.replace('.', '')
                    .replace(',', '')
                    .replace('!', '')
                    .replace('?', '')
                    .replace("'", '')
                    .replace('"', '')
                    .replace(';', '')
                    .replace(':', '')
                    .replace('(', '')
                    .replace(')', '')
                    .replace('-', '')
                    .replace('_', ''))

# 7. Replacing line breaks with spaces
raw_text = raw_text.replace('\n', ' ')

# 8. This splits on ANY whitespace including the spaces we just added from 7.
words = raw_text.split() 

# And joins back with single spaces
raw_text = ' '.join(words)

# 5: Assigning the raw_text content to the clean_text variable
clean_text = raw_text

# 9: Printing the final cleaned version (clean_text)
# print(clean_text)

# -----------------------End of Problem 1-----------------------------------------------------

# 1. Splitting the text to have individual words
words = clean_text.split()

# 2. Creating dictionary to count word appearences 
word_counts = {}
for word in words:
    if word in word_counts:
        # Increase count if the word already exists
        word_counts[word] += 1
    else:
        # Else start the count at 1 if it's a new word
        word_counts[word] = 1

# 3. Converting to a set to remove duplicates 
unique_words_set = set(words)

# 4. Final collection of unique words
unique_words = list(unique_words_set)


# 5.a) Printing the number of unique words
print("Number of unique words:", len(unique_words))

#  5.b) Printing the frequency of each unique word
print("\nFrequency of each word:")
for word, count in word_counts.items():
    print(f"{word}: {count}")

# 5c. A list of unique words with the first letter capitalized
capitalized_words = [word.capitalize() for word in unique_words]
print("\n Unique words capitalized:")
print(capitalized_words)