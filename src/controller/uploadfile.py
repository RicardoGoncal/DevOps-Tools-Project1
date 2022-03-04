from werkzeug.utils import secure_filename
import os
import src.infra.utility.generator as generator

UPLOAD_FOLDER = os.getcwd() + '/files'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'csv'}

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def uploadfile(request):

    if request.method == 'POST':

        if 'file' not in request.files:
            response = 'No file part'
        
        file = request.files['file']

        if file.filename == '':
            response = 'No selected file'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)

            id = generator.Generator.radom_string_number()
            filename = id + '_' + filename

            destination = '/'.join([UPLOAD_FOLDER,filename])
            file.save(destination)
            response = 'Upload complete'

        return response
        