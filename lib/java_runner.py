import os
import re
import subprocess
from lib.FileCreator import FileCreator


class JavaRunner:

    __main_directory = "java_files/"
    filename = str
    test_filename = str

    def __init__(self, user_directory, code):
        self.user_directory = self.get_user_dir(user_directory)
        self.code = code

    def get_user_dir(self, user_mail):
        replace_at = re.sub('@+', "_", user_mail)
        replace_dot = re.sub('\.', "_", replace_at)
        return replace_dot

    def check_and_create_dir(self):
        directory_name = "{}/{}".format(self.__main_directory, self.user_directory)
        dir_is_exist = os.path.isdir(directory_name)

        if not dir_is_exist:
            os.mkdir(directory_name)

    def create_file(self):
        class_regx = r'(?<=class )\w+'
        file = re.search(class_regx, self.code)
        filename = file.group(0)

        self.filename = filename
        self.test_filename = "JUnit{}Test".format(filename)
        try:
            pack_name = "{}".format(self.user_directory)
            fc = FileCreator(filename=self.filename, package_name=pack_name, user_dir=self.user_directory,
                             code=self.code)
            fc.create_file()

            fc.create_test_file()

        except OSError as e:
            print(e)

        finally:
            return self.compile_file()

    def compile_file(self):
        compile_command = "javac java_files/{}/{}.java".format(self.user_directory, self.filename)

        try:
            output = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            output = err
        print(output)
        return output

    def run_file(self):
        run_command = "cd java_files && java --version && java -cp .;{0}/{1} {0}.{1}".format(self.user_directory, self.filename)
        try:
            output = subprocess.run(run_command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

        except subprocess.CalledProcessError as err:
            output = err

        finally:
             os.remove("java_files/{}/{}.class".format(self.user_directory, self.filename))

        print(output)
        return output

    def run_test(self):
        junit_file = "lib/junit-4.13.2.jar"
        hamcrest_file = "lib/hamcrest-core-1.3.jar"

        run_compile_test = "cd java_files && javac -cp .;{0};{1} {2}/{3}.java".\
            format(junit_file, hamcrest_file, self.user_directory, self.test_filename)
        run_test_command = "cd java_files && java -cp .;{0};{1};{2}/{3} org.junit.runner.JUnitCore {2}.{3}".\
            format(junit_file, hamcrest_file, self.user_directory, self.test_filename) #

        try:
            output = subprocess.run(run_compile_test, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            output = err
        print(output)

        try:
            output = subprocess.run(run_test_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as err:
            output = err

        print(output)
        return output

    def run(self):
        self.check_and_create_dir()

        create_n_compile = self.create_file()

        if create_n_compile.returncode == 1:
            return {"java": create_n_compile.stderr.decode("utf-8"), "test_output": "TEST FAILED!"}

        final_output = self.run_file()

        test_output = None
        point = 0

        if final_output.returncode == 1:
            java = final_output.stderr.decode("utf-8")
        else:
            java = final_output.stdout.decode("utf-8")

            o = self.run_test()
            if o.returncode == 0:
                test_output = o.stdout.decode("utf-8")

                matcher = r'(OK \(\d+ test\))'
                ok_matcher = re.compile(matcher)
                res = ok_matcher.search(test_output)

                # add point of found OK (<int> test)
                point = len(res.groups()) * 10
            else:
                test_output = o.stderr.decode("utf-8") or o.stdout.decode("utf-8")

        output = {
            "java": java,
            "test_output": test_output,
            "point": point
        }

        return output
