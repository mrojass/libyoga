from flask import Flask, jsonify, redirect, render_template, request, url_for
from werkzeug import secure_filename
from lib.geometry import hough, edge
import os

# Initialize Flask app
app = Flask(__name__)

# This is the path to the upload directory
app.config['UPLOAD_FOLDER'] = 'api/uploads/'
# These are the extension that we are accepting to be uploaded
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg'])

# For a given file, return whether it's an allowed type or not
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

# Redirect to API url
@app.route('/')
def index():
    return redirect(url_for('api'))


@app.route('/images')
def layout_images():
    return render_template('index.html')

# API welcome message!
@app.route('/api/')
def api():
    return 'You are using the libyoga API. Congratulations.'


# Add a new image (through an upload)
@app.route('/api/images', methods=['POST'])
def images():
    file1 = request.files['file1']
    if file1 and allowed_file(file1.filename):
        # Make the filename safe, remove unsupported chars
        filename = secure_filename(file1.filename)
        # Move the file form the temporal folder to
        # the upload folder we setup
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file2 = '../img/partner-A/gs-edge-females.jpg'

        # Process image and calculate score
        edge.edge('api/uploads/' + filename, 'api/img/gs-edge-' + filename)
        print filename
        score = hough.lines('api/img/gs-edge-females.jpg', 'api/img/gs-edge-' + filename)

        return (
            jsonify(
                status=200,
                message='You have successfully received your score.',
                score=score
            ),
            200
        )
    return jsonify(status=500, message='New image resource not uploaded.'), 500

# Get data about a particular image
@app.route('/api/images/<int:id>')
def image(id):
    return 'Got image #' + str(id)


# Respond to 404 errors (aka resource not found)
@app.errorhandler(404)
def page_not_found(error):
    return jsonify(error='404', message='Resource not found.'), 404

if __name__ == '__main__':
    app.run(debug=True)
