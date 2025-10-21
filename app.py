# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'static/pdfs'
# app.config['ADMIN_PASSWORD'] = 'iiser2025'  # You can change this password

# @app.route("/")
# def home():
#     user = {
#         "name": "Argha Patra",
#         "about": "BS-MS Second Year Undergraduate Student in IISER Mohali",
#     }
#     return render_template("index.html", user=user)

# @app.route("/blogs")
# def blogs():
#     pdf_files = os.listdir(app.config['UPLOAD_FOLDER'])
#     blogs = [
#         {"title": os.path.splitext(pdf)[0].replace('_', ' ').title(), "pdf": pdf}
#         for pdf in pdf_files
#     ]
#     return render_template("blogs.html", blogs=blogs)

# @app.route("/projects")
# def projects():
#     projects_list = [
#         {"title": "Predictive Modeling of Bacterial Growth", 
#          "desc": "Mathematical model for OD growth data.", 
#          "pdf": "project1.pdf"},
#         {"title": "Arduino Robotic Arm", 
#          "desc": "Design and control of robotic arm with sensors.", 
#          "pdf": "robotic_arm_report.pdf"}
#     ]
#     return render_template("projects.html", projects=projects_list)

# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     if request.method == "POST":
#         password = request.form.get("password")
#         if password != app.config['ADMIN_PASSWORD']:
#             return "Unauthorized: Wrong Password", 403

#         file = request.files['pdf']
#         if file and file.filename.endswith('.pdf'):
#             filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
#             file.save(filepath)
#             return redirect(url_for('blogs'))
#         else:
#             return "Invalid File Type", 400
#     return render_template("upload.html")

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/pdfs'
app.config['ADMIN_PASSWORD'] = 'iiser2025'  # change if needed

@app.route("/")
def home():
    user = {
        "name": "Argha Patra",
        "about": "BS-MS Second Year Undergraduate Student in IISER Mohali",
    }
    return render_template("index.html", user=user)

@app.route("/blogs")
def blogs():
    pdf_folder = app.config['UPLOAD_FOLDER']
    files = os.listdir(pdf_folder)
    blogs = []

    for f in files:
        if f.endswith('.pdf') or f.endswith('.md'):
            blogs.append({
                "title": os.path.splitext(f)[0].replace('_', ' ').title(),
                "file": f,
                "type": f.split('.')[-1]  # 'pdf' or 'md'
            })
    return render_template("blogs.html", blogs=blogs)
@app.route("/projects")
def projects():
    projects_list = [
        {
            "title": "Predictive Modeling of Bacterial Growth",
            "desc": "Mathematical model for OD growth data.",
            "pdf": "project1.pdf"
        },
        {
            "title": "Arduino Robotic Arm",
            "desc": "Design and control of robotic arm with sensors.",
            "pdf": "robotic_arm_report.pdf"
        }
    ]
    return render_template("projects.html", projects=projects_list)

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        password = request.form.get("password")
        if password != app.config['ADMIN_PASSWORD']:
            return "Unauthorized: Wrong Password", 403

        file = request.files['pdf']
        if file and file.filename.endswith('.pdf'):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            return redirect(url_for('blogs'))
        else:
            return "Invalid File Type", 400

    return render_template("upload.html")

# For local testing; Render uses gunicorn in production
if __name__ == "__main__":
    app.run(debug=True)

