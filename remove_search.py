def remove_search(exclude, yellow_possible):
    possible_words = yellow_possible.copy()
    index = len(exclude)
    
    while index > 0:
        for word in yellow_possible:
            if exclude[index-1] in word:
                try:
                    possible_words.remove(word)
                except:
                    pass
        index -= 1
    
    return possible_words
