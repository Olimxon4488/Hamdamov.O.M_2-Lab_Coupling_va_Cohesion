def save(path, name, grades):
    with open(path, "a", encoding="utf-8") as f:
        f.write(name + ":" + ",".join(map(str, grades)) + "\n")
