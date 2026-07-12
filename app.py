from flask import (
    Flask,
    render_template,
    request,
    redirect,
    flash,
    send_file,
    url_for
)

from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge

import os

from utils.crypto_utils import encrypt_file, decrypt_file

app = Flask(__name__)

app.secret_key = "ciphervault_secret_key"

app.config["MAX_CONTENT_LENGTH"] = 20 * 1024 * 1024  # 20 MB

UPLOAD_FOLDER = "uploads"
ENCRYPTED_FOLDER = "encrypted"
DECRYPTED_FOLDER = "decrypted"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(ENCRYPTED_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {
    "txt",
    "pdf",
    "docx",
    "png",
    "jpg",
    "jpeg",
    "csv",
    "xlsx",
    "enc"
}


def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        flash("Please select a file.", "danger")
        return redirect(url_for("home"))

    file = request.files["file"]

    if file.filename == "":
        flash("Please choose a file.", "danger")
        return redirect(url_for("home"))

    if not allowed_file(file.filename):
        flash("Unsupported file type.", "danger")
        return redirect(url_for("home"))

    password = request.form.get("password")

    if not password:
        flash("Password is required.", "danger")
        return redirect(url_for("home"))

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    try:

        encrypted_file, stats = encrypt_file(
            filepath,
            password
        )

        flash(
            f"Encryption Successful | "
            f"File: {stats['filename']} | "
            f"Original: {stats['original_size']} KB | "
            f"Encrypted: {stats['encrypted_size']} KB | "
            f"Time: {stats['time_taken']} sec | "
            f"Algorithm: {stats['algorithm']}",
            "success"
        )

        # Delete uploaded file after encryption
        os.remove(filepath)

        return send_file(
            encrypted_file,
            as_attachment=True,
            download_name=filename + ".enc"
        )

    except Exception as e:

        flash(f"Encryption Failed: {e}", "danger")

        return redirect(url_for("home"))

@app.route("/decrypt", methods=["POST"])
def decrypt():

    if "file" not in request.files:
        flash("Please select a file.", "danger")
        return redirect(url_for("home"))

    file = request.files["file"]

    if file.filename == "":
        flash("Please choose a file.", "danger")
        return redirect(url_for("home"))

    if not allowed_file(file.filename):
        flash("Unsupported file type.", "danger")
        return redirect(url_for("home"))

    password = request.form.get("password")

    if not password:
        flash("Password is required.", "danger")
        return redirect(url_for("home"))

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    file.save(filepath)

    try:

        decrypted_file = decrypt_file(
            filepath,
            password
        )

        flash("🔓 File decrypted successfully!", "success")

        # Delete uploaded encrypted file
        os.remove(filepath)

        return send_file(
            decrypted_file,
            as_attachment=True,
            download_name=filename.replace(".enc", "")
        )

    except Exception as e:

        flash(
            f"Decryption Failed: {e}",
            "danger"
        )

        return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)