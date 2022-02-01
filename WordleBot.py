import yaml
import matplotlib.pyplot as plt

def WordleBot(green, yellow, exclude):
    if check_input(green, yellow, exclude) == True:
        green_possible = green_search(green)
        yellow_possible = yellow_search2(yellow, green_possible)
        possible_words = remove_search(exclude, yellow_possible)
        common_letters = dict(letter_count(possible_words))
        
        Ls_common_letters = {'e': 1233,'a': 979,'r': 899,'o': 754,'t': 729,'l': 719,'i': 671,'s': 669,'n': 575,'c': 477,'u': 467,'y': 425,'d': 393,'h': 389,'p': 367,'m': 316,'g': 311,'b': 281,'f': 230,'k': 210,'w': 195,'v': 153,'z': 40,'x': 37,'q': 29,'j': 27}
        x_total, y_total = list(Ls_common_letters.keys()), Ls_common_letters.values()
        x_possible, y_possible = list(common_letters.keys()), common_letters.values()
        plt.rcParams['figure.figsize'] = [10,2]
        plt.subplot(1,2,1)
        plt.bar(x_total, y_total, color = 'purple')
        plt.locator_params(axis='y', nbins=2)
        plt.title('Most Common Letters in Solutions List')
        plt.subplot(1,2,2)
        plt.bar(x_possible, y_possible, color = 'orange')
        plt.locator_params(integer=True, axis='y', nbins=2)
        plt.title('Most Common Letters in Possible Words')
        plt.show()
        return print(f'There are {len(possible_words)} possible words: {", ".join(possible_words)}')

    else:
        return 'Input error: Correct your input values'
#WordleBot('?o?o?', 'tr', 'gemn')
