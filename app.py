from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Activity 3: Implementing Stack data structure
# Using a list to mimic Stack LIFO behavior
data_stack = []

@app.route('/')
def index():
    # Activity 1: Displaying values in the DataGridView (HTML Table)
    return render_template('index.html', stack=data_stack)

@app.route('/push', methods=['POST'])
def push():
    # Activity 2: Inserting values at run time
    item = request.form.get('item')
    if item:
        data_stack.append(item) 
    return redirect(url_for('index'))

@app.route('/pop', methods=['POST'])
def pop():
    # Removing from stack
    if data_stack:
        data_stack.pop()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)