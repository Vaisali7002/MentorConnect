from flask import Flask, render_template, request,redirect,session
from models import create_tables, add_user, check_user,add_request,get_requests,update_status,get_student_requests

app = Flask(__name__)
app.secret_key = "mentorconnect123"

print("APP STARTED")
create_tables()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        success = add_user(name, email, password, role)

        if success:

            return redirect("/login")

        else:

            return "Email Already Exists"

    return render_template("register.html")
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = check_user(email, password)

        if user:
            session["role"] = user["role"]
            session["email"] = user["email"]

            if user["role"] == "Student":

                return redirect("/student_dashboard")

            else:

                return redirect("/dashboard")

        else:

            return "Invalid Credentials"

    return render_template("login.html")


@app.route("/request", methods=["GET", "POST"])
def request_page():
    if session.get("role") != "Student":

        return redirect("/")

    if request.method == "POST":

        student_email = request.form["student_email"]
        category = request.form["category"]
        priority = request.form["priority"]
        meeting_date = request.form["meeting_date"]
        message = request.form["message"]

        add_request(
            student_email,
            category,
            priority,
            meeting_date,
            message)
        return redirect("/student_dashboard")

    return render_template("request.html")
@app.route("/dashboard")
def dashboard():

    if session.get("role") != "Mentor":

        return redirect("/")

    requests = get_requests()

    return render_template("dashboard.html", requests=requests)
@app.route("/accept/<int:request_id>")
def accept_request(request_id):
    if session.get("role") != "Mentor":

        return redirect("/")

    update_status(request_id, "accepted")

    return redirect("/dashboard")
@app.route("/reject/<int:request_id>")
def reject_request(request_id):
    if session.get("role") != "Mentor":

        return redirect("/")

    update_status(request_id, "rejected")

    return redirect("/dashboard")
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")
@app.route("/student_dashboard")
def student_dashboard():

    if session.get("role") != "Student":

        return redirect("/")

    email = session["email"]

    requests = get_student_requests(email)

    return render_template(
        "student_dashboard.html",
        requests=requests
    )

if __name__ == "__main__":
    app.run(debug=True)