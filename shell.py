import os

class pyshell:
    def __init__(self) -> None:
        self.line = ""
        self.prompt = ">"
        self.parts = []

    def loop(self):
        while 1:
            try:
                line = input(self.prompt)
                self.process(line)
            except KeyboardInterrupt:
                break

    def process(self, _input):
        self.parts = _input.lower().split(";")
        for part in self.parts:
            print(f"Executing chain: {part}")
            self.process_line(part)

    def process_line(self, line):
        parts = line.lower().split(" ")
        for part in parts:
            if part[0] == "ls":
                for file in os.listdir(parts[1]):
                    print(file)



shell = pyshell()
shell.loop()