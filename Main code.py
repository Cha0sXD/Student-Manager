#Person Class
class Person():
    password = "admin123"
    student_file = "/Users/anupsingh/Documents/Codes/Student-Manager/student.txt"
    teacher_file = "/Users/anupsingh/Documents/Codes/Student-Manager/teachers.txt"
    def __init__(self,file,identidication):
        self.file = file
        self.identification = identidication
    @staticmethod
    def confirm_exit():
        confirm = input("Are You Sure? y/n : ")
        if confirm == "y":
            return 0
        else:
            return 1

    def finding(self):
        try:
            id = int(self.identification)
            with open(self.file,"r") as f:
                data = True
                line = 1
                found_line = None
                while data:
                    data = f.readline()
                    if data == "\n":
                        line = line + 1
                        continue
                    data = data.strip()
                    if data == "":
                        return 0
                    part1 = data.split(", ")
                    if int(part1[0]) == id:
                        found_line = line
                        return found_line, part1
                    line = line + 1
        except ValueError:
            print("\nOnly Numerical Value Admitted")

    def view_profile(self,part1):
        self.part = part1
        print("\nName          - ",part1[1])
        print("Student ID    - ",part1[0])
        print("Course        - ",part1[2])
        print("Semester      - ",part1[3])
        print("Average Marks - ",part1[4])
        print("Attendance    - ",part1[5])
        print("Grade         - ",part1[6])
    
    @staticmethod
    def view_list():
        with open(Person.student_file,"r") as f:
            data = True
            while data:
                data = f.readline()
                print(data)

    def update_stuff(self,update_marks,update_attendance,found_line):
        self.found = found_line
        if update_marks is not None:
            try:
                update_marks = int(update_marks)
                if 0 <= update_marks <= 100:
                    with open(self.file,"r") as f:
                        data = f.readlines()
                        with open(self.file,"w") as f:
                            old_data = data[found_line-1]
                            old_data = old_data.strip()
                            new_data = old_data.split(", ")
                            new_data[4] = update_marks
                            replace_data = f"{new_data[0]}, {new_data[1]}, {new_data[2]}, {new_data[3]}, {new_data[4]}, {new_data[5]}, {new_data[6]}\n"
                            data[found_line-1] = replace_data
                            f.writelines(data)
                            print("\nData Updated Successfully")
                else:
                    print("Marks Must be between 0-100")
                    teacher_dash()
            except ValueError:
                print("Enter a Numerical Value")
        if update_attendance is not None:
            try:
                update_attendance = int(update_attendance)
                if 0 <= update_attendance <= 100:
                    with open(self.file,"r") as f:
                        data = f.readlines()
                        with open(self.file,"w") as f:
                            old_data = data[found_line-1]
                            old_data = old_data.strip()
                            new_data = old_data.split(", ")
                            new_data[5] = update_attendance
                            replace_data = f"{new_data[0]}, {new_data[1]}, {new_data[2]}, {new_data[3]}, {new_data[4]}, {new_data[5]}, {new_data[6]}\n"
                            data[found_line-1] = replace_data
                            f.writelines(data)
                            print("\nData Updated Successfully")
                else:
                    print("Attendance must be between 0-100")
                    teacher_dash()
            except ValueError:
                print("Enter a Numerical value")
        
#Student Clas
class Student(Person):
    pass

#Teacher Classs
class Teacher(Person):
    pass

#Admin Class
class Admin(Person):
    @staticmethod
    def add_new():
        print("Enter details, Enter Numerical Value for all except Name,semester and graede\n")
        student_name = input("Student Name = ").capitalize()
        student_course = input("Course - ").capitalize()
        student_grade = input("Grade - ").capitalize()
        try:
            student_id = int(input("Student ID - "))
            student_semester = int(input("Semester - "))
            student_marks = int(input("Average Marks - "))
            student_atttendance = int(input("Attendance - "))
        except ValueError:
            print("Enter Integer Value")
            return
        if 0<=student_atttendance<=100 and 0<=student_marks<=100:
            new_student_data = f"\n{student_id}, {student_name}, {student_course}, {student_semester}, {student_marks}, {student_atttendance}, {student_grade}"
            with open("/Users/anupsingh/Documents/Codes/.vscode/Early Game/Student Manager/3.0/student.txt","a") as f:
                f.write(new_student_data)
        else:
            print("Value Of Attendance and Marks must be between 0-100")

    def average(what):
        stuff = True
        line = 1
        sum = 0
        with open(Person.student_file,"r") as f:
            while stuff:
                stuff = f.readline()
                if stuff  == "\n":
                    continue
                stuff = stuff.strip()
                if stuff == "":
                    break
                new = stuff.split(", ")
                needed_item = float(new[what])
                sum = needed_item + sum
                line = line+1
            if line !=0:
                pass
            return sum , (line-1)

    def change_pass():
        old_pass = input("Enter Old Password : ")
        if old_pass == Person.password:
            new_pass = input("Enter New Password : ")
            confirm_pass = input("Re-enter Password : ")
            if confirm_pass == new_pass:
                Person.password = new_pass
                print("Password Updated Successfully")
                admin_dash()
            else:
                print("Both Passwords are not same")
                admin_dash()
        else:
            print("Wrong Password")
            admin_dash()

    def remove_student():
        try:
            remove_id = int(input("Enter Student id - "))
        except ValueError:
            print("Enter Numerical value")
            admin_dash()
        s1 = Person(Person.student_file,remove_id)
        a = s1.finding()
        if a == 0:
            print("No Student Found With the provided ID")
            admin_dash()
        else:
            found , part = s1.finding()
            with open(Person.student_file,"r") as f:
                data = f.readlines()
            data.pop(found-1)
            with open(Person.student_file,"w") as f:
                f.writelines(data)
            print("Student ID",remove_id,"Has Been Removed From the Database")
            admin_dash()
        
