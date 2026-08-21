# ProgrammingOneFormativeAssignment
This repository contains the first assignment for Programming 1

Student Grade / Assignmet Tracker
This is a command lime program for recording hpmework and exam results, filtering asssignments and viewing grade summaries within sinle terminal session. 

Feautures
Add Assignment: Record homework or exams with subject, tiltle, score, max score and due date.

List Assignmnet: View every recorded assignmnet in a cleaan, readble format.

Filter Assignmnets: By subject, type (homework/exam), or month.

Grade Summaries: Overall average, per subject average and the highest/lowest scoring assignmnet.

Input Validation: Invalid menu choices and no numerica or out of range scores are caught and reported without crashing the program.

Extra:
   - There's also low score warning (flagging any assignment scoring below 50%)
   - Top performing subject

All data is kept in memory for the curent sessionn only , nothing is saved to disk, and the current tracker starts empty each time the program runs.


Project Structure
main.py         # Menu loop and user interaction
assignment.py   # Assignment base class, Homework and Exam subclasses
tracker.py      # GradeTracker class (add/list/filter/summarize)
README.md
reflection.pdf
screenshots/'

How to Run
Clone this repository and open it in your terminal / VS Code.
Make sure Python 3 is installed (python --version).
Run: python main.py
Follow the on screen menu

Menu Structure
===== Student Grade Tracker =====
1) Add homework
2) Add exam
3) List assignments
4) Filter (by subject / type / month)
5) Show summary
0) Exit
chosing option 4 opens a sub menu

Sample interaction
Choose an option: 1
Subject: math
Title: Fractions HW
Score: 22
Max score: 23
Due date (YYYY-MM-DD): 2026-10-14
Homework added!

Choose an option: 5
Overall average: 91.6
Per-subject averages: {'math': 91.6, 'science': 92.3}
Highest scoring: [homework] math - Fractions HW: 22.0/23.0 (due 2026-10-14)
Lowest scoring: [exam] science - Midterm: 72.0/100.0 (due 2026-10-20)

Top performing subject: science (92.3%)

Score: abc
Could not add homework: could not convert string to float: 'abc'

Class Design
Assignment:Base class holding shared attributes (subject, title, score, max_score, due_date, type)and validation logic (score must be numeric and cannot exceed max_score).

Homework and Exam : Subclasses of Assignment that call super().__init__() and hardcode their type.

GradeTracker: Owns the in-memory list of assignments and provides add_assignment, list_assignments, filter_by_type, filter_by_subject, filter_by_month, and the summary methods (overall_average, per_subject_averages, highest_scoring, lowest_scoring, low_score_warnings, top_subject).