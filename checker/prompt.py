class Prompt:
    ignored = []
    lines = []
    word = None
    suggest = []
    replace_always = {}
    stop = False
    current_line = 0

    def __init__(self, lines):
        self.lines = lines

    def prompt(self, word, suggest, line):
        self.word = word
        self.suggest = suggest
        self.current_line = line
        if self.word in self.replace_always:
            return self.replace_always[self.word]
        if len(self.suggest) == 0:
            return word
        if self.word in self.ignored:
            return self.word
        print("ERROR: {0}".format(self.word))
        print("HOW ABOUT: {0}".format(self.suggest))
        status = False
        while not status and not self.stop:
            try:
                status = self.read_command()
            except EOFError:
                self.stop = True
        if self.stop:
            return None
        return self.word


    def read_command(self):
        cmd = input(">> ")
        cmd = cmd.strip()

        if cmd.isdigit():
            repl = int(cmd)
            if repl >= len(self.suggest):
                print("Not a valid index: {0}".format(repl))
                return False
            print('Replacing "{0}" with "{1}"'.format(self.word,
                self.suggest[repl]))
            self.word = self.suggest[repl]
            return True

        if len(cmd) > 0 and cmd[0] == 'R':
            if not cmd[1:].isdigit():
                print("Badly formatted command (try help)")
                return False
            repl = int(cmd[1:])
            if repl >= len(self.suggest):
                print("Not a valid index: {0}".format(repl))
                return False
            self.replace_always[self.word] = self.suggest[repl]
            self.word = self.suggest[repl]
            return True

        if cmd == 'i':
            return True

        if cmd == 'I':
            self.ignored.append(self.word)
            return True

        if cmd == 'e':
            repl = input("New Word: ")
            repl = repl.strip()
            self.word = repl
            return True

        if cmd == 'l':
            print("{0}: {1}".format(self.current_line,
                self.lines[self.current_line]))
            return False

        if len(cmd) > 0 and cmd[0] == 'L':
            if not cmd[1:].isdigit():
                print("Badly formatted command (try help)")
                return False
            repl = int(cmd[1:])
            min = self.current_line - repl
            if min < 0:
                min = 0
            max = self.current_line + repl + 1
            if max >= len(self.lines):
                max = len(self.lines)
            for line in range(min, max):
                print("{0}: {1}".format(line, self.lines[line]))
            print("----------------------------------------------------")
            print("HOW ABOUT: {0}".format(self.suggest))
            return False

        if cmd == 'q':
            self.stop = True
            return True

        if cmd == 'h':
            self.print_help()
            return False

        print("Badly formatted command (try 'help')")
        return False

    def print_help(self):
        print("0..N:    replace with the numbered suggestion")
        print("R0..rN:  always replace with the numbered suggestion")
        print("i:       ignore this word")
        print("I:       always ignore this word")
        print("e:       edit the word")
        print("l:       show current line")
        print("L0..lN   show numbered previous and next lines")
        print("q:       quit checking")
        print("h:       print this help message")
        print("----------------------------------------------------")
        print("HOW ABOUT: {0}".format(self.suggest))
