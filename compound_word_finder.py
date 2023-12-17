import time

def read_file(file_name):
    with open(file_name, 'r') as file:
        words = file.read().splitlines()
    return words

def is_compound_word(word, word_set):
    if not word:
        return False

    n = len(word)
    for i in range(1, n):
        prefix = word[:i]
        suffix = word[i:]

        if prefix in word_set and (suffix in word_set or is_compound_word(suffix, word_set)):
            return True

    return False

def find_compound_words(word_list):
    word_set = set(word_list)
    compound_words = [word for word in word_list if is_compound_word(word, word_set)]
    return compound_words

def find_longest_compounded_word(compounded_words):
    if compounded_words:
        compounded_words.sort(key=lambda x: len(x), reverse=True)
        return compounded_words[0]
    return None

def find_second_longest_compounded_word(compounded_words):
    if len(compounded_words) > 1:
        compounded_words.sort(key=lambda x: len(x), reverse=True)
        return compounded_words[1]
    return None

def process_input_file(file_name):
    start_time = time.time()
    words = read_file(file_name)
    compound_words = find_compound_words(words)
    longest_compound_word = find_longest_compounded_word(compound_words)
    second_longest_compound_word = find_second_longest_compounded_word(compound_words)
    end_time = time.time()

    time_taken = (end_time - start_time) * 1000  # in milliseconds
    return longest_compound_word, second_longest_compound_word, time_taken

file_01 = 'Input_01.txt'
file_02 = 'Input_02.txt'

# Process Input_01.txt
longest_compound_01, second_longest_compound_01, time_taken_01 = process_input_file(file_01)

# Process Input_02.txt
longest_compound_02, second_longest_compound_02, time_taken_02 = process_input_file(file_02)

# Display results
print(f"Longest Compound Word in {file_01}: {longest_compound_01}")
print(f"Second Longest Compound Word in {file_01}: {second_longest_compound_01}")
print(f"Time taken to process file {file_01}: {time_taken_01:.2f} milliseconds\n")

print(f"Longest Compound Word in {file_02}: {longest_compound_02}")
print(f"Second Longest Compound Word in {file_02}: {second_longest_compound_02}")
print(f"Time taken to process file {file_02}: {time_taken_02:.2f} milliseconds")
