# WordleDictionary
## Uses your clues from PowerLanguage's Wordle game to look for words in the solutions list that fit those hints

 The app Wordle is a popular game in my circle. It's a guessing game with an unkown 5-letter word. It gives you hints after you guess a word. Yellow means you have a correct letter in the wrong spot, green means correcct letter in correct spot, and grey means the letter is not in the word. You have 6 guesses to get the correct word.
 
 This script is designed to look up 5-letter words that fit your guessed letters.


To accomplish this I need to import the scrabble dictionary that Wordle uses, remove words longer/shorter than 5 characters, and use that list to search. Searching needs a way to check characters and index of the characters... and check the word for characters not in the word

From some more research into the source code, it looks like there are two word lists: 1 with possible solutions and 1 with playable words. Obviously the goal is to find a solution, so lets just take that list.
