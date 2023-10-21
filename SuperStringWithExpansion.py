def read_swe_file_stdin():
    count = int(input().strip())  # Read the first line as a number
    s = input().strip()           # Read the second line as a string
    array_data = []
    key_value_pairs = {}

    for _ in range(count):
        line = input().strip()  # Read the next 'count' lines into an array
        array_data.append(line)

    line = input().strip()
    while line:
        key, values = line.split(":")
        values = values.split(",")
        key_value_pairs[key] = values
        line = input().strip()

    return count, s, array_data, key_value_pairs

def stringExpansion(chosen_key_value_pairs, t):
    expanded_string = t
    
    for key, value in chosen_key_value_pairs.items():
        expanded_string = expanded_string.replace(key, value)
    
    return expanded_string

def checkSubstring(s,t_list):
    return all((t in s) for t in t_list)

def recursiveCombination(key_value_pairs, s, t_list, current_combination=None, i=0):
    if current_combination is None:
        current_combination = {}
    
    if i >= len(key_value_pairs):
        # Check if the expanded string is a valid substring
        expanded_list = [stringExpansion(current_combination, t) for t in t_list]
        if checkSubstring(s, expanded_list):
            return current_combination
        else:
            return {}
    
    key = list(key_value_pairs.keys())[i]
    values = key_value_pairs[key]
    
    for value in values:
        if checkSubstring(s, [value]):
            current_combination[key] = value
            result = recursiveCombination(key_value_pairs, s, t_list, current_combination, i+1)
            if result:
                return result
            else:
                # If this value doesn't lead to a solution, remove it from the combination
                del current_combination[key]
        else:
            key_value_pairs[key].remove(value)
            print(value)

    return {}


def filter_key_value_pairs(key_value_pairs, array_data):
    valid_keys = set()
    for string in array_data:
        valid_keys.update(set(string))

    filtered_key_value_pairs = {key: value for key, value in key_value_pairs.items() if key in valid_keys}
    return filtered_key_value_pairs

def superStringWithExpansion():
    count, s, array_data, key_value_pairs = read_swe_file_stdin()
    
    filtered_key_value_pairs = filter_key_value_pairs(key_value_pairs, array_data) 

    result = recursiveCombination(filtered_key_value_pairs,s,array_data)
    print(filtered_key_value_pairs)
    return result

superStringWithExpansion()




