from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simulated database (dictionary)
users = {
    "john": {"name": "suba", "age": 22, "hobby": "Teaching"},
    "jane": {"name": "yuva", "age": 24, "hobby": "Reading"}
}

@app.route("/")
def home():
    return render_template("index.html", title="Home - Flask App")

@app.route("/about")
def about():
    return render_template("about.html", title="About Us")

@app.route("/users")
def list_users():
    return render_template("users.html", title="User List", users=users)

@app.route("/user/<username>")
def user_profile(username):
    user = users.get(username)
    if not user:
        return render_template("404.html", title="User Not Found"), 404
    return render_template("user.html", title=user["name"], user=user)

@app.route("/add-user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form["username"].strip().lower()
        name = request.form["name"]
        age = request.form["age"]
        hobby = request.form["hobby"]

        if username in users:
            error = "Username already exists!"
            return render_template("add_user.html", title="Add User", error=error)

        users[username] = {"name": name, "age": int(age), "hobby": hobby}
        return redirect(url_for("list_users"))

    return render_template("add_user.html", title="Add User")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", title="404 Error"), 404

if __name__ == "__main__":
    app.run(debug=True)
