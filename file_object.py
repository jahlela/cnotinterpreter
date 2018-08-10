
class FileObject(object):
    def __init__(self, filename = ""):
        self.filename = filename
        self.get_file_data()

    def get_file_data(self):
        """
        Returns an array of stripped lines in program
        """
        if self.filename:
            with open(self.filename, 'r') as readable_file:
                self.readable_file = readable_file
                self.content = self.readable_file.readlines()
                self.lines = [x.strip() for x in self.content]
            readable_file.close()
