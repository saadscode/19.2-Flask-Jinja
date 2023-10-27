from flask import Flask, render_template, request
from stories import Story

app = Flask(__name__)

# From stories.py starter file
story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/story', methods=['POST'])
def generate_story():
    answers = {
        'place': request.form['place'],
        'noun': request.form['noun'],
        'verb': request.form['verb'],
        'adjective': request.form['adjective'],
        'plural_noun': request.form['plural_noun']

    }

    generated_story = story.generate(answers)

    return render_template('story.html', story=generated_story)
