import io

def replace(s):
    if s == "ä":
        return "\\\"{a}"
    elif s == "Ä":
        return "\\\"{A}"
    elif s == "ö":
        return "\\\"{o}"
    elif s == "Ö":
        return "\\\"{O}"
    elif s == "ü":
        return "\\\"{u}"
    elif s == "Ü":
        return "\\\"{U}"
    elif s == "ß":
        return "{\\ss}"
    else:
        return s

if __name__ == "__main__":
    file = io.open("C:\\Info\\Projects\\UniprojektGitHub\\Doku\\Tagesdokus\\10thDay\\TagesDoku.tex", "r", encoding="utf-8")
    data = [replace(c) for line in file for c in line]
    file.close()
    with io.open("C:\\Info\\Projects\\UniprojektGitHub\\Doku\\Tagesdokus\\10thDay\\TagesDoku.tex", "w+", encoding="utf-8") as f:
        for c in data:
            f.write(c)

