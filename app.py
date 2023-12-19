from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = 'greentreemonitor1357'
debug = DebugToolbarExtension(app)

global selected_story
selected_story = None

@app.route('/')
def home_page():
    return render_template('home.html', stories=stories)

@app.route('/madlibs')
def madlibs():
    type = request.args['type']
    global selected_story
    selected_story = stories.get(type)
    app.logger.info('%s', type)
    return render_template('madlibs.html', prompts=selected_story.prompts)

@app.route('/story')
def story():
    words = {k:v.upper() for k, v in request.args.items()}
    global selected_story
    story = selected_story.generate(words)
    app.logger.info('%s', words)
    return render_template('story.html', story=story)

