import os

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from rag import create_vector_store, ask_question

app = Flask(__name__)

UPLOAD_FOLDER = "data"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_pdf():

    if "pdf" not in request.files:
        return render_template(
            "index.html",
            message="Please select a PDF file."
        )

    file = request.files["pdf"]

    if file.filename == "":
        return render_template(
            "index.html",
            message="Please select a PDF file."
        )

    if not file.filename.lower().endswith(".pdf"):
        return render_template(
            "index.html",
            message="Only PDF files are supported."
        )

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(filepath)

    try:
        create_vector_store(filepath)

        return render_template(
            "index.html",
            message=f"{filename} processed successfully! You can now ask questions."
        )

    except Exception as e:
        return render_template(
            "index.html",
            message=f"Error processing PDF: {str(e)}"
        )


@app.route("/ask", methods=["POST"])
def ask():

    question = request.form.get("question", "").strip()

    if not question:
        return render_template(
            "index.html",
            message="Please enter a question."
        )

    try:
        answer = ask_question(question)

        return render_template(
            "index.html",
            question=question,
            answer=answer,
            message="Document ready."
        )

    except Exception as e:
        return render_template(
            "index.html",
            message=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    app.run(debug=True)