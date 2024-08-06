import subprocess
import flask

app = flask.Flask(__name__)

@app.route("/")
def ui():
    return flask.render_template('index.html')

@app.route("/api/<path:command>")
def api_cmd(command):
    print(f'Command: {command}')
    with subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as process:
        stdout, stderr = process.communicate()
    response = {
        'output': stdout.decode(),
        'error': stderr.decode()
    }
    print(f'Response: {response}')
    return flask.jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999, debug=True, threaded=True)
