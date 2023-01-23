# Readme  
  
use following step to using this project\  
this project using **django** and **python 3.x**.\  
**python 3.10** is recommended  
  
## First initialize project  
1. make python virtual environment  
   - in current project run `python -m venv venv`  
 - it will create `venv` folder in project  
   
2. run `source venv/bin/activate`  
    in your terminal will look like\
    `(venv) user@your_pc onlinecompiler %`  
3. on `(venv)` mode, run `pip install -r requirements.txt`

all project dependency is located on `requirements.txt`  
  
## How to run project  
  
1. run `(venv)` mode with step number 2 on above.  
2. on `(venv)` mode, run `python manage.py runserver` 
it will serve on default port `8000`   
## Exit venv mode  
run `(venv) you@your_pc % deactivate`  
  
## API DOC  
  
| URL                    | Description               | method | params | response |  
|------------------------|---------------------------|--------|--------|----------|  
|  `/compile/run` | Compile java file | POST | ```{code:'xxx', user: 'you@mail.com'}```|```{output: { java: 'xx', test_output: 'xx', point: x}}```                 
| `/compile/test_files`|Get all java Test Files | GET ||
|`/compile/upload`|Upload java test file|POST|`{file:'xx'(multipart/form-data)}`|`{status: "ok"}`
|`compile/delete`|Delete java test file|POST|`{filename: 'xx'}`| ```{"message": "readme.txt deleted","status": "success"}```
