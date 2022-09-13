from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")
#href = "{{url_for('function')}}"
@app.route('/gallery')
def gallery():
    return render_template("photo_index.html")

@app.route('/post')
def post():
    return render_template("post.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def recieve_data():
    data = request.form
    name = data["name"]
    email = data["email"]
    phone = data["phone"]
    message = data["message"]
    return f"<h1> {name}. Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True)