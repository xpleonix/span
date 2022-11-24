import copy
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import ttk

from arnion.data.departments_data import DepartmentDataHandler
from arnion.data.employees_data import EmployeeDataHandler, EmployeeDataObject


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
        self.data_row = EmployeeDataObject()
        self.record_window = EmployeeWindow(True, self.data_row, self)
        self.record_window.open()

    # finishing add new record
    def add_record_callback(self, added_data_row: EmployeeDataObject):
        EmployeeDataHandler.insert(added_data_row)
        self.data_rows.append(added_data_row)
        self.lbox_data_rows.insert('end', added_data_row.get_full_name())
        self.lbox_data_rows.selection_clear(0, 'end')
        self.lbox_data_rows.select_set('end')

    def edit_record(self):
        self.selection = self.lbox_data_rows.curselection()[0]
        self.data_row = copy.deepcopy(self.data_rows[self.selection])
        self.record_window = EmployeeWindow(False, self.data_row, self)
        self.record_window.open()

    def edit_record_callback(self, edited_data_row: EmployeeDataObject):
        EmployeeDataHandler.update(edited_data_row)
        self.data_rows[self.selection] = edited_data_row
        self.refresh_list_box(self.selection, edited_data_row.get_full_name())


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
        self.lbox_data_rows.delete(selection, selection)
        self.lbox_data_rows.insert(selection, value)
        self.lbox_data_rows.select_set(selection)

    def open(self):
        # move focus on window creation
        self.window.focus_force()
        # move commands om window creation
        self.window.grab_set()

    def close(self):
        self.window.destroy()


class EmployeeWindow:

    # constructor
    def __init__(self, add_new: bool, data_row: EmployeeDataObject,
                 parent: EmployeesWindow):
        if add_new:
            title_text = "New employee"
        else:
            title_text = "Edit employee"

        self.add_new = add_new
        self.data_row = data_row
        self.parent = parent

        self.window = tk.Toplevel()
        self.window.geometry("500x290")
        self.window.title(title_text)

        # header
        lblTitle1 = tk.Label(self.window, text=title_text,
                     font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lblTitle1.place(x=25, y=15, width=450, height=50)

        # input fields
        lbl_first_name = tk.Label(self.window, text="First name", font=('Helvetica', 10, 'bold'))
        lbl_first_name.place(x=20, y=85)

        self.ent_first_name = tk.Entry(self.window, font=('Helvetica', 10, 'bold'))
        self.ent_first_name.place(x=115, y=85, width=370, height=25)
        self.ent_first_name.insert(tk.END, data_row.first_name)

        lbl_middle_name = tk.Label(self.window, text="Second name", font=('Helvetica', 10, 'bold'))
        lbl_middle_name.place(x=20, y=120)

        self.ent_middle_name = tk.Entry(self.window, font=('Helvetica', 10, 'bold'))
        self.ent_middle_name.place(x=115, y=120, width=370, height=25)
        self.ent_middle_name.insert(tk.END, data_row.middle_name)

        lbl_last_name = tk.Label(self.window, text="Last name", font=('Helvetica', 10, 'bold'))
        lbl_last_name.place(x=20, y=155)

        self.ent_last_name = tk.Entry(self.window, font=('Helvetica', 10, 'bold'))
        self.ent_last_name.place(x=115, y=155, width=370, height=25)
        self.ent_last_name.insert(tk.END, data_row.last_name)

        # input filed for department
        lbl_department = tk.Label(self.window, text="Department", font=('Helvetica', 10, 'bold'))
        lbl_department.place(x=20, y=195)

        self.cbo_department = ttk.Combobox(self.window, font=('Helvetica', 10, 'bold'))
        self.init_combobox()
        # prohibit entry by user
        self.cbo_department['state'] = 'readonly'
        self.set_id_to_combobox(data_row.department_id)
        self.cbo_department.place(x=115, y=190, width=370, height=25)

        # button "Save"
        self.btn_ok = tk.Button(self.window, text="Save",
                                 font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.save)
        self.btn_ok.place(x=140, y=240, width=90, height=30)

        # button "Save"
        self.btn_cancel = tk.Button(self.window, text="Cancel",
                                font=('Helvetica', 10, 'bold'), bg='#ffeeee', command=self.close)
        self.btn_cancel.place(x=250, y=240, width=90, height=30)


    # fill Combobox
    def init_combobox(self):
        self.cbox_ids = []
        self.cbox_values = []
        data_rows = DepartmentDataHandler.select_list()
        for data_row in data_rows:
            self.cbox_ids.append(data_row.department_id)
            self.cbox_values.append(data_row.department_name)
        self.cbo_department['values'] = self.cbox_values

    # set department id to list in combobox
    def set_id_to_combobox(self, id):
        try:
            id_index = self.cbox_ids.index(int(id))
            self.cbo_department.set(self.cbox_values[id_index])
        except ValueError as e:
            self.cbo_department.set("")

    # get id from combobox list
    def get_id_from_combobox(self, value: str) -> int:
        try:
            id_index = self.cbox_values.index(value)
            return self.cbox_ids[id_index]
        except ValueError as e:
            return 0


    # open window
    def open(self):
        # move focus on window creation
        self.window.focus_force()
        # move commands om window creation
        self.window.grab_set()

    # save record and close window
    def save(self):
        self.collect_from_controls()
        if self.add_new:
            self.parent.add_record_callback(self.data_row)
        else:
            self.parent.edit_record_callback(self.data_row)
        self.close()

    # close window without saving a record ("cancel" button)
    def close(self):
        self.window.destroy()

    # collect info from the input fields
    def collect_from_controls(self):
        self.data_row.first_name = str(self.ent_first_name.get())
        self.data_row.middle_name = str(self.ent_middle_name.get())
        self.data_row.last_name = str(self.ent_last_name.get())
        self.data_row.department_id = str(self.get_id_from_combobox(self.cbo_department.get()))

