from flask import Flask, render_template, redirect, url_for
from forms import UploadForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    form = UploadForm()
    if form.validate_on_submit():
        # Handle file uploads, form data, etc.
        # Save files, process instructions, etc.
        return redirect(url_for('success'))
    return render_template('evaluation.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
