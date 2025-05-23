def get_num_words(filepath):
    with open(filepath) as f:
        return count_words(f.read())

def count_words(content):
    return len(content.split())

def get_char_map(filepath):
    with open(filepath) as f:
        return count_characters(f.read().lower())

def count_characters(content):
    char_counts = {}
    for char in content:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts  
    
def sort_on(dict):
    return dict["num"]
    
def get_ind_dicts(char_map):
    res = []
    for item in char_map:
        tmp_dict = {}
        tmp_dict["char"] = item
        tmp_dict["num"]  = char_map[item]
        res.append(tmp_dict)
    res.sort(reverse=True, key=sort_on)
    return res
        
        
        
    