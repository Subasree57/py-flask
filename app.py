from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # Passing static data to the template
    return render_template("index.html", title="Welcome", description="This is a dynamic Flask application!")

@app.route("/user/<username>")
def user_profile(username):
    # Passing dynamic data (username)
    return render_template("user.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)
