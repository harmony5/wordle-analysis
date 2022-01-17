from string import ascii_lowercase
from collections import Counter


class LetterCounter:

    def __init__(self, words: list[str] | None = None) -> None:
        words = words or []
        self.__letter_counter = Counter(dict.fromkeys(ascii_lowercase, 0))
        self.__letter_rankings = dict.fromkeys(ascii_lowercase, 0)
        
        for word in words:
            self.__letter_counter.update(word)

        self.__update_rankings()
    
    @property
    def letter_counter(self) -> Counter:
        return self.__letter_counter

    def __update_rankings(self) -> None:
        # the rankings go from 1 to 26, with the most frequent letter being 1
        for i, (letter, count) in enumerate(self.__letter_counter.most_common(), start=1):
            if count > 0:
                self.__letter_rankings[letter] = i

    def update(self, letters: str) -> None:
        self.__letter_counter.update(letters)
        self.__update_rankings()
    
    def get_ranking_for_letter(self, letter: str) -> int:
        return self.__letter_rankings[letter]
    
    def most_common_letters(self, n: int | None = None) -> list[str]:
        return [letter for letter, _ in self.__letter_counter.most_common(n)]
    

with (open("5_letter_words.txt") as f,
    open("nth_letter_by_frequency.txt", "w") as f_out,
    open("word_by_frequency_of_nth_letter.txt", "w") as f_out_2,
    open("letter_frequency.txt", "w") as f_out_3):
    
    text = f.read()
    words = [w.strip() for w in text.split("\n")]
    text = text.replace("\n", "")
    general_letter_counter = Counter(text)
    

    # spam              secdfg  -> s: 1, e: 1, c: 1, d: 1, f: 1, g: 1
    # eggs              pgarao  -> p: 1, g: 1, a: a, r: 1, o: 1
    # calm              agloll  -> a: 1, g: 1, l: 3, o: 1
    # drop      ->      msmpld  -> m: 2, s: 1, p: 1, l: 1, d: 1
    # fall
    # gold
    counts = [LetterCounter() for _ in range(5)]
    for i, letters in enumerate(zip(*words, strict=True)):
        print(letters[:10])
        print(letters.count("e"), letters.count("a"), letters.count("s"))
        counts[i].update(letters)


    letter_by_frequency = zip(*[c.most_common_letters() for c in counts])
    f_out.write("\n".join(["".join(letters) for letters in letter_by_frequency]))

    word_by_frequency = sorted(words,
        key=lambda word: sum(counts[i].get_ranking_for_letter(word[i]) for i in range(5)),
    )
    f_out_2.write("\n".join(word_by_frequency))

    f_out_3.write("\n".join([f"{letter}: {count}" for letter, count in general_letter_counter.most_common()]))