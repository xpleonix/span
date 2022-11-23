import copy
import tkinter as tk
from tkinter import messagebox as mb

from arnion.data.departments_data import DepartmentDataHandler, DepartmentDataObject


class DepartmentsWindow:

    def __init__(self):
        self.window = tk.Toplevel()
        self.window.geometry("500x435")
        self.window.title("Departments")

        # header
        lblTitle1 = tk.Label(self.window, text="Departments",
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
        self.data_rows = DepartmentDataHandler.select_list()
        for data_row in self.data_rows:
            self.lbox_data_rows.insert('end', data_row.department_name)
        if len(self.data_rows) > 0:
            self.lbox_data_rows.select_set(0)

    # add new record
    def add_record(self):
        self.data_row = DepartmentDataObject()
        self.record_window = DepartmentWindow(True, self.data_row, self)
        self.record_window.open()

    # finish adding new record
    def add_record_callback(self, added_data_row: DepartmentDataObject):
        DepartmentDataHandler.insert(added_data_row)
        self.data_rows.append(added_data_row)
        self.lbox_data_rows.insert('end', added_data_row.department_name)
        self.lbox_data_rows.selection_clear(0, 'end')
        self.lbox_data_rows.select_set('end')

    def edit_record(self):
        self.selection = self.lbox_data_rows.curselection()[0]
        self.data_row = copy.deepcopy(self.data_rows[self.selection])
        self.record_window = DepartmentWindow(False, self.data_row, self)
        self.record_window.open()

    def edit_record_callback(self, edited_data_row: DepartmentDataObject):
        DepartmentDataHandler.update(edited_data_row)
        self.data_rows[self.selection] = edited_data_row
        self.refresh_list_box(self.selection, edited_data_row.department_name)

    # delete existing record
    def delete_record(self):
        answer = mb.askyesno(parent=self.window, title="Confirm",
                             message="Are you sure you want to delete this record?")
        if not answer:
            return
        self.selection = self.lbox_data_rows.curselection()[0]
        id = self.data_rows[self.selection].department_id
        DepartmentDataHandler.delete_by_id(id)
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


class DepartmentWindow:

    # constructor
    def __init__(self, add_new: bool, data_row: DepartmentDataObject,
                 parent: DepartmentsWindow):
        if add_new:
            title_text = "New department"
        else:
            title_text = "Edit department"

        self.add_new = add_new
        self.data_row = data_row
        self.parent = parent

        self.window = tk.Toplevel()
        self.window.geometry("500x200")
        self.window.title(title_text)

        # header
        lblTitle1 = tk.Label(self.window, text=title_text,
                     font=('Helvetica', 16, 'bold'), fg='#0000cc', justify='center')
        lblTitle1.place(x=25, y=15, width=450, height=50)

        # input fields
        lbl_name = tk.Label(self.window, text="Department", font=('Helvetica', 10, 'bold'))
        lbl_name.place(x=20, y=85)

        self.ent_name = tk.Entry(self.window, font=('Helvetica', 10, 'bold'))
        self.ent_name.place(x=115, y=85, width=370, height=25)
        self.ent_name.insert(tk.END, data_row.department_name)

        # button "Save"
        self.btn_ok = tk.Button(self.window, text="Save",
                                 font=('Helvetica', 10, 'bold'), bg='#ccffcc', command=self.save)
        self.btn_ok.place(x=140, y=150, width=90, height=30)

        # button "Save"
        self.btn_cancel = tk.Button(self.window, text="Cancel",
                                font=('Helvetica', 10, 'bold'), bg='#ffeeee', command=self.close)
        self.btn_cancel.place(x=250, y=150, width=90, height=30)


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
        self.data_row.department_name = str(self.ent_name.get())
