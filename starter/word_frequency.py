import sys

file_name = sys.argv[1]
result_count = int(sys.argv[2])

word_counts = {}

with open(file_name, 'r') as file:
    for line in file:
        words = line.split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
                
sorted_words = sorted(word_counts.items(), key=lambda item: item[1])
sorted_words = sorted_words[::-1]

result_count = min(result_count, len(sorted_words))

longest_word_length = max(len(word) for word in word_counts.keys())

for i in range(result_count):
    word, count = sorted_words[i]
    spaces = ' ' * (longest_word_length - len(word))
    print(f"{word}{spaces} : {count}")