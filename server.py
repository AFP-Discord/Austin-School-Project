def webserver(encodedmessage):
    from multiprocessing import Process
    from flask import Flask, render_template
    import os
    import base64
    b64d = base64.b64encode(encodedmessage.encode('ascii'))
    hexd = bytes.hex(b64d)

    app = Flask(__name__)

    @app.route('/')
    def index():
        return '404 PAGE NOT FOUND'

    @app.route('/bWVzc2FnZS1jaGF0')
    def message():
        return hexd

    server = Process(target=app.run(debug=False, host='0.0.0.0'))
    server.start()