def get_num_words(file_contents):
    words = file_contents.split()
    count = len(words)
    print(f"Found {count} total words")

def count_characters(text):
    character_count = {}
    for char in text.lower():
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

def sort_character_counts(character_counts):
    char_count_list = []
    for char, count in character_counts.items():
        char_count_list.append({"char": char, "num": count})

    def get_count(item):
        return item["num"]

    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list