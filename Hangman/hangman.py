from random import randint


def random_word(words):
    return words[randint(0, len(words) - 1)]


def main():
    print("HANGMAN")

    words = ['python', 'java', 'javascript', 'php']
    word_to_guess = random_word(words)
    print("Guess the word: ", end="")
    word = input()
    if word_to_guess == word:
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
