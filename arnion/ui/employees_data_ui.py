import copy
import tkinter as tk
from tkinter import messagebox as mb

from arnion.data.employees_data import EmployeeDataHandler


class EmployeesWindow:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("500x435")
        self.window.title("Employees")

        # header
        lblTitle1 = tk.Label(self.window, text="Employees",
                             font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lblTitle1.place(x=25, y=15, width=450, height=50)

        # container for the list and scrollbar
        self.frame = tk.Frame(self.window)

        # add list of records
        self.lbox_data_rows = tk.Listbox(self.frame, selectmode='single', activestyle='none',
                                         font=('Courier New', 10, 'bold'))
        self.lbox_data_rows.place(x=0, y=0, width=450, height=300)

        self.scrollbar = tk.Scrollbar(self.frame, orient='vertical')
        self.scrollbar.config(command=self.lbox_data_rows.yview)
        self.scrollbar.place(x=450, y=0, width=20, height=300)

        self.lbox_data_rows.config(yscrollcommand=self.scrollbar.set)

        self.init_data_rows()
        self.frame.place(x=15, y=75, width=470, height=300)

        # button Add
        self.btn_add = tk.Button(self.window, text="Add",
                                 font=('Helvetica', 10, 'bold'), bg='#ccffff', command=self.add_record)
        self.btn_add.place(x=20, y=390, width=90, height=30)

        # button Edit
        self.btn_edit = tk.Button(self.window, text="Edit",
                                 font=('Helvetica', 10, 'bold'), bg='#ccffff', command=self.edit_record)
        self.btn_edit.place(x=120, y=390, width=90, height=30)

        # button Delete
        self.btn_delete = tk.Button(self.window, text="Delete",
                                 font=('Helvetica', 10, 'bold'), bg='#ccffff', command=self.delete_record)
        self.btn_delete.place(x=220, y=390, width=90, height=30)

        # button Close
        self.btn_close = tk.Button(self.window, text="Close",
                                 font=('Helvetica', 10, 'bold'), bg='#ccffff', command=self.close)
        self.btn_close.place(x=390, y=390, width=90, height=30)

    # function to fill the list
    def init_data_rows(self):
        self.data_rows = EmployeeDataHandler.select_list()
        for data_row in self.data_rows:
            self.lbox_data_rows.insert('end', data_row.get_full_name())
        if len(self.data_rows) > 0:
            self.lbox_data_rows.select_set(0)

    # add new record
    def add_record(self):
        pass

    # finishing add new record
    def add_record_callback(self, added_data_row):
        pass

    def edit_record(self):
        pass

    def edit_record_callback(self, edited_data_row):
        pass

    # delete existing record
    def delete_record(self):
        answer = mb.askyesno(parent=self.window, title="Confirm",
                             message="Are you sure you want to delete this record?")
        if not answer:
            return
        self.selection = self.lbox_data_rows.curselection()[0]
        id = self.data_rows[self.selection].employee_id
        EmployeeDataHandler.delete_by_id(id)
        self.data_rows.pop(self.selection)
        self.lbox_data_rows.delete(self.selection)


    # refresh list
    def refresh_list_box(self, selection:int, value:str):
        pass

    def open(self):
        # move focus on window creation
        self.window.focus_force()
        # move commands om window creation
        self.window.grab_set()

    def close(self):
        self.window.destroy()