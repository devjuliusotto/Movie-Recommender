from flask import Blueprint, render_template, request, redirect, url_for
from .models import Movie
from .forms import MovieForm
from . import db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = MovieForm()
    if form.validate_on_submit():
        movie = Movie(title=form.title.data, genre=form.genre.data)
        db.session.add(movie)
        db.session.commit()
        return redirect(url_for('main.index'))
    movies = Movie.query.all()
    return render_template('index.html', form=form, movies=movies)
