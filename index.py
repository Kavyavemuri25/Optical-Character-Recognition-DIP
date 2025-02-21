from flask import Flask, request, render_template
import tasks
output = ""
app = Flask(__name__)
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        message = tasks.construct(request.files['image'])
        print("This is the output {}".format(message))
        output = message[:-1].lstrip()
        f = open("output.txt", "w")
        f.write(output)
        f.close()
        f = open("output.txt", "r")
        output = f.read()
        f.close()
        return open("templates/display.html").read().format(variable=output)
    else:
        return render_template('form1.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/info')
def info():
    return render_template('info.html')

if __name__ == '__main__':
    app.run()
