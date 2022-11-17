import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText as st

from arnion.data.employees_data import EmployeeDataHandler


class EmployeesReportWindow:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("500x450")
        self.window.title("Report: Employees")

        # header
        lblTitle1 = tk.Label(self.window, text="Employees",
                             font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lblTitle1.place(x=25, y=15, width=350, height=50)

        # window of output text
        self.txt_output = st(self.window, font=('Courier New', 10, 'bold'))
        self.txt_output.insert(tk.END, self.get_report_text())
        self.txt_output.place(x=15, y=75, width=470, height=310)

        # close button
        self.btn_close = tk.Button(self.window, text="Close",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc", command=self.close)
        self.btn_close.place(x=190, y=400, width=90, height=30)

    def get_report_text(self):
        report_text = "                EMPLOYEES BY DEPARTMENTS " + os.linesep
        report_text += "--------------------------------------------------" + os.linesep
        data_rows = EmployeeDataHandler.select_list_rpt()
        current_department_name = "d118034c-2021-4b75-9ddd-87b4f219b84d"
        for data_row in data_rows:
            # if department is new add it to the group header
            if data_row.department_name != current_department_name:
                report_text += data_row.department_name + os.linesep
                current_department_name = data_row.department_name
            # adding row
            report_text += "          " + data_row.get_full_name() + os.linesep
        return report_text

    def open(self):
        # move focus on window creation
        self.window.focus_force()
        # move commands om window creation
        self.window.grab_set()

    def close(self):
        self.window.destroy()

