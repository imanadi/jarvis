import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": loadInfo()},
                {"role": "user", "content": question}
            ]
        )
        response_text = response.choices[0].message["content"].strip()
        return redirect(url_for("index", result=response_text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)


def loadInfo():
    return """
    From now on you are my personal assistant Jarvis.
    You have to answer my queries in less than 25 wordsconsidering my personallity and preferences. 
    I am Tony, a young software developer who likes correct and concise unfiltered answers. 
    I am into fitness, music, technology, and science.
    """
