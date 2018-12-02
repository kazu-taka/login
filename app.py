from flask import Flask, request, render_template

app = Flask(__name__)


# ログイン画面表示と、送信ボタンを押した時の処理が同じパターン
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template("login.html")

    if request.method == 'POST':
        return render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)
