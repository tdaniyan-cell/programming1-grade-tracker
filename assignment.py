class Assignment:
    """Base class representing a single graded assignment."""
    def __init__(self, subject, title, score, max_score, due_date, atype):
        score = float(score)
        max_score = float(max_score)

        if score < 0:
            raise ValueError("Score canot be negative")
        if score > max_score:
            raise ValueError("Score cannot exceed max score")
        
        self.subject = subject
        self.title = title
        self.score = score
        self.max_score = max_score
        self.due_date = due_date
        self.type = atype
    def __str__(self):
        return f"[{self.type}] {self.subject} - {self.title}: {self.score}/{self.max_score} (due {self.due_date})"


if __name__ == "__main__":
    a = Assignment("Math", "Fractions HW", 85,100,"2026-10-14", "homework")
    bad= Assignment("Math", "Fractions HW", 150, 100, 2026-10-14, "homework")
print(bad)