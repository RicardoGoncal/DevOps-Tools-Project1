from werkzeug.utils import secure_filename
import os


def upload_file(request):

    if request.method == 'POST':

        cwd = os.getcwd() + '/files'

        print(cwd)

        f = request.files['data']

        file_name = f.filename
        destino = '/'.join([cwd, file_name])

        print(destino)

        f.save(destino)

        response = 'vai cagar'

        return response
   