import sqlite3 as sql
import sys
import objects as obj

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit, QLabel, QRadioButton, QMessageBox, \
    QComboBox, QToolBox

import pandas as pd


# print section Registration for student
class PrintSectionWindow(QMainWindow):
    def __init__(self, record):
        super().__init__()

        self.record = record
        self.setWindowTitle("Print Semester Registration")
        self.setGeometry(30, 30, 400, 400)

        #Enrolled label
        self.enrolled_label= QLabel(self)
        self.enrolled_label.setText("Enrolled Student")
        self.enrolled_label.resize(200, 30)
        self.enrolled_label.move(10, 10)

        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        students = self.record.print_class_list(curs)
        self.enrolled = []

        self.names = []
        self.lookup_buttons = []

        x = 10
        y = 50
        for i in range(len(students)):
            self.names.append(QLabel(self))
            nextButton = QPushButton(self)

            self.names[i].setText(students[i][1])
            nextButton.setText("Lookup")
            self.enrolled.append(obj.Student([students[i][0]]))
            nextButton.clicked.connect(lambda:self.build_lookup(nextButton))

            self.lookup_buttons.append(nextButton)

            self.names[i].move(x, y)
            self.lookup_buttons[i].move(x + 280, y)
            y += 30

        # Remove Flag Button
        self.remove_flag_button =QPushButton(self)
        self.remove_flag_button.setText("Remove Flag")
        self.remove_flag_button.resize(150,30)
        self.remove_flag_button.move(10, 350)

        # cancel Button
        self.cancel_button = QPushButton(self)
        self.cancel_button.setText("Cancel")
        self.cancel_button.move(300,350)
        self.cancel_button.clicked.connect(self.exit)

    def remove_flag(self):
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        self.record.approve_flags(curs, conn)
        conn.close()

    def build_lookup(self, button):
        index = self.lookup_buttons.index(button)
        self.lookup = LookupWindow(self.enrolled[index])
        self.lookup.show()

    def exit(self):
        self.close()

class courseEnrollWindow(QMainWindow):
    def __init__(self, record, action):
        super().__init__()
        self.action = action
        self.record = record

        self.setGeometry(20, 20, 300, 230)

        # Adds Faculty ID Label
        self.add_idLabel = QLabel(self)
        self.add_idLabel.setText("ID:")
        self.add_idLabel.move(10, 5)
        self.id = QLabel(self)
        self.id.setText(self.record.ID)
        self.id.move(45, 5)

        # Adds Faculty Name Label
        self.add_name_Label = QLabel(self)
        self.add_name_Label.setText("Name:")
        self.add_name_Label.move(10, 30)
        self.name = QLabel(self)
        self.name.setText(self.record.name)
        self.name.move(55, 30)

        # Adds Course ID Label
        self.add_course_Id = QLabel(self)
        self.add_course_Id.setText("Course ID:")
        self.add_course_Id.move(10, 80)

        # Input Course ID Input
        self.modifyCourseId = QLineEdit(self)
        self.modifyCourseId.move(80, 80)

        # Adds Section
        self.add_sectionNum = QLabel(self)
        self.add_sectionNum.setText("Section:")
        self.add_sectionNum.move(10, 125)

        # Input Section Input
        self.modifyFacSection = QLineEdit(self)
        self.modifyFacSection.move(80, 125)

        # Confirm Change Button (Will add/remove base on self.action)
        self.confirm_change_button = QPushButton(self)
        self.confirm_change_button.resize(120, 30)
        self.confirm_change_button.move(10, 175)
        self.confirm_change_button.clicked.connect(self.finalize)
        if self.action:
            # Sets Title
            self.setWindowTitle("Add Course")
            # Set button text
            self.confirm_change_button.setText("Add")
        else:
            # Sets Title
            self.setWindowTitle("Remove Course")
            # Set button text
            self.confirm_change_button.setText("Remove")
            
        #Cancel Faculty Button
        self.cancel_Action = QPushButton(self)
        self.cancel_Action.setText("Cancel")
        self.cancel_Action.resize(120,30)
        self.cancel_Action.move(175, 175)
        self.cancel_Action.clicked.connect(self.exit)

    def finalize(self):
        sectionID = self.modifyFacSection.text()
        courseID = self.modifyCourseId.text()

        parts=courseID.split("-")
        course_section_ID = parts[0] + parts[1] + "-" +sectionID

        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        if self.action:
            self.record.add_course(course_section_ID, curs, conn)
        else:
            self.record.remove_course(course_section_ID, curs, conn)
        conn.close()

    def exit(self):
        self.close()

