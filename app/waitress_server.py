import sys
import hupper


def main(args=sys.argv[1:]):
    from app.webapp import app
    if '--reload' in args:
        reloader = hupper.start_reloader('app.waitress_server.main')
        reloader.watch_files(['foo.ini'])

    app.run(host='0.0.0.0', port=5000)
