from flask import Flask, render_template, request, redirect, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for flashing messages

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Form submission route
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    phone = request.form.get('phone')
    class_level = request.form.get('class')

    # Basic validation
    if not name or not phone or not class_level:
        flash("All fields are required!", "error")
        return redirect('/#contact')

    # 🧠 Here you can replace this with saving to DB or sending email
    print(f"📞 Callback Request: {name} | {phone} | Class: {class_level} | {datetime.now()}")

    flash("✅ Your request has been received! We'll call you soon.", "success")
    return redirect('/#contact')


if __name__ == '__main__':
    app.run(debug=True)
