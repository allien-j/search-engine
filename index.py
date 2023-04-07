from flask import Flask, render_template, request
from unidecode import unidecode
import subprocess


app = Flask(__name__)


def launch_request(string):
    results = []
    if string != "exit":

        jar_process.stdin.write(f"{string}\n".encode())
        jar_process.stdin.flush()

        while True:
            output = jar_process.stdout.readline().decode().strip()
            if output == "Done":
                results.insert(0, int(jar_process.stdout.readline().decode()))
                break

            if output == "No result":
                results.append(output)
                jar_process.stdout.readline().decode()
                break

            results.append(output)
    else:
        results.append("No result")
    return results


@app.route('/', methods=['POST', 'GET'])
def index():
    # On défini notre tableau de résultats
    results = []
    # Si on a une requête, on récupère les éléments de celle-ci
    if request.method == 'POST':
        results = launch_request(unidecode(request.form.get('request')))

    return render_template('index.html', results=results)


if __name__ == '__main__':
    # Lance le programme java
    jar_process = subprocess.Popen(['java', '-jar', 'search-engine.jar'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ready = jar_process.stdout.readline().decode().strip()
    if ready == "Ready":
        time = int(jar_process.stdout.readline().decode())
        print(time / 1000, "s")
    print(ready)
    # Lance l'application web Flask
    app.run()
