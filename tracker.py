from assignment import Assignment

class GradeTracker:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def list_assignments(self):
        for a in self.assignments:
            print(a)

if __name__ == "__main__":
    from assignment import Homework, Exam

    gt = GradeTracker()
    gt.add_assignment(Homework("Math", "Fractions HW", 85, 100, "2026-10-14"))
    gt.add_assignment(Exam("Science", "Midterm", 72, 100, "2026-=10-20"))
    gt.list_assignments()
    # print(gt.assignments)