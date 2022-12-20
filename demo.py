print("HI THIS IS DURGA PRASAD")
print("THIS IS SIRISHA")
from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def demo():
    return render_template('index.html')


if __name__ == '__main__':
    app.run();