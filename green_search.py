def green_search(guess):
    green_list = list()
    index = 4
    qs = 0
    for letter in guess:
        if letter == '?':
            qs += 1    
    if qs == 5:
        return Ls
    else:
    	while index >= 0:
            for word in Ls:
                if guess[index] == '?': 
                    pass
                elif guess[index] in word[index]:
                    green_list.append(word)
            index -= 1
    
    green_dict = dict()
    for word in green_list:
        green_dict[word] = green_dict.get(word,0)+1
    

    sorted_green_dict = {key:val for key, val in green_dict.items() if val == (5-qs)}
    
    green_possible = list(sorted_green_dict.keys())
    return green_possible
