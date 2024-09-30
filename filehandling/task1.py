
file_name = "filehandling/story.txt"
word_count = 0
try:
        
    with open(file_name, 'r', encoding='utf-8') as file:
            
        for line in file:
            words = line.split()
            word_count += len(words)
except FileNotFoundError:
    print(f"The file {file_name} was not found.")

file_name = "filehandling/story.txt"
print(f"The total number of words in the file is: {word_count}")

