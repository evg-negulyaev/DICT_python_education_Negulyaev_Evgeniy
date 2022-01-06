from random import randint


def hint(word):
    return word[0:3] + "-" * (len(word) - 3)


def random_word(words):
    return words[randint(0, len(words) - 1)]


def main():
    print("HANGMAN")

    words = ['python', 'java', 'javascript', 'php']
    word_to_guess = random_word(words)
    print(f"Guess the word {hint(word_to_guess)}: ", end="")
    word = input()
    if word_to_guess == word:
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
