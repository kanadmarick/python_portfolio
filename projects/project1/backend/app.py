Here is the updated Python code with Google-style docstrings:

```python
"""Flask backend for Project 1."""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    """Route to serve when users visit the site's root URL (/)"""
    return 'Hello from Project 1 Backend!'

if __name__ == '__main__':
    app.run(debug=True)
```
