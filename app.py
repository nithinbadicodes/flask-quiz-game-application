from flask import Flask, jsonify, render_template, session, redirect, request
import random
from data.easy_questions import easy_questions
from data.medium_questions import medium_questions
from data.hard_questions import hard_questions

app = Flask(__name__)
app.secret_key = "your_secret_key"


# ================= QUESTIONS =================


# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("front.html")


@app.route("/start")
def start():
    difficulty = session.get('difficulty', 'Easy')

    all_questions = {
        "Easy": easy_questions,
        "Medium": medium_questions,
        "Hard": hard_questions
    }

    questions = all_questions.get(difficulty, easy_questions)


    session['questions'] = questions
    session["question_indices"] = random.sample(range(len(questions)), 8)
    session["current_index"] = 0
    session["selected_answers"] = [None] * 8
    session["difficulty"] = difficulty  # ensure consistency

    return redirect("/quiz")

@app.route("/quiz")
def quiz():
    curr_index = session.get("current_index", 0)
    # question_indices = session.get('question_indices',
    #                                random.sample(range(len(session['questions'])),8))
    
    
    # print(q_index)
    # print(session['questions'])
    # q_index = question_indices[curr_index]
    q = session["questions"][curr_index]

    return render_template(
        "quiz.html",
        q=q,
        index=curr_index,
        total=8,
        selected=session["selected_answers"][curr_index]
    )


@app.route("/next", methods=["GET"])
def next():
    selected = request.form.get("options")
    curr_index = session["current_index"]
    print(selected)
    if selected is not None:
        session["selected_answers"][curr_index] = int(selected)

    session["current_index"] += 1

    if session["current_index"] >= 8:
        return redirect("/result")

    return redirect("/quiz")


@app.route("/prev", methods=["GET"])
def prev():
    curr_index = session["current_index"]

    selected = request.form.get("options")
    if selected is not None:
        session["selected_answers"][curr_index] = int(selected)

    if curr_index > 0:
        session["current_index"] -= 1

    return redirect("/quiz")


@app.route("/set_difficulty", methods=["POST"])
def set_difficulty():
    data = request.get_json()  # get JSON from fetch

    difficulty = data.get("difficulty")
    print(data)
    # store in session
    session["difficulty"] = difficulty

    print("Difficulty set to:", difficulty)

    return jsonify({"status": "success"})



@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()  # get JSON from fetch

    selected = data.get("answer")
    curr_index = session.get("current_index", 0)

    # make sure list exists
    if "selected_answers" not in session:
        session["selected_answers"] = [None] * 8  # adjust size if needed

    # store answer
    session["selected_answers"][curr_index] = selected

    print("Saved answer:", selected, "for question:", curr_index)

    return jsonify({"status": "success"})


@app.route("/result")
def result():
    score = 0

    for i, q in enumerate(session["questions"]):
        if session["selected_answers"][i] == q["answer"]:
            score += 1

    return render_template('final.html',score=score)


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)