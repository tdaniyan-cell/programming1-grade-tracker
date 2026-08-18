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

            homework = Homework(subject, title, score, max_score, due_date)
            tracker.add_assignment(homework)
            print("Homework added!")

        elif choice == "2":
            subject = input("Subject: ")
            title = input("Title: ")
            score = input("Score: ")
            max_score = input("Max score: ")
            due_date = input("Due date (YYYY-MM-DD): ")

            exam = Exam(subject, title, score, max_score, due_date)
            tracker.add_assignment(exam)
            print("Exam added!")

        elif choice == "3":
            tracker.list_assignments()
        
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("You choose:", choice)

if __name__ == "__main__":
    main()