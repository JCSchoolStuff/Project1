from PyQt6.QtWidgets import *
import csv

from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """
    Contains the logic for the GUI,
    Obtains class name and student scores, calculates average grade,
    writes that data to a csv file.
    """
    def __init__(self) -> None:
        """
        Initializes the GUI.
        """
        super().__init__()
        self.setupUi(self)

        self.hide_grades()

        self.class_submit.clicked.connect(lambda: self.student_submit())
        self.scores_submit.clicked.connect(lambda: self.submit())

    def hide_grades(self) -> None:
        """
        Hides the grades column.
        """
        self.student1_grade.hide()
        self.student1_label.hide()
        self.student2_grade.hide()
        self.student2_label.hide()
        self.student3_grade.hide()
        self.student3_label.hide()
        self.student4_grade.hide()
        self.student4_label.hide()
        self.student5_grade.hide()
        self.student5_label.hide()

    def student_submit(self) -> None:
        self.hide_grades()

        self.__class_name = self.class_name.text().strip()
        self.__student_count = self.num_students.text().strip()

        try:
            if self.__student_count == '':
                raise ValueError
            elif not self.__student_count.isdigit():
                raise TypeError
            else:
                self.__student_count = int(self.__student_count)

            if self.__class_name == '':
                raise ValueError

            if 1 <= self.__student_count <= 5 :
                if self.__student_count >= 1:
                    self.student1_grade.show()
                    self.student1_label.show()
                if self.__student_count >= 2:
                    self.student2_grade.show()
                    self.student2_label.show()
                if self.__student_count >= 3:
                    self.student3_grade.show()
                    self.student3_label.show()
                if self.__student_count >= 4:
                    self.student4_grade.show()
                    self.student4_label.show()
                if self.__student_count == 5:
                    self.student5_grade.show()
                    self.student5_label.show()
            else:
                raise IndexError


        except TypeError:
            self.submit_info.setStyleSheet("color: red;")
            self.submit_info.setText('Class size must be an integer.')
        except ValueError:
            self.submit_info.setStyleSheet("color: orange;")
            self.submit_info.setText('Please enter a value for both inputs.')
        except IndexError:
            self.submit_info.setStyleSheet("color: green;")
            self.submit_info.setText('Class size must be an integer from 1 to 5.')

    def submit(self) -> None:
        """
        Obtains values from GUI input,
        calculates average grade,
        writes class name, student scores, and average grade to a csv file.
        """

        self.__grade1 = self.student1_grade.text().strip()
        self.__grade2 = self.student2_grade.text().strip()
        self.__grade3 = self.student3_grade.text().strip()
        self.__grade4 = self.student4_grade.text().strip()
        self.__grade5 = self.student5_grade.text().strip()
        self.__grades_list = []
        try:
            if self.__student_count >= 1:
                if self.__grade1 == '':
                    raise ValueError
                if not self.__grade1.isdigit():
                    raise TypeError
                else:
                    self.__grades_list.append(int(self.__grade1))
            if self.__student_count >= 2:
                if self.__grade2 == '':
                    raise ValueError
                if not self.__grade2.isdigit():
                    raise TypeError
                else:
                    self.__grades_list.append(int(self.__grade2))
            if self.__student_count >= 3:
                if self.__grade3 == '':
                    raise ValueError
                if not self.__grade3.isdigit():
                    raise TypeError
                else:
                    self.__grades_list.append(int(self.__grade3))
            if self.__student_count >= 4:
                if self.__grade4 == '':
                    raise ValueError
                if not self.__grade4.isdigit():
                    raise TypeError
                else:
                    self.__grades_list.append(int(self.__grade4))
            if self.__student_count >= 5:
                if self.__grade5 == '':
                    raise ValueError
                if not self.__grade5.isdigit():
                    raise TypeError
                else:
                    self.__grades_list.append(int(self.__grade5))
            for value in self.__grades_list:
                if value < 0 or value > 100:
                    raise OverflowError

            self.__avg = sum(self.__grades_list) / len(self.__grades_list)

            self.__write_list = [self.__class_name]
            self.__write_list.extend(self.__grades_list)
            for i in range(5-len(self.__grades_list)):
                self.__write_list.append('N/A')
            self.__write_list.append(f'{self.__avg:.2f}')

            with open('students.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(self.__write_list)

            self.submit_info.setStyleSheet("color: black;")
            self.submit_info.setText('Submitted.')
        except TypeError:
            self.submit_info.setStyleSheet("color: cyan;")
            self.submit_info.setText('Grades must be integers.')
        except ValueError:
            self.submit_info.setStyleSheet("color: blue;")
            self.submit_info.setText('Cannot have empty values.')
        except OverflowError:
            self.submit_info.setStyleSheet("color: purple;")
            self.submit_info.setText('Grades must be from 0-100.')