#Main Function
def main_dash():
    print("\n========================================\n" \
          "             STUDENT MANAGER              \n" \
          "========================================\n\n" \
          "1. Student Login\n" \
          "2. Teacher Login\n" \
          "3. Admin Login\n" \
          "4. Exit\n")
    query = input("Enter The Command Number : ")
    student_file = "/Users/anupsingh/Documents/Codes/.vscode/Early Game/Student Manager/3.0/student.txt"
    teacher_file = "/Users/anupsingh/Documents/Codes/.vscode/Early Game/Student Manager/3.0/teachers.txt"
    try:
        query = int(query)
    except ValueError:
        print("Please Enter a Integer Value")
        main_dash()
    if query == 1:
        try:
            student_id = int(input("Enter Student ID : "))
        except:
            print("Enter A Integer")
            main_dash()
        global s1
        s1 = Student(student_file,student_id)
        found = s1.finding()
        if found == 0:
            print("\nStudent Not Found")
            main_dash()
        elif found != 0:
            found_line, data = s1.finding()
            print("\nWelcome",data[1])
            student_dash()
    elif query == 2:
        teacher_id = input("Enter Teacher ID : ")
        global t1
        t1 = Teacher(teacher_file,teacher_id)
        found = t1.finding()
        if found == 0:
            print("\nNo Teacher Found")
            main_dash()
        elif found != 0:
            found_line, data  = t1.finding()
            print("\nWelcome",data[1])
            teacher_dash()
    elif query == 3:
        password = input("Enter Password : ")
        if password == Person.password:
            print("Welcome Admin")
            admin_dash()
        else:
            print("Wrong Password")
            main_dash()
    elif query == 4:
        a = Person.confirm_exit()
        if a == 0:
            print("Exiting...")
            pass
        elif a != 0:
            print("Continuing Operation...")
            main_dash()
    else:
        print("Enter Correct Command Number")
        main_dash()

#Student Dashboard
def student_dash():
    print("\n========================================\n" \
            "             STUDENT PANEL              \n" \
            "========================================\n\n" \
            "1. View Profle\n" \
            "2. View Avergae Marks\n" \
            "3. View Grades\n" \
            "4. View Attendance\n" \
            "5. LogOut")
    query = input("Enter Command Number : ")
    try:
        query = int(query)
    except:
        print("\nPlease Enter a Valid Number")
        student_dash()
    found_line, part1 = s1.finding()
    if query == 1:
        s1.view_profile(part1)
        student_dash()
    elif query == 2:
        print("\nYour Avergae Marks are",part1[4])
        student_dash()
    elif query == 3:
        print("\nYour Grade is",part1[6])
        student_dash()
    elif query == 4:
        print("\nYour Attendance is",part1[5])
        student_dash()
    elif query == 5:
        a = Person.confirm_exit()
        if a == 0:
            print("Exiting...")
            main_dash()
        elif a != 0:
            print("Continuing Operation...")
            student_dash()
    else:
        print("Enter Correct Command Number")
        student_dash()

