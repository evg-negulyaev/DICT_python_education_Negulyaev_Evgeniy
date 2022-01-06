def main():
    print("HANGMAN")

    word_to_guess = "python"
    print("Guess the word: ", end="")
    word = input()
    if word_to_guess == word:
        print("You survived!")
    else:
        print("You lost!")


if __name__ == "__main__":
    main()
