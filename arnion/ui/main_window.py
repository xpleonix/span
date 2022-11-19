import tkinter as tk

from arnion.data.departments_data import DepartmentDataHandler, DepartmentDataObject
from arnion.data.employees_data import EmployeeDataHandler, EmployeeDataObject
from arnion.db.mysql_connection import ConnectionHandler
from arnion.ui.departments_reports_ui import DepartmentsReportWindow
from arnion.ui.employees_report_ui import EmployeesReportWindow


class MainWindow:

    # constructor
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("310x380")
        self.window.title("SPAN")

        # header
        lbl_title = tk.Label(text="SPAN", font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lbl_title.place(x=25, y=15, width=250, height=50)

        # header for Data
        lblTitle1 = tk.Label(text="Data", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lblTitle1.place(x=25, y=55, width=250, height=50)

        #button for Data Departments
        btn_report = tk.Button(self.window, text="Departments",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc")
        btn_report.place(x=25, y=100, width=120, height=50)

        # button for Data Employees
        btn_close = tk.Button(self.window, text="Employees",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc")
        btn_close.place(x=160, y=100, width=120, height=50)

        # header for Reports
        lblTitle1 = tk.Label(text="Reports", font=('Helvetica', 12, 'bold'), fg='#0066ff', justify='center')
        lblTitle1.place(x=25, y=155, width=250, height=50)

        # button for Reports Departments
        btn_report = tk.Button(self.window, text="Departments",
                               font=('Helvetica', 10, 'bold'), bg="#ccffcc", command=self.do_report_departments)
        btn_report.place(x=25, y=200, width=120, height=50)

        # button for Reports Employees
        btn_close = tk.Button(self.window, text="Employees",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc", command=self.do_report_employees)
        btn_close.place(x=160, y=200, width=120, height=50)

        # "Test" button
        btn_test = tk.Button(self.window, text="Test",
                              font=('Helvetica', 10, 'bold'), bg="#ffffcc", command=self.do_test)
        btn_test.place(x=25, y=300, width=120, height=50)

        #add close window button
        btn_close = tk.Button(self.window, text="Exit",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc", command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)

    #function Test

    def do_test(self):
        # replace employee
        #employee = EmployeeDataHandler.select_by_id(7)
        #print(employee.get_full_name(), employee.department_id)
        #employee.first_name = "Дмитрий"
        #employee.middle_name = "Олегович"
        #employee.last_name = "Кириллов"
        #employee.department_id = "1"
        #print(employee.get_full_name(), employee.department_id)
        #EmployeeDataHandler.update(employee)
        #print("Done!")

        # add new employee
        employee = EmployeeDataObject(first_name="Василий", middle_name="Леонидович",
                                      last_name="Вадимов", department_id=2)
        print(employee.employee_id)
        EmployeeDataHandler.insert(employee)
        print(employee.employee_id)
        print("Done!")

# add new department
        #department = DepartmentDataObject(department_name="Отдел тестирования")
        #print(department.department_id)
        #DepartmentDataHandler.insert(department)
        #print(department.department_id)
        #print("Done!")
              
# rename department
        #department = DepartmentDataHandler.select_by_id(3)
        #print(department.department_name)
        #department.department_name = "Отдел работы с клиентами"
        #print(department.department_name)
        #DepartmentDataHandler.update(department)
        #print("Done!")

    # open report Departments
    def do_report_departments(self):
        rpt = DepartmentsReportWindow()
        rpt.open

    # open report Employees
    def do_report_employees(self):
        rpt = EmployeesReportWindow()
        rpt.open

    #close main window function
    def close(self):
        self.window.destroy()

    #start cycle
    def start_mainloop(self):
        self.window.mainloop()



