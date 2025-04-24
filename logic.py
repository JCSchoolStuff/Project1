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
        self.__student_count = self.num_students.text().strip()
        self.__grades_list = self.student_grades.text().split(', ')
        print("Running")
        try:
            if self.__student_count == '':
                raise ValueError
            else:
                int(self.__student_count)
            for pos, grade in enumerate(self.__grades_list):
                self.__grades_list[pos] = int(grade.strip())
                if grade == '':
                    raise ValueError
            if len(self.__grades_list) != int(self.__student_count):
                raise IndexError

            self.__avg = sum(self.__grades_list) / len(self.__grades_list)
            self.__grades_list.append(self.__avg)

            self.__best_grade = max(self.__grades_list)
            self.__letter_grade = []
            for grade in self.__grades_list:
                if grade >= self.__best_grade - 10:
                    self.__letter_grade.append('A')
                elif grade >= self.__best_grade - 20:
                    self.__letter_grade.append('B')
                elif grade >= self.__best_grade - 30:
                    self.__letter_grade.append('C')
                elif grade >= self.__best_grade - 40:
                    self.__letter_grade.append('D')
                else:
                    self.__letter_grade.append('F')


            with open('students.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for student in range(int(self.__student_count)):
                    writer.writerow([student, self.__grades_list[student],self.__letter_grade[student]])
                writer.writerow(['Average', self.__avg, self.__letter_grade[len(self.__letter_grade)-1]])

            with open('students.csv', 'r', newline='') as csvfile:
                reader = csv.reader(csvfile)
                final_results = ''
                for row in reader:
                    if row[0] == 'Average':
                        final_results += f'The average score is {self.__avg:.2f}, a grade of {self.__letter_grade[len(self.__letter_grade) - 1]}'
                    else:
                        final_results += f'Student {int(row[0]) + 1} score is {row[1]} and grade is {row[2]}\n'
                self.results_label.setText(final_results)

        except TypeError:
            self.results_label.setText('Student number and grades must be integers.')
        except ValueError:
            self.results_label.setText('Cannot have empty values.')
        except IndexError:
            self.results_label.setText('There must be as many grades as students.')