
class WordCount():
    word_length = ''
    word = ''


    def __init__(self,word):
        self.word = word


    def word_count(self,word):
        self.word_length = self.word.split()
        self.word_length = len(self.word_length)
        return print("Total Number of Words in Text:" + " " + str(self.word_length))

    def decision(self):
        print("\nPlease press \"1\" if you would like to stop this program or \"2\" to continue")
        self.select = input()

        return self.select

def main():
    while True:

        word = input("Please input Text:" +" ")
        obj = WordCount(word)
        obj.word_count(word)
        select = obj.decision()

        if select == 1:
            continue

        else:
            break


if __name__ == "__main__":
    main()