#Teacher Dashboard:
def teacher_dash():
    print("\n========================================\n" \
              "             TEACHER PANEL              \n" \
              "========================================\n\n" \
              "1. View Students\n" \
              "2. Search Student\n" \
              "3. Update Marks\n" \
              "4. Update Attendance\n" \
              "5. LogOut")
    query = input("Enter Command Number : ")
    try:
        query = int(query)
    except:
        print("\nPlease Enter a Valid Number")
        main_dash()
    if query == 1:
        t1.view_list()
        teacher_dash()
    elif query == 2:
        student_id = input("Enter Student ID : ")
        t2 = Teacher(Person.student_file,student_id)
        try:
            found = t2.finding()
            print(found)
            if found == 0:
                print("\nStudent Not Found")
            else:
                t2.view_profile(found[1])
        except:
            pass
        teacher_dash()
    elif query == 3:
        student_id = input("Enter Student ID. : ")
        t3 = Teacher("/Users/anupsingh/Documents/Codes/.vscode/Early Game/Student Manager/3.0/student.txt",student_id)
        try:
            a = t3.finding()
            if a == 0:
                print("\nStudent Not Found")
                teacher_dash()
            else:
                found = a[0]
                part = a[1]
                print("\nCurrent Marks of",part[1],"are",part[4])
                update_marks = input("Enter New Marks : ")
                t3.update_stuff(update_marks,None,found)
        except:
            print("Something Went Wrong")
            pass
        teacher_dash()
    elif query == 4:
        student_id = input("Enter Student ID. : ")
        t4 = Teacher(Person.student_file,student_id)
        try:
            a = t4.finding()
            if a == 0:
                print("\nStudent Not Found")
                teacher_dash()
            else:
                found = a[0]
                part = a[1]
                print("\nCurrent Attendance of",part[1],"are",part[5])
                update_attendance = input("Enter New Attendance : ")
                t4.update_stuff(None,update_attendance,found)
        except:
            print("Something Went Wrong")
            pass
        teacher_dash()
    elif query == 5:
        a = Person.confirm_exit()
        if a == 0:
            print("Exiting...")
            main_dash()
        elif a != 0:
            print("Continuing Operation...")
            teacher_dash()

def admin_dash():
    print("\n========================================\n" \
              "             ADMIN PANEL              \n" \
              "========================================\n\n" \
              "1. View Students\n" \
              "2. Search Student\n" \
              "3. Update Marks\n" \
              "4. Update Attendance\n" \
              "5. Add New Student\n" \
              "6. Remove Student\n" \
              "7. Calculate Average Marks\n" \
              "8. Calculate Average Attendance\n" \
              "9. Change Password\n"\
              "10. Logout")
    query = input("Enter Command Number : ")
    try:
        query = int(query)
    except:
        print("\nPlease Enter a Valid Number")
        admin_dash()
    if query == 1:
        Admin.view_list()
        admin_dash()
    elif query == 2:
        student_id = input("Enter Student ID : ")
        a1 = Admin(Person.student_file,student_id)
        try:
            found = a1.finding()
            print(found)
            if found == 0:
                print("\nStudent Not Found")
            else:
                a1.view_profile(found[1])
        except:
            pass
        admin_dash()
    elif query == 3:
        student_id = input("Enter Student ID. : ")
        a2 = Teacher(Person.student_file,student_id)
        try:
            a = a2.finding()
            if a == 0:
                print("\nStudent Not Found")
                admin_dash()
            else:
                found = a[0]
                part = a[1]
                print("\nCurrent Marks of",part[1],"are",part[4])
                update_marks = input("Enter New Marks : ")
                a2.update_stuff(update_marks,None,found)
        except:
            print("Something Went Wrong")
            pass
        admin_dash()
    elif query == 4:
        student_id = input("Enter Student ID. : ")
        a3 = Teacher(Person.student_file,student_id)
        try:
            a = a3.finding()
            if a == 0:
                print("\nStudent Not Found")
                admin_dash()
            else:
                found = a[0]
                part = a[1]
                print("\nCurrent Attendance of",part[1],"are",part[5])
                update_attendance = input("Enter New Attendance : ")
                a3.update_stuff(None,update_attendance,found)
        except:
            print("Something Went Wrong")
            pass
        admin_dash()
    elif query == 5:
        Admin.add_new()
        admin_dash()
    elif query == 6:
        Admin.remove_student()
    elif query == 7:
        sum , lines = Admin.average(4)
        avergae = f"{(sum/lines):.2f}"
        print("\nAverage Marks of",lines,"Students is",avergae,"%")
        admin_dash()
    elif query == 8:
        sum , lines = Admin.average(5)
        avergae = f"{(sum/lines):.2f}"
        print("\nAverage Attendance of",lines,"Students is",avergae,"%")
        admin_dash()
    elif query == 9:
        Admin.change_pass()
    elif query == 10:
        a = Person.confirm_exit()
        if a == 0:
            print("Exiting...")
            main_dash()
        elif a != 0:
            print("Continuing Operation...")
            admin_dash()
    else:
        print("Please Enter Valid Command Number")
        admin_dash()

main_dash()