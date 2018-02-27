import os
from flask import Flask, render_template, request

__author__ = 'jay'


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'userdata/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)


    return render_template("complete.html")
	
@app.route('/delete/<filename>',methods=['GET', 'POST'])
def delete(filename):
    target = os.path.join(APP_ROOT, 'userdata/')
    file_path = target+"\\"+filename
    print(file_path)
    try:
        os.remove(file_path)
        file_handle.close()
    except Exception as error:
        app.logger.error("Error removing file handle", error)
   
    return render_template("delete.html")


	
if __name__ == "__main__":
    app.run(port=4555, debug=True)