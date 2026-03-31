from flask import Flask, jsonify, render_template, session, redirect, request
import random
from data.easy_questions import easy_questions
from data.medium_questions import medium_questions
from data.hard_questions import hard_questions

app = Flask(__name__)
app.secret_key = "your_secret_key"


# ================= ROUTES =================

@app.route("/")
def home():
    return render_template("front.html")


@app.route("/start")
def start():
    difficulty = session.get('difficulty', 'easy').lower()

    session.clear()
    session["difficulty"] = difficulty

    all_questions = {
        "easy": easy_questions,
        "medium": medium_questions,
        "hard": hard_questions
    }
    print(len(easy_questions))
    print(len(medium_questions))
    print(len(hard_questions))
    questions = all_questions.get(difficulty, easy_questions)

    
    session["questions"] = questions

    indices = list(range(len(questions)))
    random.shuffle(indices)
    session["question_indices"] = indices[:8]

    session["current_index"] = 0
    session["selected_answers"] = [None] * 8

    return redirect("/quiz")

@app.route("/quiz")
def quiz():
    curr_index = session.get("current_index", 0)
    print(curr_index)
    print(session['difficulty'])
    # FIX: prevent index out of range
    if curr_index >= 8:
        return redirect("/result")

    question_indices = session.get("question_indices")
    q_index = question_indices[curr_index]
    q = session["questions"][q_index]


    return render_template(
        "quiz.html",
        q=q,
        index=curr_index,
        total=8,
        selected=session["selected_answers"][curr_index]
    )

@app.route("/next", methods=["POST"])
def next():
    # FIX: stop at last question
    if session["current_index"] < 7:
        session["current_index"] += 1
        return redirect("/quiz")
    else:
        session["current_index"] = 8
        return redirect("/result")

@app.route("/prev", methods=["POST"])
def prev():
    if session["current_index"] > 0:
        session["current_index"] -= 1

    return redirect("/quiz")


@app.route("/review_next", methods=["POST"])
def review_next():
    # FIX: stop at last question
    if session["current_index"] < 7:
        session["current_index"] += 1
        return redirect("/review")
    else:
        session["current_index"] = 8
        return redirect("/result")


@app.route("/review_prev", methods=["POST"])
def review_prev():
    if session["current_index"] > 0:
        session["current_index"] -= 1

    return redirect("/review")


@app.route("/set_difficulty", methods=["POST"])
def set_difficulty():
    data = request.get_json()
    difficulty = data.get("difficulty")
    
    session["difficulty"] = difficulty.lower()
    print("Stored difficulty:", session["difficulty"])

    return jsonify({"status": "success"})

@app.route("/answer", methods=["POST"])
def answer():
    data = request.get_json()

    selected = data.get("answer")
    curr_index = session.get("current_index", 0)

    session["selected_answers"][curr_index] = selected

    return jsonify({"status": "success"})


@app.route("/result")
def result():
    score = 0

    questions = session["questions"]
    question_indices = session["question_indices"]
    selected_answers = session["selected_answers"]

    for i, q_index in enumerate(question_indices):
        if selected_answers[i] == questions[q_index]["answer"]:
            score += 1

    return render_template('final.html', score=score)


@app.route("/review",methods=['GET'])
def review():
    print('review function entered')
    curr_index = session.get("current_index", 0)
    q=session['questions']

    return render_template(
        "review.html",
        q=q,
        index=curr_index,
        total=8,
        # selected=session["selected_answers"][curr_index]
    )


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)