class ReviewWindow(QMainWindow):
    def __init__(self, record):
        super().__init__()
        self.record = record
        self.setWindowTitle("Registration Info")
        self.setGeometry(30,30,500,400)


       # setting Id label
        self.id = QLabel(self)
        self.id_label = QLabel(self)
        self.id_label.setText("ID")
        self.id_label.move(2, 10)
        self.id.setText(self.record.ID)
        self.id.move(50, 10)

        #setting Name Label
        self.name_label = QLabel(self)
        self.name_label.setText("Name")
        self.name_label.move(2, 30)
        self.name = QLabel(self)
        self.name.setText(self.record.name)
        self.name.move(50, 30)

        # create lists of each data point for student courses to display info
        self.ids = [QLabel(self)]
        self.descriptions = [QLabel(self)]
        self.sections = [QLabel(self)]
        self.capacities = [QLabel(self)]
        self.credits = [QLabel(self)]
        self.flags = [QLabel(self)]

        # populate label lists with headers
        self.ids[0].setText("ID")
        self.descriptions[0].setText("Description")
        self.sections[0].setText("Section")
        self.capacities[0].setText("Capacity")
        self.credits[0].setText("Credits")
        self.flags[0].setText("Flag")

        height = 75
        # Move label headers to appropriate location
        self.ids[0].move(5, height)
        self.descriptions[0].move(100, height)
        self.sections[0].move(325, height)
        self.capacities[0].move(375, height)
        self.credits[0].move(425, height)
        self.flags[0].move(475, height)

        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        self.db_sections = self.record.print_registration(curs)

        for i in range(len(self.db_sections)):
            self.ids.append(QLabel(self))
            self.descriptions.append(QLabel(self))
            self.sections.append(QLabel(self))
            self.capacities.append(QLabel(self))
            self.credits.append(QLabel(self))
            self.flags.append(QLabel(self))

            # populate data
            self.ids[i+1].setText(self.db_sections[i][0])
            self.descriptions[i+1].setText(self.db_sections[i][1])
            self.sections[i+1].setText(str(self.db_sections[i][2]))
            self.capacities[i+1].setText(str(self.db_sections[i][3]))
            self.credits[i+1].setText(str(self.db_sections[i][4]))
            self.flags[i+1].setText(str(self.db_sections[i][5]))

            height += 25
            # Move data to appropriate location
            self.ids[i+1].move(5, height)
            self.descriptions[i+1].move(100, height)
            self.descriptions[i+1].resize(225, 30) # Specifically resize this field as it's long and gets truncated
            self.sections[i+1].move(325, height)
            self.capacities[i+1].move(375, height)
            self.credits[i+1].move(425, height)
            self.flags[i+1].move(475, height)

        # Remove Flag Button
        self.removeflag = QPushButton(self)
        self.removeflag.setText("Remove Flag")
        self.removeflag.resize(120, 30)
        self.removeflag.move(10, 350)
        self.removeflag.clicked.connect(self.remove_flag)

        # Remove Course Button
        self.removecourse = QPushButton(self)
        self.removecourse.setText("Remove Course")
        self.removecourse.resize(120, 30)
        self.removecourse.move(130, 350)
        self.removecourse.clicked.connect(self.remove_course)

        # Cancel Button
        self.cancel = QPushButton(self)
        self.cancel.setText("Cancel")
        self.cancel.resize(120, 30)
        self.cancel.move(375, 350)
        self.cancel.clicked.connect(self.exit)

    def remove_flag(self):
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        self.record.approve_flags(curs, conn)
        conn.close()

    def remove_course(self):
        self.rem_crs_win = courseEnrollWindow(self.record, False)
        self.rem_crs_win.show()

    def exit(self):
        self.close()


