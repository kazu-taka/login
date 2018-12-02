from flask import Flask, request, render_template

app = Flask(__name__)


# ログイン画面表示と、送信ボタンを押した時の処理が別のパターン
@app.route("/login", methods=["GET"])
def login():
    return render_template("login2.html")


@app.route("/login_action", methods=["POST"])
def login():
    return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)
