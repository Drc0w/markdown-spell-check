class Sanitizer:

    word = ""
    prefix = ""
    suffix = ""

    def __init__(self, word):
        self.word = word
        while len(self.word) > 0 and self.word[0] in "*#_[]{}()`!.+-,;.?/:\\\"'":
            self.prefix += self.word[0]
            self.word = self.word[1:]
        while len(self.word) > 0 and self.word[-1] in "*#_[]{}()`!.+-,;.?/:\\\"'":
            self.suffix += self.word[-1]
            self.word = self.word[:-1]
        self.suffix = self.suffix[::-1]

    def get_word(self):
        return self.word

    def get_prefix(self):
        return self.prefix

    def get_suffix(self):
        return self.suffix
