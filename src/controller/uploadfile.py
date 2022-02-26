from werkzeug.utils import secure_filename
import os

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
            destination = '/'.join([UPLOAD_FOLDER,filename])
            file.save(destination)
            response = 'Upload complete'

        return response
        
        # destination = os.getcwd() + '/files'
        # print(destination)
        # if os.path.isdir(destination):
        # f = request.files['data']
        # file_name = f.filename
        # destino = '/'.join([destination, file_name])
        # print(destino)
        # f.save(destino)
        # response = 'vai cagar'
        # return response
   