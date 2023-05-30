import os

class pyshell:
    def __init__(self) -> None:
        self.line = ""
        self.prompt = ">"
        self.current_dir = os.getcwd()
        self.parts = []

    def loop(self):
        while 1:
            try:
                line = input(f"PYSHELL: {self.current_dir} >> ")
                self.process(line)
            except KeyboardInterrupt:
                break

    def run_ls(self, path):
        print(f"=== ls {path} ===")
        try:
            for file in os.listdir(path):
                print(file)
        except FileNotFoundError:
            print(f"ERROR: {path} doesnt exist.")

    def run_cat(self, file):
        print(f"=== cat {file} ===")
        try:
            with open(file,"r") as out:
                lines = out.readlines()
                for line in lines:
                    print(line)
        except FileNotFoundError:
            print(f"Pyshell: File {file} doesnt exist")

    def process(self, _input):
        self.parts = _input.lower().split(";")
        for part in self.parts:
            #print(f"Executing chain: {part}")
            self.process_line(part)

    def process_line(self, line):
        parts = line.lower().split(" ")
        if len(parts) >= 2:
            if parts[0] == "ls":
                self.run_ls(parts[1])

            elif parts[0] == "cat":
                self.run_cat(parts[1])

            elif parts[0] == "cd":
                try:
                    os.chdir(parts[1])
                    self.current_dir = os.getcwd()
                except FileNotFoundError:
                    print(f"pyshell: path doesnt exist")
        else:
            if parts[0] == "help":
                print("ls <dir>")
                print("cat <file>")
                print("cd <dir>")
            elif parts[0] == "ls":
                self.run_ls(".")
            elif parts[0] == "cat":
                print("display contents")
                print("displays the contents of a file")
            elif parts[0] == "cd":
                print("change directory")
            else:
                print(f"Unknown command {parts[0]}")




shell = pyshell()
print("pyshell v0")
shell.loop()