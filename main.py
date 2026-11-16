from validator import all_valid
from storage import save
from calculator import average
from reporter import show


def process_student(name, grades):
    if not all_valid(grades):
        print("Xato: baholar noto'g'ri")
        return
    save("students.txt", name, grades)
    show(name, average(grades))


process_student("Ali Valiyev", [85, 90, 78])
process_student("Vali Karimov", [85, 120, 78])
