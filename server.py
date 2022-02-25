def webserver(encodedmessage):
    from multiprocessing import Process
    from flask import Flask, render_template
    import os

    cwd = os.getcwd()
    app = Flask(__name__)

    @app.route('/')
    def index():
        return '404 PAGE NOT FOUND'

    @app.route('/bWVzc2FnZS1jaGF0')
    def message():
        return encodedmessage

    server = Process(target=app.run(debug=False, host='0.0.0.0'))
    server.start()