class ModifyWindow(QMainWindow):
    def __init__(self, record):
        super().__init__()
        self.record = record

        self.setWindowTitle("Modify window")
        self.setGeometry(20, 20, 300, 300)

         # modify label
        self.id_modify_label = QLabel(self)
        self.id_modify_label.setText("ID")
        self.id_modify_label.move(20, 30)

        # modify label
        self.name_modify_label = QLabel(self)
        self.name_modify_label.setText("Name")
        self.name_modify_label.move(20, 100)

        # modify text Field
        self.modifyId = QLineEdit(self)
        self.modifyId.move(70, 30)
        self.modifyName = QLineEdit(self)
        self.modifyName.move(70, 100)

        #Uptdate_Button
        self.update_button= QPushButton(self)
        self.update_button.setText("Update")
        self.update_button.resize(100, 30)
        self.update_button.move(20, 250)
        self.update_button.clicked.connect(self.finalize)

        #Done_Button
        self.done_button = QPushButton(self)
        self.done_button.setText("Done")
        self.done_button.resize(70, 30)
        self.done_button.move(230, 250)
        self.done_button.clicked.connect(self.done_exit)

    def finalize(self):
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        name = self.modifyName.text()
        # Pulls the data entered into the name field to update the record's information
        self.record.modify(name, curs, conn)

    def done_exit(self):
        choice = QMessageBox.question(self, 'Extract!', "Are you sure ?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.close()
        else:
            pass


class CourseAddWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Course")
        # Entry field for id
        self.id_label = QLabel(self)
        self.id_field = QLineEdit(self)
        # Entry field for description
        self.description_label = QLabel(self)
        self.description_field = QLineEdit(self)
        # Entry field for section id
        self.section_label = QLabel(self)
        self.section_field = QLineEdit(self)
        # Entry field for credits
        self.credits_label = QLabel(self)
        self.credits_field = QLineEdit(self)
        # Entry field for capacity
        self.capacity_label = QLabel(self)
        self.capacity_field = QLineEdit(self)
        # Entry field for semester
        self.semester_label = QLabel(self)
        self.semester_field = QLineEdit(self)

        self.done_button = QPushButton(self)
        self.cancel_button = QPushButton(self)

        self.setup_ui()

    def setup_ui(self):
        self.setGeometry(20, 20, 500, 250)

        self.id_label.setText("ID:")
        self.id_label.resize(100, 30)
        self.id_label.move(20, 10)
        self.id_field.resize(250, 20)
        self.id_field.move(100, 10)

        self.description_label.setText("Description:")
        self.description_label.resize(100, 30)
        self.description_label.move(20, 40)
        self.description_field.resize(250, 20)
        self.description_field.move(100, 40)

        self.credits_label.setText("Credits:")
        self.credits_label.resize(100, 30)
        self.credits_label.move(20, 70)
        self.credits_field.resize(250, 20)
        self.credits_field.move(100, 70)

        self.section_label.setText("Section:")
        self.section_label.resize(100, 30)
        self.section_label.move(20, 100)
        self.section_field.resize(250, 20)
        self.section_field.move(100, 100)

        self.capacity_label.setText("Capacity:")
        self.capacity_label.resize(100, 30)
        self.capacity_label.move(20, 130)
        self.capacity_field.resize(250, 20)
        self.capacity_field.move(100, 130)

        self.semester_label.setText("Semester:")
        self.semester_label.resize(100, 30)
        self.semester_label.move(20, 160)
        self.semester_field.resize(250, 20)
        self.semester_field.move(100, 160)

        self.done_button.setText("Done")
        self.done_button.move(20, 200)
        self.done_button.clicked.connect(self.add_to_db)

        self.cancel_button.setText("Cancel")
        self.cancel_button.move(380, 200)
        self.cancel_button.clicked.connect(self.exit)

    def add_to_db(self):
        # Starts by creating a connection and cursor to work with
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()

        # Pulls data from fields to create objects later
        course_id = self.id_field.text()
        course_desc = self.description_field.text()
        section_id = self.section_field.text()
        course_credits = self.credits_field.text()
        section_capacity = self.capacity_field.text()
        section_semester = self.semester_field.text()

        # Course_Section_ID is constructed separately,
        # as the user is not expected to concatenate them
        parts = course_id.split("-")
        course_section_id = parts[0] + parts[1] + "-" + section_id

        if section_id != "":
            section = obj.Section([course_section_id, course_id, "00000000",
                                   section_id, section_capacity, section_semester])
            section.add(curs, conn)
        elif course_id != "":
            course = obj.Course([course_id, course_desc, course_credits])
            course.add(curs, conn)

        conn.close()

    def exit(self):
        self.close()

class LookupWindow(QMainWindow):
    def __init__(self, record):
        super().__init__()
        self.record = record

        self.remove_record_button = QPushButton(self)
        self.remove_record_button.resize(150, 30)
        self.remove_record_button.move(20, 350)
        self.remove_record_button.clicked.connect(self.remove_record)

        if type(record) == obj.Student:
            self.setup_student_ui()
        elif type(record) == obj.Faculty:
            self.setup_faculty_ui()
        elif type(record) == obj.Course:
            self.setup_course_ui()
        elif type(record) == obj.Section:
            self.setup_section_ui()

    def setup_student_ui(self):
        self.setWindowTitle("Student Lookup")

        # StudentId
        self.student_label = QLabel(self)
        self.studentId = QLabel(self)
        # student Enrolled
        self.student_enrolled_label = QLabel(self)
        self.studentEnrolled = QLabel(self)

        # student credits
        self.student_credits_label = QLabel(self)
        self.studentCredits = QLabel(self)

        # Student Name
        self.student_name_label = QLabel(self)
        self.studentName = QLabel(self)

        # studentButton
        self.add_course_button = QPushButton(self)
        self.review = QPushButton(self)
        self.review.clicked.connect(self.reviewWindow)
        self.remove_course_button = QPushButton(self)
        self.modify_student = QPushButton(self)
        self.print_semester = QPushButton(self)
        self.print_semester.clicked.connect(self.reviewWindow)
        self.done = QPushButton(self)
        self.cancel = QPushButton(self)

        self.setGeometry(20, 20, 500, 500)
        # StudentId
        self.student_label.setText("ID:")
        self.student_label.resize(100, 30)
        self.student_label.move(20, 10)
        self.studentId.setText(self.record.ID)
        self.studentId.resize(150, 20)
        self.studentId.move(75, 20)

        # student Name
        self.student_name_label.setText("Name:")
        self.student_name_label.resize(100, 30)
        self.student_name_label.move(20, 55)
        self.studentName.setText(self.record.name)
        self.studentName.resize(150, 20)
        self.studentName.move(75, 60)
        # student enrolled
        self.student_enrolled_label.setText("Enrolled:")
        self.student_enrolled_label.resize(150,30)
        self.student_enrolled_label.move(20,95)
        self.studentEnrolled.resize(150,20)
        self.studentEnrolled.move(75,100)

        # student Credits
        self.student_credits_label.setText("Credits:")
        self.student_credits_label.resize(150,20)
        self.student_credits_label.move(20,150)
        self.studentCredits.setText(str(self.record.credits))
        self.studentCredits.resize(150,20)
        self.studentCredits.move(75,150)


        # student AddButton
        self.add_course_button.setText("Add Course")
        self.add_course_button.move(20, 200)
        self.add_course_button.clicked.connect(self.add_course)
        # student review
        self.review.setText("Review")
        self.review.move(370,150)
        # student RemoveCourseButton
        self.remove_course_button.setText("Remove Course")
        self.remove_course_button.resize(150, 30)
        self.remove_course_button.move(20, 250)
        self.remove_course_button.clicked.connect(self.remove_course)

        # student ModifyButton
        self.modify_student.setText("Modify Student")
        self.modify_student.resize(150, 30)
        self.modify_student.move(20,300)
        self.modify_student.clicked.connect(self.modifyWindow)

        # student Remove Student Button
        self.remove_record_button.setText("Remove Student")

        # Print Semester Registration
        self.print_semester.setText("Print Semester Registration")
        self.print_semester.resize(300,30)
        self.print_semester.move(20,400)



        # student doneButton
        self.done.setText("Done")
        self.done.move(20, 450)
        self.done.clicked.connect(self.done_exit)

        # student cancelButton
        self.cancel.setText("Cancel")
        self.cancel.resize(100, 30)
        self.cancel.move(270, 450)
        self.cancel.clicked.connect(self.done_exit)


   # print Semester Registration
    def printSection(self):
        self.open_newWindow = PrintSectionWindow(self.record)
        self.open_newWindow.show()
        # Review Window
    def reviewWindow(self):
            self.open_newWindow = ReviewWindow(self.record)
            self.open_newWindow.show()

    def setup_faculty_ui(self):
        self.setWindowTitle("Faculty Lookup")

        # facultyId
        self.faculty_label = QLabel(self)
        self.facultyId = QLabel(self)

        # facultyName
        self.faculty_name_label = QLabel(self)
        self.facultyName = QLabel(self)
        # facultyButton
        self.add_course_button = QPushButton(self)
        self.remove_course_button = QPushButton(self)
        self.done = QPushButton(self)
        self.cancel = QPushButton(self)
        self.modify_Faculty= QPushButton(self)

        self.setGeometry(20, 20, 500, 500)
        # facultyId
        self.faculty_label.setText("ID")
        self.faculty_label.resize(100, 30)
        self.faculty_label.move(20, 10)
        self.facultyId.setText(self.record.ID)
        self.facultyId.resize(150,20)
        self.facultyId.move(67,20)

        # faculty Name
        self.faculty_name_label.setText("Name")
        self.faculty_name_label.resize(100,30)
        self.faculty_name_label.move(20,55)
        self.facultyName.setText(self.record.name)
        self.facultyName.resize(150,20)
        self.facultyName.move(67,60)

        # faculty AddButton
        self.add_course_button.setText("Add Course")
        self.add_course_button.move(20,100)
        self.add_course_button.clicked.connect(self.add_course)

        # faculty RemoveCourseButton
        self.remove_course_button.setText("Remove Course")
        self.remove_course_button.resize(150,30)
        self.remove_course_button.move(20,150)
        self.remove_course_button.clicked.connect(self.remove_course)
        # faculty RemoveFacultyButton
        self.remove_record_button.setText("Remove Faculty")
        self.remove_record_button.move(20, 200)

        # modify Faculty_Button
        self.modify_Faculty.setText("Modify Faculty")
        self.modify_Faculty.resize(150,30)
        self.modify_Faculty.move(20,300)
        self.modify_Faculty.clicked.connect(self.modifyWindow)

        # faculty doneButton
        self.done.setText("Done")
        self.done.move(20,350)
        self.done.clicked.connect(self.done_exit)

        # faculty cancelButton
        self.cancel.setText("Cancel")
        self.cancel.resize(100,30)
        self.cancel.move(270, 350)
        self.cancel.clicked.connect(self.done_exit)

    def setup_course_ui(self):
        self.setWindowTitle("Course Lookup")

        # courseId
        self.course_label = QLabel(self)
        self.courseId = QLabel(self)

        # courseDescription
        self.course_description_label = QLabel(self)
        self.courseDescription = QLabel(self)

        # courseCredits
        self.course_credits_label = QLabel(self)
        self.courseCredits = QLabel(self)

        # courseButton
        self.done = QPushButton(self)
        self.cancel = QPushButton(self)

        self.setGeometry(20, 20, 400, 400)
        # courseId
        self.course_label.setText("ID")
        self.course_label.resize(100, 30)
        self.course_label.move(20, 10)
        self.courseId.setText(self.record.course_ID)
        self.courseId.resize(150, 20)
        self.courseId.move(100, 20)

        # course Description
        self.course_description_label.setText("Description:")
        self.course_description_label.resize(150, 30)
        self.course_description_label.move(20, 45)
        self.courseDescription.setText(self.record.name)
        self.courseDescription.resize(150, 20)
        self.courseDescription.move(100, 50)

        self.course_credits_label.setText("Credits:")
        self.course_credits_label.resize(100, 30)
        self.course_credits_label.move(20, 95)
        self.courseCredits.setText(str(self.record.credits))
        self.courseCredits.resize(150, 20)
        self.courseCredits.move(100, 100)

        # course RemoveCourseButton
        self.remove_record_button.setText("Remove Course")
        self.remove_record_button.move(20, 150)

        # course doneButton
        self.done.setText("Done")
        self.done.move(20, 350)
        self.done.clicked.connect(self.done_exit)

        # course cancelButton
        self.cancel.setText("Cancel")
        self.cancel.resize(100, 30)
        self.cancel.move(270, 350)
        self.cancel.clicked.connect(self.done_exit)


    def setup_section_ui(self):
        course = obj.Course([self.record.course_ID])
        self.setWindowTitle("Course Section Lookup")

        # SectionId
        self.section_id_label = QLabel(self)
        self.sectionId = QLabel(self)

        # section Description
        self.section_description_label = QLabel(self)
        self.sectionDescription = QLabel(self)

        # section
        self.section_name_label = QLabel(self)
        self.sectionName = QLabel(self)

        # section credits
        self.section_credits_label = QLabel(self)
        self.sectionCredits = QLabel(self)

        # section capacity
        self.section_capacity_label = QLabel(self)
        self.sectionCapacity = QLabel(self)

        # section semester
        self.section_semester_label = QLabel(self)
        self.sectionSemester = QLabel(self)


        # section Button
        self.review = QPushButton(self)
        self.print_semester = QPushButton(self)
        self.done = QPushButton(self)
        self.cancel = QPushButton(self)

        self.setGeometry(20, 20, 600, 600)
        # SectionId
        self.section_id_label.setText("ID:")
        self.section_id_label.resize(100, 30)
        self.section_id_label.move(20, 10)
        self.sectionId.setText(str(self.record.section_ID))
        self.sectionId.resize(150, 20)
        self.sectionId.move(100, 20)

        # section Description
        self.section_description_label.setText("Description:")
        self.section_description_label.resize(100, 30)
        self.section_description_label.move(20, 55)
        self.sectionDescription.setText(course.name)
        self.sectionDescription.resize(150, 20)
        self.sectionDescription.move(100, 60)

        # section
        self.section_name_label.setText("Section:")
        self.section_name_label.resize(150, 30)
        self.section_name_label.move(20, 95)
        self.sectionName.setText("00" + str(self.record.section_ID))
        self.sectionName.resize(150, 20)
        self.sectionName.move(100, 100)

        # section Credits
        self.section_credits_label.setText("Credits:")
        self.section_credits_label.resize(150, 20)
        self.section_credits_label.move(20, 150)
        self.sectionCredits.setText(str(course.credits))
        self.sectionCredits.resize(150, 20)
        self.sectionCredits.move(100, 150)


        # section Capacity
        self.section_capacity_label.setText("Capacity:")
        self.section_capacity_label.resize(150, 20)
        self.section_capacity_label.move(20, 250)

        # Creates a connection on the spot to capture the number of currently enrolled students in the course.
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        self.sectionCapacity.setText(str(len(self.record.print_class_list(curs))) + "/" + str(self.record.capacity))
        conn.close()
        self.sectionCapacity.resize(150, 20)
        self.sectionCapacity.move(100, 250)

        # section Semester
        self.section_semester_label.setText("Semester:")
        self.section_semester_label.resize(150, 20)
        self.section_semester_label.move(20,300)
        self.sectionSemester.setText(self.record.semester)
        self.sectionSemester.resize(150, 20)
        self.sectionSemester.move(100, 300)

        # section review
        self.review.setText("Review")
        self.review.move(450, 250)
        self.review.clicked.connect(self.printSection)
        # section Remove
        self.remove_record_button.setText("Remove section")

        # Print Semester Registration
        self.print_semester.setText("Print Semester Registration")
        self.print_semester.resize(300, 30)
        self.print_semester.move(20, 500)
        self.print_semester.clicked.connect(self.printSection)

        # student doneButton
        self.done.setText("Done")
        self.done.move(20, 550)
        self.done.clicked.connect(self.done_exit)

        # student cancelButton
        self.cancel.setText("Cancel")
        self.cancel.resize(100, 30)
        self.cancel.move(450, 550)
        self.cancel.clicked.connect(self.exit)

    #modify Window
    def modifyWindow(self):
            self.open_newWindow = ModifyWindow(self.record)
            self.open_newWindow.show()

    # Removes the supplied record from the database, if possible
    def remove_record(self):
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        if self.record.remove(curs, conn):
            conn.close()
            self.close()
        else:
            print(type(self.record), "could not be deleted")

    # These two methods open the same type of window.
    # If passed true, the window will have a button to add
    # a course. If passed false, it will remove a course.
    # These windows are meant for students and faculty.
    def add_course(self):
        self.add_crs_win = courseEnrollWindow(self.record, True)
        self.add_crs_win.show()

    def remove_course(self):
        self.rem_crs_win = courseEnrollWindow(self.record, False)
        self.rem_crs_win.show()


    # Review Window
    def reviewWindow(self):
            self.open_newWindow = ReviewWindow(self.record)
            self.open_newWindow.show()

    def done_exit(self):
        choice = QMessageBox.question(self, 'Extract!', "Are you sure ?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.close()
        else:
            pass

    def exit(self):
        self.close()

class MainWindow(QMainWindow):
    def __init__(self, conn: sql.Connection, curs: sql.Cursor):
        super().__init__()
        # Labels
        self.title = 'Database'
        # creating a textfield label
        self.studentID_Label = QLabel(self)
        # creating a box to enter student Id
        self.studentID = QLineEdit(self)
        # creating a student Name Label
        self.studentName_label = QLabel(self)
        # creating a box to enter student name
        self.studentName = QLineEdit(self)

        # creating add button label
        self.add_button = QPushButton(self)

        # lookupButton
        self.lookup_button = QPushButton(self)

        # Done Button
        self.done_button = QPushButton(self)

        # This is the Error contain message if the add doesn't exist
        self.id_error = QMessageBox(self)
        self.id_error.setWindowTitle("invalid ID error")
        self.id_error.setText(" Invalid student ID. Please try again")
        # dropdown
        self.box = QComboBox(self)
        # Database tools
        self.cursor = curs
        self.connection = conn

        # setting gui
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Main Database Window")
        self.setGeometry(30, 30, 475, 250)

        # student Id field
        self.studentID_Label.setText("ID:")
        self.studentID_Label.move(30, 80)
        self.studentID_Label.resize(75, 30)
        self.studentID.move(100, 80)
        self.studentID.resize(250, 30)

        # student name field
        self.studentName_label.setText("Name:")
        self.studentName_label.move(30, 120)
        self.studentName_label.resize(75, 30)
        self.studentName.move(100, 120)
        self.studentName.resize(250, 30)

        # will show our add button inside Main Window
        self.add_button.resize(70, 30)
        self.add_button.move(20, 200)
        self.add_button.setText('Add')
        self.add_button.clicked.connect(self.add_record)

        # LookUp Button
        self.lookup_button.resize(100, 30)
        self.lookup_button.move(100, 200)
        self.lookup_button.setText('Lookup')
        self.lookup_button.clicked.connect(self.build_lookup)

        # Done Button
        self.done_button.resize(100, 30)
        self.done_button.move(350, 200)
        self.done_button.setText("Done")
        self.done_button.clicked.connect(self.done_exit)

        # dropDown
        # self.box.resize(100,50)
        self.box.move(30, 10)
        self.box.addItem("Student")
        self.box.addItem("Course")
        self.box.addItem("Faculty")
        self.box.addItem("Section")
        self.box.currentIndexChanged.connect(self.update_labels)

        # show on the display
        self.show()

    # Changes main window labels to match the required data for the
    # newly selected record type.
    def update_labels(self):
        if self.box.currentText() == "Student" or self.box.currentText() == "Faculty":
            self.studentID_Label.setText("ID:")
            self.studentName_label.setText("Name:")
        elif self.box.currentText() == "Course" or self.box.currentText() == "Section":
            self.studentID_Label.setText("Course ID:")
            self.studentName_label.setText("Section ID:")

    def done_exit(self):
        choice = QMessageBox.question(self, 'Extract!', "Are you sure ?",
                              QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            print("Ok have a good day!")
            self.close()
        else:
            pass

    # OnClick method for the lookup button
    # Pulls record type from the dropdown, then creates
    # the corresponding type of record by pulling its
    # ID from the ID entry. That record is then passed
    # to a new lookup menu object.
    def build_lookup(self):
        record_type = self.box.currentText()
        record = None
        if record_type == "Student":
            record = obj.Student([self.studentID.text(), self.studentName.text()])
        elif record_type == "Faculty":
            record = obj.Faculty([self.studentID.text(), self.studentName.text()])
        elif record_type == "Course":
            record = obj.Course([self.studentID.text()])
        elif record_type == "Section":
            course_id = self.studentID.text()
            section_id = self.studentName.text()
            parts = course_id.split("-")
            course_section_id = parts[0] + parts[1] + "-" + section_id
            record = obj.Section([course_section_id])

        self.lookup = LookupWindow(record)
        self.lookup.show()

    # Checks the record type specified by the dropdown.
    # For student and faculty, it will create an object
    # of that type and call its add method to add it to
    # the database. For course and section, it will create
    # a course add window to capture more fields.
    def add_record(self):
        conn = sql.connect("NorthStarRegistrationDB.db")
        curs = conn.cursor()
        if self.box.currentText() == "Student":
            s = obj.Student([self.studentID.text(), self.studentName.text()])
            s.add(curs, conn)
        elif self.box.currentText() == "Faculty":
            f = obj.Faculty([self.studentID.text(), self.studentName.text()])
            f.add(curs, conn)
        elif self.box.currentText() == "Course" or self.box.currentText() == "Section":
            self.course_add = CourseAddWindow()
            self.course_add.show()
        conn.close()
