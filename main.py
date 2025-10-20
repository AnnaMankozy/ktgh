students = {
    "Іваненко Петро Петрович": {
        "група": "П-21",
        "курс": 2,
        "предмети": {"Вища математика": 85, "Програмування": 90, "Англійська": 78, "Предмет за вибором": 90},
        "адреса": "м. Київ, вул. Хрещатик, буд. 15, кв. 2",
        "номер телефону": "+38093123456",
        "форма фінансування": "Бюджет",
        "форма навчання": "Денна"
    },
    "Коваленко Олена Ігорівна": {
        "група": "П-21",
        "курс": 2,
        "предмети": {"Вища математика": 92, "Програмування": 88, "Англійська": 84, "Предмет за вибором": 88},
        "адреса": "м. Львів, вул. Шевченка, буд. 101, кв. 12",
        "номер телефону": "+380671112233",
        "форма фінансування": "Бюджет",
        "форма навчання": "Заочна"
    },
    "Мельник Анна Сергіївна": {
        "група": "П-21",
        "курс": 2,
        "предмети": {"Вища математика": 70, "Програмування": 95, "Англійська": 68, "Предмет за вибором": 69},
        "адреса": "м. Одеса, вул. Дерибасівська, буд. 7, кв. 45",
        "номер телефону": "+380501234890",
        "форма фінансування": "Бюджет",
        "форма навчання": "Денна"
    }
} # Манько Анна

# Функція додавання нового студента - Снаговська Дарья
def add_student(database, student_name, student_group, student_course, student_subjects, student_address, student_numer_of_phone, student_form_of_financing, student_form_of_study):
    database[student_name] = {
        "група": student_group,
        "курс": student_course,
        "предмети": student_subjects,
        "адреса": student_address,
        "номер телефону": student_numer_of_phone,
        "форма фінансування": student_form_of_financing,
        "форма навчання": student_form_of_study
    }
    print(f"Студента {student_name} додано до бази даних.")

while True:
    print("\nМеню:")
    print("Вивести усіх студентів -> 1 <-")
    print("Додати нового студента -> 2 <-")
    print("Видалити студента -> 3 <-")
    print("Порахувати середній бал студента -> 4 <-")
    print("Змінити дані студента -> 5 <-")
    print("Вийти з програми -> 0 <-")

    choice = input("Введіть пункт меню: ")

    if choice == "1":
        print_students(students)

    elif choice == "2":
        name = input("Введіть ПІБ студента: ")
        group = input("Введіть групу: ")
        course = int(input("Введіть курс: "))

        # Готовий список предметів — користувач вводить лише оцінки
        default_subjects = ["Вища математика", "Програмування", "Англійська", "Предмет за вибором"]
        subjects = {}

        print("Введіть оцінки з кожного предмета:")
        for subject in default_subjects:
            while True:
                try:
                    grade = int(input(f"{subject}: "))
                    if 0 <= grade <= 100:
                        subjects[subject] = grade
                        break
                    else:
                        print("Оцінка має бути від 0 до 100.")
                except ValueError:
                    print("Введіть ціле число!")
        address=input("Введіть адресу: ")
        numer_of_phone=input("Введіть номер телефону: ")
        form_of_financing=input("Введіть форму фінансування: ")
        form_of_study=input("Введіть форму навчання: ")
        add_student(students, name, group, course, subjects, address, numer_of_phone,form_of_financing,form_of_study)

    elif choice == "3":
        name = input("Введіть ПІБ студента для видалення: ")
        delete_student(students, name)

    elif choice == "4":
        name = input("Введіть ПІБ студента: ")
        average_grade(students, name)

    elif choice == "5":
        print("Що можете змінити:")
        for key in students["Іваненко Петро Петрович"].keys():
            print(key)
        student=input("Введіть ПІБ студента, дані якого хочете змінити: ")
        subject_to_change=input("Введіть назву властивості, яку хочете змінити: ")
        change_student_details(students, subject_to_change, student)


    elif choice == "0":
        print("Вихід із програми...")
        break

    else:
        print("Невірний вибір, спробуйте ще раз!")
        print("lk")
  