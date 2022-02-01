# Yellow search two works in the same format as the green_search 
# where '?' are placed in black letter spaces so the search can compare letter index to the solution word index
# making yellow letters not able to be in the smae spot

def yellow_search2(guess, green_possible):
    yellow_list = list()
    index = 4
    qs = 0
    for letter in guess:
        if letter == '?':
            qs += 1    
    if qs == 5:
        return green_possible
    else:
    	while index >= 0:
            for word in green_possible:
                if guess[index] == '?': 
                    pass
                elif guess[index] in word:
                    if guess[index] in word[index]:
                        pass
                    else:
                        yellow_list.append(word)
            index -= 1
    
    yellow_dict = dict()
    for word in yellow_list:
        yellow_dict[word] = yellow_dict.get(word,0)+1
    

    sorted_yellow_dict = {key:val for key, val in yellow_dict.items() if val == (5-qs)}
    
    yellow_possible = list(sorted_yellow_dict.keys())
    return yellow_possible
