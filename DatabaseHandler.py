import csv

class CsvReader():
    """reads CSV file"""
    def __init__(self, file_path):
        self._file_path = file_path     
        self.import_csv()

    def import_csv(self):
        """moves data into a list object"""
        with open(self._file_path, 'r') as csvfile:
            quote_reader = csv.reader(csvfile, delimiter='|')
            self.quote_list = list(quote_reader)            

    def __str__(self):
        x = ''
        for row in self.quote_list:
           x += str(row) + '\n'
        return x

class DatabaseHandler():
    """Handles all transactions with database"""

    def __init__(self, request, is_pull):
        self._request = request
        if is_pull:
            self.extract_data()
        elif not is_pull:
            self.push_data()
        
    def extract_data():
        """pull data from database and place it in list"""
        # add code here

    def push_data():
        """run query on server but do not create a list"""
        #add code here 


x = csv_reader("companylist.csv")
print(x)


