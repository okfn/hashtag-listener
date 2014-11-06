from flask import render_template, request, abort, json, send_from_directory
from app import app, db
import models as m


@app.route('/')
def index():
    params = {
        'title': 'Hashtag Listener',
    }
    return render_template('index.html', **params)


@app.route('/api', methods=['POST'])
def api():
    auth = request.headers.get('Authorization')
    if auth != app.config['APIKEY']:
        return json.dumps({'success': False, 'message': 'Not authorized'}), 400
    data = request.get_json(force=True)
    if not data:
        return json.dumps({'success': False, 'message': 'JSON data not found '
                           'or mimetype not set'}), 400
    try:
        entry = m.Entry(
            username=data.get('username'),
            entry_type=data.get('type'),
            entry_text=data.get('text')
        )
    except m.ValidationError:
        return json.dumps({'success': False, 'message': 'Validation error with'
                          ' the data provided'}), 400
    db.session.add(entry)
    db.session.commit()
    return json.dumps({'success': True})


@app.route('/entry/<name>')
def entry_show(name=None):
    params = {
        'title': ''.join(['#', name]),
        'data': m.Entry.query.filter_by(entry_type=name)
                       .order_by(m.Entry.created.desc()).all()
    }
    return render_template('entry.html', **params)


@app.route('/robots.txt')
def robots():
    return send_from_directory(app.static_folder, request.path[1:])
