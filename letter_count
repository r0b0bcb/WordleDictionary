import collections as c
def letter_count(possible_words):
    count_str = ""
    for word in possible_words:
        count_str = count_str +str(word)
    sum_letters = dict(sorted(c.Counter(count_str).items(), key=lambda x:x[1], reverse=True))
    return sum_letters
#letter_count(Ls)
