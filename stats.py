def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def get_word_count(string_of_words):
    word_list = string_of_words.split()
    word_count = len(word_list)
    return word_count

def get_char_count(string_of_words):
    characters = {}
    char_list = list(string_of_words.lower())
    for i in char_list:
        # if(i is in characters)
        if i in characters:
            # increment the value in characters
            characters[i] = characters[i] + 1
        else:
            # set the value = 1
            characters[i] = 1
    return characters

def sort_char_count(characters):
    char_list = []
    for i in characters:
        new_dict = {}
        new_dict["char"] = i
        new_dict["num"] = characters[i]
        char_list.append(new_dict)
 
    def sort_on(dict):
        return dict["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list