with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

line_count = len(lines)

words = []

for line in lines:
    line = line.lower()          
    line = line.replace(".", "")
    line = line.replace(",", "")
    line = line.replace("!", "")
    line = line.replace("?", "")
    parts = line.split()         
    words.extend(parts)


word_count = len(words)

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

with open("analysis.txt", "w", encoding="utf-8") as file:
    file.write("Total lines: " + str(line_count) + "\n")
    file.write("Total words: " + str(word_count) + "\n\n")
    file.write("Word frequencies:\n")

    for word in frequency:
        file.write(word + ": " + str(frequency[word]) + "\n")

print("Done! Check analysis.txt")

