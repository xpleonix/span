
class ListWindow:

    # constructor
    def __init__(self):
        pass

    # fill list
    def init_data_row(self):
        pass

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
        pass

    # refresh list
    def refresh_list_box(self, selection:int, value:str):
        pass

    def open(self):
        pass

    def close(self):
        pass

class RecordWindow:

    # constructor
    def __init__(self):
        pass

    # open window
    def open(self):
        pass

    # save record and close window
    def save(self):
        pass

    # close window without saving a record ("cancel" button)
    def close(self):
        pass

    # collect info from the input fields
    def collect_from_controls(self):
        pass
