def get_num_words(sentences):
    num_words = len(sentences.split())
    return num_words

def get_character_count(text):
    character_count = {}

    for c in text.lower():
        if c in character_count:
            character_count[c] += 1
        else:
            character_count[c] = 1

    return character_count

def sort_on(items):
    return items["num"]

def sort_character_count_dict(character_count_dict):
    transformed_dict = []

    for key, value in character_count_dict.items():
        transformed_dict.append({"char": key, "num": value})

    transformed_dict.sort(reverse=True, key=sort_on)
    return transformed_dict