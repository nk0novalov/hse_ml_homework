from flask import Flask, render_template,request
import ml_pipeline

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template("index.html")


@app.route('/process', methods=["GET", "POST"])
def run_processing():
    return ml_pipeline.exe_pipeline(request.args.get('promt'))

if __name__ == '__main__':
    app.run()
