
from flask import Flask, render_template, request, redirect, url_for, flash
import bigquery

# Initialize the Flask application
app = Flask(__name__)

# Set the secret key for the application
app.secret_key = 'YOUR_SECRET_KEY'

# Initialize the BigQuery client
client = bigquery.Client()

# Define the home route
@app.route('/')
def home():
    return render_template('index.html')

# Define the route to save the expense data
@app.route('/save_expense', methods=['POST'])
def save_expense():
    # Get the expense data from the form
    expense_name = request.form['expense_name']
    expense_amount = request.form['expense_amount']
    expense_date = request.form['expense_date']

    # Validate the data
    if not expense_name or not expense_amount or not expense_date:
        flash('All fields are required.', 'error')
        return redirect(url_for('home'))

    # Prepare the data to be inserted into BigQuery
    data = [
        {
            'expense_name': expense_name,
            'expense_amount': expense_amount,
            'expense_date': expense_date
        }
    ]

    # Insert the data into BigQuery
    try:
        client.insert_rows_json(
            'your-project.your_dataset.your_table', data
        )
        flash('Expense data saved successfully.', 'success')
        return redirect(url_for('home'))
    except Exception as e:
        flash('Error saving expense data: {}'.format(e), 'error')
        return redirect(url_for('home'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
