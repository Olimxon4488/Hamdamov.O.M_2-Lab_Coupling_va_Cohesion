def is_valid_grade(g):
    return isinstance(g, int) and 0 <= g <= 100


def all_valid(grades):
    return len(grades) > 0 and all(is_valid_grade(g) for g in grades)
