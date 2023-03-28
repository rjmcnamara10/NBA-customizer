manual_formats = {"deandre":"DeAndre", "demar":"DeMar", "derozan":"DeRozan", "divincenzo":"DiVincenzo", "javale":"JaVale", 
"lamelo":"LaMelo", "lavine":"LaVine", "lebron":"LeBron", "levert":"LeVert", "rj":"RJ", "vanvleet":"VanVleet"}

def custom_title(string):
    split_string = string.split()
    new_string = []
    for word in split_string:
        if len(word) < 3:
            new_string.append(word.upper())
        else:
            new_string.append(word.title())
    return " ".join(new_string)

def team_name_modifier(name):
    modified_name = custom_title(name.strip())
    if modified_name == "":
        return modified_name
    if len(modified_name) < 3:
        return modified_name.upper()
    split_string = modified_name.split()
    last_word = split_string[-1]
    name_not_corrected = True
    list_last_word = list(last_word)
    cur_index = 0
    while name_not_corrected:
        if list_last_word[cur_index].isdigit():
            if not list_last_word[cur_index + 1].isdigit():
                list_last_word[cur_index + 1] = list_last_word[cur_index + 1].lower()
                correct_last_word = "".join(list_last_word)
                split_string[-1] = correct_last_word
                return " ".join(split_string)
            else:
                if cur_index < (len(list_last_word) - 2):
                    cur_index += 1
                else:
                    name_not_corrected = False
        else:
            name_not_corrected = False
    return modified_name

def player_name_modifier(name):
    if name.strip() != "":
        formatted_name = ""
        if len(name) < 3:
            formatted_name = name.strip()
        else:
            formatted_name = name.strip().title()
        split_string = formatted_name.split()
        for word in split_string:
            if word.lower() in manual_formats:
                split_string[split_string.index(word)] = manual_formats[word.lower()]
            list_word = list(word)
            if len(list_word) > 1:
                if (list_word[0] == "M") and (list_word[1] == "c"):
                    list_word[2] = list_word[2].upper()
                    corrected_word = "".join(list_word)
                    split_string[split_string.index(word)] = corrected_word
        last_word_uppercase = split_string[-1].upper()
        list_last_word = list(last_word_uppercase)
        non_roman_numeral_found = False
        for letter in list_last_word:
            if (letter != "I") and (letter != "V"):
                non_roman_numeral_found = True
        if not non_roman_numeral_found:
            split_string[-1] = last_word_uppercase
        return " ".join(split_string)
    else:
        return name

def valid_name(name, name_type):
    if name == "":
        raise ValueError(f"{name_type} cannot be empty.")
    if name.strip() == "":
        raise ValueError(f"{name_type} cannot contain only spaces.")
            
def check_for_numbers(name, name_type):
    list_name = list(name)
    for letter in list_name:
        if letter.isdigit():
            raise ValueError(f"{name_type} cannot contain any integers.")
