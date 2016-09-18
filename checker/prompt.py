class Prompt:
    ignored = None
    lines = []
    word = None
    suggest = None

    


    def __init__(self, lines):
        self.ignored = []
        self.lines = lines

    def prompt(self, word, suggest):
        self.word = word
        self.suggest = suggest
        print("ERROR: {0}\nHOW ABOUT: {1}".format(self.word, self.suggest))
