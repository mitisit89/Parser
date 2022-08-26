import itertools
import pathlib


def parcer(path_to_file: str | pathlib.Path):
    with open("./PythonTest.txt", "r", encoding="utf-8") as file, open(
        "eng.txt", "w"
    ) as eng_txt, open("ru.txt", "w") as ru_txt:
        try:
            for line in file.readlines():
                en, ru = line.strip().split("\t")
                en = (x.strip() for x in en.split(";"))
                ru = (x.strip() for x in ru.split(";"))
                for en_word, ru_word in zip(en, itertools.cycle(ru)):
                    eng_txt.writelines(f"{en_word}\n")
                    ru_txt.writelines(f"{ru_word}\n")
        except FileNotFoundError:
            print("File not found. Check the path variable and filename")
            exit()


parcer("./PythonTest.txt")
