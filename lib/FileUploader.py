class FileUploader:

    __main_dir = "java_files/test_cases"

    def __init__(self, filename, file):
        self.filename = filename
        self.file = file

    def upload(self):
        loc = "{0}/{1}".format(self.__main_dir, self.filename)
        with open(loc, "wb+") as f:
            for chunk in self.file.chunks():
                f.write(chunk)

        return "success"
