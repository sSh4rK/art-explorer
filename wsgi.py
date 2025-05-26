from waitress import serve
from app import create_app

if __name__ == '__main__':
    app = create_app()
    print('Starting Waitress server...')
    print('Application will be available at: http://localhost:8000')
    serve(app, host='0.0.0.0', port=8000, threads=6) 