import os

from django.http import JsonResponse

from lib.FileUploader import FileUploader
from lib.java_runner import JavaRunner
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    user_dir = request.POST["user"]
    code = request.POST["code"]

    java_runner = JavaRunner(user_directory=user_dir, code=code)
    res = java_runner.run()

    return JsonResponse({
        'output': res
    }, status=200)


@csrf_exempt
def upload_java_test_file(request):
    file = request.FILES["file"]
    fu = FileUploader(filename=file, file=file)
    fu.upload()

    return JsonResponse({
        "status": "ok"
    }, status=200)


def get_test_file_list(request):
    print(request)
    return JsonResponse({
        "file_list": os.listdir("java_files/test_cases")
    }, status=200)


@csrf_exempt
def delete_test(request):
    filename = request.POST["filename"]
    print(filename)
    try:
        os.remove("java_files/test_cases/{}".format(filename))
    except FileNotFoundError as err:
        return JsonResponse({"error": str(err), "status": "failed"}, status=500)

    return JsonResponse({"message": "{} deleted".format(filename), "status": "success"}, status=200)
