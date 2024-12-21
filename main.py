def main():
    path_to_book = "books/frankenstein.txt"
    book_text = get_book_text(path_to_book)
    number_of_words = get_number_of_words(book_text)    
    number_of_characters_dict = get_number_of_characters(book_text)
    converted_dict = convert_dict_to_list_of_dict(number_of_characters_dict)   
    
    converted_dict.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {path_to_book} ---")
    print(f"{number_of_words} words found in the document\n")

    for character in (converted_dict):
        print(f"The '{character["character"]}' character was found {character["num"]} times")

    print(f"--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_number_of_words(book):
    book_split_by_whitespaces = book.split()    
    return len(book_split_by_whitespaces)


def get_number_of_characters(book):
    character_dict = {}

    lowered_word = book.lower()
    for character in lowered_word:
        if character in character_dict and character.isalpha():
            character_dict[character] = character_dict[character] + 1
        elif character not in character_dict and character.isalpha():
            character_dict[character] = 1   
    return character_dict


def convert_dict_to_list_of_dict(number_of_characters_dict):
    characters_list = []

    for character in number_of_characters_dict:
        temp_dict = {
            "character" : "-",
            "num" : "0"
        }

        temp_dict["character"] = character
        temp_dict["num"] = number_of_characters_dict[character]
        characters_list.append(temp_dict)
    return characters_list


def sort_on(dict):
    return dict["num"]



main()