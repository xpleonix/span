from arnion.db.mysql_connection import my_connection_handler


class EmployeeDataObject():
    def __init__(self, employee_id=0, first_name='', middle_name='', last_name='', department_id=0):
        self.employee_id = employee_id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.department_id = department_id

    def get_full_name(self):
        full_name = self.first_name + " " + self.middle_name + " " + self.last_name
        return full_name

class EmployeeRptDataObject(EmployeeDataObject):
    def __init__(self, department_name='', employee_id=0, first_name='', middle_name='', last_name='', department_id=0):
        super().__init__(employee_id, first_name, middle_name, last_name, department_id)
        self.department_name = department_name

class EmployeeDataHandler():
    @staticmethod
    def select_list():
        employees = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM employees ORDER BY employee_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        employees.append(EmployeeDataHandler.get_employee(row))
            return employees
        except:
            raise

    @staticmethod
    def select_by_id(employee_id: int):
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT * FROM employees WHERE employee_id" + str(employee_id)
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    row = cursor.fetchone()
                    employee = EmployeeDataHandler.get_employee(row)
                    return employee
        except:
            raise

    @staticmethod
    def get_employee(row):
        return EmployeeDataObject(row[0], row[1], row[2], row[3], row[4])

    @staticmethod
    def select_list_rpt():
        employees = []
        try:
            with my_connection_handler.get_connection() as cnn:
                select_query = "SELECT d.department_name, e.* " \
                               "FROM employees e " \
                               "INNER JOIN departments d " \
                               "ON e.department_id = d.department_id " \
                               "ORDER BY department_id, employee_id"
                with cnn.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    for row in result:
                        employees.append(EmployeeDataHandler.get_employee_rpt(row))
            return employees
        except:
            raise

    @staticmethod
    def get_employee_rpt(row):
        return EmployeeRptDataObject(row[0], row[1], row[2], row[3], row[4], row[5])