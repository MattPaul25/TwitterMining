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


class DatabaseConnect():
    """add some method for connection here"""


class DatabaseReader(DatabaseConnect):
    """Handles all transactions with database"""

    def __init__(self, request):
        self._request = request

    def extract_data():
        """pull data from database and place it in list"""
        # add code here
        return ['some data', 1]


class DatabaseWriter(DatabaseConnect):
    """Handles all transactions with database"""

    def __init__(self, request):
        self._request = request

    def push_data():
        """run query on server but do not create a list"""
        #add code here 

#x = csv_reader("companylist.csv")
#print(x)


