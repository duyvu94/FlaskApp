import tensorflow as tf

from blueprints import *

from flask import Flask, render_template
app = Flask(__name__)
app.register_blueprint(predict_api)


@app.route('/')
def index():
    return render_template('home.html')


def parse_image(imgData):
    img_str = re.search(b"base64,(.*)", imgData).group(1)
    img_decode = base64.decodebytes(img_str)
    with open('output.png', "wb") as f:
        f.write(img_decode)
    return img_decode

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)


