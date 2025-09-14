
from flask import Flask, render_template, request, redirect, url_for, flash # pyright: ignore[reportMissingImports]

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Needed for flash messages

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # For demo, we just flash a message and redirect to contact
        if not name or not email or not message:
            flash('Please fill all fields.', 'error')
        else:
            flash('Thank you for contacting us!', 'success')
            # Here you could add code to save to a database or send an email

        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
