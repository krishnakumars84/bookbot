def get_word_count(text: str):
    if not text: 
        raise
    words = text.split()
    return len(words)

def character_counter(text: str): 
    char_counter = {}
    for c in text: 
        if not char_counter.get(c.lower(),None):
            char_counter[c.lower()] = 1
        else:
            char_counter[c.lower()]+= 1
    return char_counter

def sort_by_count(input_val):
    return input_val["count"]

def generate_sorted_report_from_dict(raw_dict: dict):
    list_of_dicts = []
    for k,v in raw_dict.items():
        list_of_dicts.append({"char": k, "count": v})
    filtered_list_of_dicts = [i for i in list_of_dicts if i["char"].isalpha()]
    filtered_list_of_dicts.sort(reverse=True, key=sort_by_count)
    return filtered_list_of_dicts
