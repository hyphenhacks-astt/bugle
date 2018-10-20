from flask import render_template, flash, redirect, url_for, session, request, g, abort
from app import app#, db, lm
from .forms import InputForm

@app.route('/', methods=['GET','POST'])
def index():
    form=InputForm()
    if form.validate_on_submit():
        pass
    return render_template('index.html',form=form)

@app.errorhandler(404)
def error_404(error):
    return redirect(url_for("index"))

@app.errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500