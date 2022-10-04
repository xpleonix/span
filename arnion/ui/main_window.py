import tkinter as tk

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
                               font=('Helvetica', 10, 'bold'), bg="#ccffcc")
        btn_report.place(x=25, y=200, width=120, height=50)

        # button for Reports Employees
        btn_close = tk.Button(self.window, text="Employees",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc")
        btn_close.place(x=160, y=200, width=120, height=50)

        #add close window button
        btn_close = tk.Button(self.window, text="Exit",
                              font=('Helvetica', 10, 'bold'), bg="#ccffcc", command=self.close)
        btn_close.place(x=160, y=300, width=120, height=50)


    #close main window function
    def close(self):
        self.window.destroy()

    #start cycle
    def start_mainloop(self):
        self.window.mainloop()



