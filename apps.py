from flask import Flask, render_template, request

app = Flask(__name__)

registrations = []

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        place = request.form['place']
        members = request.form['members']

        registrations.append({
            'name': name,
            'phone': phone,
            'place': place,
            'members': members
        })

    return render_template('index.html', registrations=registrations)

if __name__ == '__main__':
    app.run(debug=True)
