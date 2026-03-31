# Same word count tool from before. A new requirement came in:
# if a file is missing, the program should continue running
# without printing anything at all — no error message, no output
# for that file.

from pathlib import Path

path_0 = Path('report.txt')
path_1 = Path('notes.txt')
path_2 = Path('summary.txt')

files = [path_0, path_1, path_2]

def print_word_count(list):
    for path in list:
        try:
            contents = path.read_text()
        except FileNotFoundError:
            pass
        else:
            print(f"The file {path} has {len(contents.split())} words.")

print_word_count(files)