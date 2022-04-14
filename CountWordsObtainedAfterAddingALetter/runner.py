if __name__ == "__main__":
    word_list = ["kailyn"]
    target_word = "kailyns"

    for i in range(len(target_word)):
        new_word = target_word[:i] + target_word[i+1:]
        print(new_word)

