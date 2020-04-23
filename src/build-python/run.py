import logging
import http.server
import socketserver
import getpass

class MyHTTPHlandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        logging.info("%s - - [%s] %s\n"% (
            self.client_address[0],
            self.log_date_time_string(),
            format%args
        ))

logging.basicConfig(
    filename='/log/http-server.log',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

logging.getLogger().addHandler(logging.StreamHandler())
logging.info('Inicializando...')
PORT = 8000

httpd = socketserver.TCPServer(("", PORT), MyHTTPHlandler)
logging.info('Escutando a porta: %s', PORT)
logging.info('Usuário: %s', getpass.getuser())
httpd.serve_forever()
