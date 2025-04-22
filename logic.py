from PyQt6.QtWidgets import *
import csv

from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """
    Contains the logic for the GUI,
    calculates letter grades for students and the average score,
    Writes students, scores, and letter grades to a csv file.
    """
    def __init__(self) -> None:
        """
        Initializes the GUI.
        """
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda: self.submit())

    def submit(self) -> None:
        """
        Obtains values from GUI input,
        calculates letter grades,
        writes students, scores, and letter grades to a csv file.
        """
        student_count = self.num_students.text().strip()
        grades_list = self.student_grades.text().split(', ')
        print("Running")
        try:
            if student_count == '':
                raise ValueError
            else:
                int(student_count)
            for pos, grade in enumerate(grades_list):
                grades_list[pos] = int(grade.strip())
                if grade == '':
                    raise ValueError
            if len(grades_list) != int(student_count):
                raise IndexError

            avg = sum(grades_list) / len(grades_list)
            grades_list.append(avg)

            best_grade = max(grades_list)
            letter_grade = []
            for grade in grades_list:
                if grade >= best_grade - 10:
                    letter_grade.append('A')
                elif grade >= best_grade - 20:
                    letter_grade.append('B')
                elif grade >= best_grade - 30:
                    letter_grade.append('C')
                elif grade >= best_grade - 40:
                    letter_grade.append('D')
                else:
                    letter_grade.append('F')


            with open('students.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for student in range(int(student_count)):
                    writer.writerow([student, grades_list[student],letter_grade[student]])
                writer.writerow(['Average', avg, letter_grade[len(letter_grade)-1]])

            with open('students.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                final_results = ''
                for row in reader:
                    if row[0] == 'Average':
                        final_results += f'The average score is {avg:.2f}, a grade of {letter_grade[len(letter_grade) - 1]}'
                    else:
                        final_results += f'Student {int(row[0]) + 1} score is {row[1]} and grade is {row[2]}\n'
                self.results_label.setText(final_results)

        except TypeError:
            self.results_label.setText('Student number and grades must be integers.')
        except ValueError:
            self.results_label.setText('Cannot have empty values.')
        except IndexError:
            self.results_label.setText('There must be as many grades as students.')