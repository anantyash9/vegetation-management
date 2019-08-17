from flask import Flask
import simple_out
app = Flask(__name__)


@app.route('/forward')
def f():
    simple_out.forward()
    return "Going forward"

@app.route('/backward')
def b():
    simple_out.backward()
    return "backward"

@app.route('/stop')
def s():
    simple_out.stop()
    return "stop"
if __name__ == '__main__':
    app.run(host='0.0.0.0')
