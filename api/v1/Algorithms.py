from datetime import datetime
import json
import sys

class Algos:
    
    ALLOWED_EXTENSIONS = ['csv']
    ''' Allowed Files '''
    @staticmethod
    def allowed_file(filename):
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in Algos.ALLOWED_EXTENSIONS

    """
        Log an error
    """
    @staticmethod
    def write_log(app, msg, msg_type):
        t = datetime.now()
        str_time = t.strftime("%Y-%m-%d %H:%M:%S")
        msg = str_time + " | " + msg
        if msg_type == 'error':
            app.logger.error(msg)
        else:
            app.logger.info(msg)

