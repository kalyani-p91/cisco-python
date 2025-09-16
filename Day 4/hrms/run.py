import sys
print("sys.path:", sys.path)
from app.routes import application

if __name__ == "__main__":
    application.run(debug=True)