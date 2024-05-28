### Flask Application Design for Saving Expense Data to BigQuery

**HTML Files**

- `index.html`: The landing page for the application, which will have a form for capturing expense details.
- `success.html`: A page displayed upon successful submission of expense data, confirming the data insertion.
- `error.html`: A page displayed if there is an error during data submission, providing a detailed error message.

**Routes**

- `/`: The route that renders the `index.html` landing page.
- `/save_expense`: The route that handles the POST request upon form submission. Here's the explanation of the functional aspects of the route:
   - It receives the expense data from the form.
   - It validates the data to ensure all necessary fields are present and in the correct format.
   - It prepares the data to be inserted into BigQuery.
   - It inserts the data into BigQuery, handling any potential errors.
   - It redirects to `success.html` if the insertion is successful, displaying a confirmation message.
   - It redirects to `error.html` if there is an error during insertion, providing the error details.