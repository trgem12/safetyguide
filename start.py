from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")  # 127.0.0.1
def index():
    # 'templates' 폴더에서 'index.html' 템플릿을 렌더링합니다.
    return render_template("index.html")

@app.route("/<string:page_name>.html")  # 다른 HTML 페이지에 대한 동적 라우트
def show_page(page_name):
    return render_template(f"{page_name}.html")

if __name__ == "__main__":
    app.run(debug=True)
