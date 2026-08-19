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
        return [a for a in self.assignments if a.type == atype.lower()]

    def filter_by_subject(self, subject):
        return [a for a in self.assignments if a.subject == subject.lower()]

    def filter_by_month(self, month):
            return [a for a in self.assignments if a.due_date[:7] == month]

    def overall_average(self):
        if not self.assignments:
            return None
        return sum(a.percentage for a in self.assignments) / len(self.assignments)

    def highest_scoring(self):
        if not self.assignments:
            return None
        return max(self.assignments, key=lambda a: a.percentage)

    def lowest_scoring(self):
        if not self.assignments:
            return None
        return min(self.assignments, key=lambda a: a.percentage)

    def per_subject_averages(self):
        subjects = {}
        for a in self.assignments:
            subjects.setdefault(a.subject, []).append(a.percentage)
        return {subj: sum(pcts) / len(pcts) for subj, pcts in subjects.items()}

    def low_score_warnings(self, threshold=50.0):
        return [a for a in self.assignments if a.percentage < threshold]

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

    print("--- Summary ---")
    print("Overall average:", gt.overall_average())
    print("Highest:", gt.highest_scoring())
    print("Lowest:", gt.lowest_scoring())
    print("--- Per-subject averages ---")
    print(gt.per_subject_averages())