def number_of_words(text):
     words = text.split()
     total_words = len(words)
     return total_words

def word_counter(text):
    character_counts = {}
    for char in text:
        if char.lower() in character_counts:
            character_counts[char.lower()] = character_counts[char.lower()] + 1
        else: 
            character_counts[char.lower()] = 1
    return character_counts

def char_counter(text):
    report_1 = {}
    for char in text:
        if char.lower() in report_1:
            report_1[char.lower()] = report_1[char.lower()] + 1
        else:
            report_1[char.lower()] = 1
    return report_1

def get_sorted_char_list(report_1):
    new_list = []
    for char, word_counter in report_1.items():
        char_dict = {"char": char, "num": word_counter}
        new_list.append(char_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def sort_on(items):
    return items["num"]
