from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    title = "Airline Stats and Visualizations"
    return render_template("index.html", title=title)

@app.route("/routes")
def routes():
    return render_template("routes.html")

@app.route("/visuals")
def visuals():
    return render_template("visuals.html")
    



if __name__ == "__main__":
    app.run(debug=True)