def main():
    # !!!! run Python3 p6-1.py instead of jsut Python in terminal
    # open the file and r for read
    with open("Story.txt", "r") as file:
        content = file.readlines()

    # initialize the variables
    uppercase_count = 0
    lowercase_count = 0
    digits_count = 0
    spaces_count = 0
    word_count = 0
    sentence_count = 0

    # iterate the lines and the words and add to counts
    for line in content:
        if line.strip():  # Ignore empty lines
            sentence_count += 1
            words = line.split()
            word_count += len(words)

            for char in line:
                if char.isupper():
                    uppercase_count += 1
                elif char.islower():
                    lowercase_count += 1
                elif char.isdigit():
                    digits_count += 1
                elif char.isspace():
                    spaces_count += 1

    average_words_per_sentence = word_count / sentence_count

    # print everything for desired output
    print("Uppercase letters:", uppercase_count)
    print("Lowercase letters:", lowercase_count)
    print("Digits:", digits_count)
    print("Spaces:", spaces_count)
    print(f"Average number of words per line: {average_words_per_sentence:.1f}")


if __name__ == "__main__":
    main()
