print("Student Grade Tracker - Initializing....")
from assignment import Homework, Exam
from tracker import GradeTracker

def print_menu():
    print("\n===== Student Grade Tracker =====")
    print("1) Add homework")
    print("2) Add exam")
    print("3) List assignments")
    print("4) Filter (by subject / type / month)")
    print("5) Show summary")
    print("0) Exit")

def main():
    tracker = GradeTracker()

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            subject = input("Subject: ")
            title = input("Title: ")
            score = input("Score: ")
            max_score = input("Max score: ")
            due_date = input("Due date (YYYY-MM-DD): ")

            try:
              homework = Homework(subject, title, score, max_score, due_date)
              tracker.add_assignment(homework)
              print("Homework added!")

            except ValueError as e:
                print("Could not add homework:", e)

        elif choice == "2":
            subject = input("Subject: ")
            title = input("Title: ")
            score = input("Score: ")
            max_score = input("Max score: ")
            due_date = input("Due date (YYYY-MM-DD): ")

            try:
                exam = Exam(subject, title, score, max_score, due_date)
                tracker.add_assignment(exam)
                print("Exam added!")

            except ValueError as e:
                print("Could not add exam", e)

        elif choice == "4":
            print("Filter by: (a) subject (b) type (c) month")
            sub_choice = input("Choose: ")

            if sub_choice == "a":
                subject = input("Enter subject: ")
                results = tracker.filter_by_subject(subject)

            elif sub_choice == "b":
                atype = input("Enter type (homework/exam): ")
                results = tracker.filter_by_type(atype)

            elif sub_choice == "c":
                month = input("Enter month (YYYY-MM): ")
                results = tracker.filter_by_month(month)
            else:
                print("Invalid filter choice")
                results = []

            for a in results:
                print(a)

        elif choice == "5":
            print("Overall average:", tracker.overall_average())
            print("Per-student average:", tracker.per_subject_averages())
            print("Highest scoring:", tracker.highest_scoring())
            print("Lowest scoring:", tracker.lowest_scoring())

        elif choice == "3":
            tracker.list_assignments()
        
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("You choose:", choice)

if __name__ == "__main__":
    main()