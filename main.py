import functools
import pathlib
import re
from typing import TextIO, Union


@functools.lru_cache
def parcer(path_to_file: Union[str, pathlib.Path]):
    try:
        with open(path_to_file, "r", encoding="utf-8") as file, open(
            "eng.txt", "w"
        ) as eng_txt, open("ru.txt", "w") as ru_txt:
            words = {}
            for line in file:
                if not line.startswith("#"):
                    eng = re.sub(r"\t.*", " ", line)
                    rus = re.findall(re.compile(r"\t.*"), line)
                    words[f"{eng}"] = "".join(rus)
            for k, v in words.items():
                if re.search(";", k):
                    eng_txt.writelines(re.sub("[;\t]", "\n", k))
                    ru_txt.writelines(re.sub("[;\t]", "\n", v))
                elif re.search(";", v):
                    ru_txt.writelines(re.sub("[;\t]", "\n", v))
                    eng_txt.writelines(re.sub("[;\t]", "\n", k))
                else:
                    ru_txt.writelines(re.sub("[;\t]", "\n", v))
                    eng_txt.writelines(re.sub("[;\t]", "\n", k))

    except OSError :
        print("file not found")
    finally:
        file.close()


parcer("./PythonTest.txt")
