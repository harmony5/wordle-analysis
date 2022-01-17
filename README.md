# Wordle analysis

Trying to crack the wordle game.

## Dataset

The dataset used for this analysis comes from [this gist](https://gist.github.com/h3xx/1976236) containing Wictionary's top 100k most common English words [for john the ripper].

This dataset was reduced to only contain words that are 5 characters long, excluding words with characters outside of the lowercase ASCII letters.

## Analysis

The provided python script is used to generate the following 3 outputs:

1. `nth_letter_by_frequency.txt`: a list containing random words formed by the nth most common letter in that position in the dataset of 5 letter words.
2. `word_by_frequency_of_nth_letter.txt`: all words in the original dataset of 5 letter words, ranked by the sum of the frequency of each letter.
3. `letter_frequency.txt`: the frequency of each letter in the dataset of 5 letter words.
