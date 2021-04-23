from flask import Flask, request, render_template
import json

data = json.load(open("data.json"))
app = Flask(__name__)
result = " "
holder = "Enter word"


@app.route('/', methods=["GET", "POST"])
def main():
    if request.method == "POST":
        text = str(request.form.get('word')).lower()
        if text is None:
            prompt = "Enter a word"
            return render_template("home.html", result=prompt, holder=holder)
        if text in data:
            string = data[text]
            return render_template("home.html", result=string, holder=text)
        else:
            prompt = '"' + text + '" does not exist in the Dictionary'
            return render_template("home.html", result=prompt, holder=text)

    return render_template("home.html", result=result, holder=holder)


if __name__ == "__main__":
    app.run(debug=True)
