from APIs import create_app, db
from APIs.config import port

# calling the factory function
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=port)
