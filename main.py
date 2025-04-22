from logic import *

def main() -> None:
    """
    Runs the main function of the program.
    """
    application = QApplication([])
    window = Logic()
    window.setWindowTitle("Project 1")
    window.show()
    application.exec()

if __name__ == '__main__':
    main()