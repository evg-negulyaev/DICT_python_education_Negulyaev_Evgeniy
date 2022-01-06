from random import randint


def hint(word, guessed_letters):
    result = ""
    for letter in word:
        if letter in guessed_letters:
            result += letter
        else:
            result += '-'
    return result


def random_word(words):
    return words[randint(0, len(words) - 1)]


def main():
    print("HANGMAN")

    words = ['python', 'java', 'javascript', 'php']
    word_to_guess = random_word(words)
    guessed_letters = set()
    for _ in range(8):
        print()
        print(hint(word_to_guess, guessed_letters))
        print("Input a letter: ", end='')
        letter = input()
        if letter in word_to_guess:
            guessed_letters.add(letter)
        else:
            print("That letter doesn't appear in the word ")
    print("Thanks for playing!")
    print("We'll see how well you did in the next stage")


if __name__ == "__main__":
    main()
