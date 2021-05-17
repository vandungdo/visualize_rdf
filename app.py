from flask import Flask, render_template, request, url_for
import json
import os
from werkzeug.utils import secure_filename
from read_rdf_turtle import rdf_2_json

app = Flask(__name__)

uploadDir = os.path.join(os.path.dirname(__file__),'data')
print(uploadDir)
@app.route('/', methods = ['GET', 'POST'])
def index():
    # f = {
    #         'nodes':[{'id':'x','name':'x'},{'id':'y','name':'y'},{'id':'z','name':'z'}],
    #         'links':[
    #             {'source':'x','target':'y','type':'a'},
    #             {'source':'y','target':'z','type':'b'},
    #             {'source':'z','target':'x','type':'c'}
    #         ]
    #     }
    # graph = json.dumps(f, indent=4)

    if request.method == 'POST':
        fileUploaded = request.files['upload_file']
        fileUploaded.save(os.path.join(uploadDir, secure_filename(fileUploaded.filename)))
        graph = rdf_2_json(os.path.join(uploadDir, secure_filename(fileUploaded.filename)))
    else:
        fileUploaded = ''
        graph = ''
    return render_template('index.html', graph = graph)

if __name__ == '__main__':
    app.run(debug=True)