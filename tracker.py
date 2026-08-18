from assignment import Assignment

class GradeTracker:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def list_assignments(self):
        for a in self.assignments:
            print(a)

    def filter_by_type(self, atype):
        return [a for a in self.assignments if a.type == atype]

    def filter_by_subject(self, subject):
        return [a for a in self.assignments if a.subject == subject]

    def filter_by_month(self, month):
            return [a for a in self.assignments if a.due_date[:7] == month]

if __name__ == "__main__":
    from assignment import Homework, Exam

    gt = GradeTracker()
    gt.add_assignment(Homework("Math", "Fractions HW", 85, 100, "2026-10-14"))
    gt.add_assignment(Exam("Science", "Midterm", 72, 100, "2026-10-20"))
    gt.add_assignment(Homework("Math", "Algebra HW", 90, 100, "2026-11-05"))

    print("--- All ---")
    gt.list_assignments()

    print("--- Only exams ---")
    for a in gt.filter_by_type("exam"):
        print(a)

    print("--- Only October ---")
    for a in gt.filter_by_month("2026-10"):
        print(a)