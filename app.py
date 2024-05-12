from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("FlightSystem.html")

@app.route("/search", methods=["GET"])
def search():
    
    background_url = request.args.get('background-url')

   
    return render_template("new_page.html", background_url=background_url)

if __name__ == "__main__":
    app.run(debug=True)
