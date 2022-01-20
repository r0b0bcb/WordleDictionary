def yellow_search(guess, green_possible):
    yellow_list = []
    index = len(guess)
    if len(guess) == 0:
        return green_possible
    while index > 0:
        for word in green_possible:
            if guess[index-1] in word:
                yellow_list.append(word)
        index -= 1
        
    yellow_dict = dict()
    for word in yellow_list:
        yellow_dict[word] = yellow_dict.get(word,0)+1
    sorted_yellow_dict = {key:val for key, val in yellow_dict.items() if val == len(guess)}
    
    yellow_possible = list(sorted_yellow_dict.keys())
    return yellow_possible
