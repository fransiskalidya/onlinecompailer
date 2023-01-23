import re


class FileCreator:

    __main_dir = "java_files"
    filename = None
    package_name = None
    destination = None
    code = None

    def __init__(self, filename, package_name, user_dir, code):
        self.filename = filename
        self.package_name = package_name
        self.destination = "{}/{}/".format(self.__main_dir, user_dir)
        self.code = code

    def create_file(self):
        des = self.destination
        dest_file = "{}/{}.java".format(des, self.filename)

        try:
            f = open(dest_file, "w")
            f.write("package {}; \n\n".format(self.package_name))
            f.write(self.code)
            f.close()

        except OSError as err:
            print(err)
            return err

    def create_test_file(self):

        # test file name base on class name of write code by user

        test_filename = "JUnit{}Test".format(self.filename) # JUnitHelloWorldTest.java
        fdir = "java_files/test_cases/{}".format(test_filename)

        test_file = open("{}.java.txt".format(fdir), "r+")
        file_content = test_file.read()

        # replace {{user_package}} as defined package
        reg = "{{user_package}}"
        final_content = re.sub(reg, string=file_content, repl=self.package_name)

        test_file.close()

        try:
            destination = "java_files/{0}/{1}.java".format(self.package_name, test_filename)
            java_test_file = open(destination, "w")
            java_test_file.write(final_content)
            java_test_file.close()
        except OSError as e:
            print(e)


