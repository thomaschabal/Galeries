import os
import shutil

def is_image(filename):
    """ Renvoie True si le fichier possede une extension d'image valide. """
    return '.' in filename and filename.rsplit('.', 1)[-1] in ('png', 'jpg', 'jpeg', 'gif', 'bmp')

def is_video(filename):
    """ Renvoie True si le fichier possede une extension de vidéo valide. """
    return '.' in filename and filename.rsplit('.', 1)[-1] in ('mp4', 'avi', 'mov')

def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. {}'.format(directory))

def delete_folder(directory):
    try:
        if os.path.exists(directory):
            shutil.rmtree(directory)
    except OSError:
        print('Error: Deleting directory. {}'.format(directory))

def copy_folder(src, dest):
    try:
        shutil.copytree(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('Directory not copied. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('Directory not copied. Error: %s' % e)

def move_file(src, dest):
    try:
        shutil.move(src, dest)
    # Directories are the same
    except shutil.Error as e:
        print('File not moved. Error: %s' % e)
    # Any error saying that the directory doesn't exist
    except OSError as e:
        print('File not moved. Error: %s' % e)

def ext(filename):
    _, extension = filename.rsplit('.', 1)
    return extension
