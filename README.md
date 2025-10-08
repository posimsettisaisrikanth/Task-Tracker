# TaskIt
A simple Web based Task Tracker for task analysis:

Running the TaskIt App Locally
Follow these steps to set up and run the TaskIt task tracker app on your local machine:

1. Clone the repository
bash
git clone <Repo-link>
cd taskit
2. Create and activate a Python virtual environment
This keeps dependencies isolated for the project.

On Windows:
    python -m venv venv
    venv\Scripts\activate
On macOS/Linux:
    python3 -m venv venv
    source venv/bin/activate
3. Install dependencies:

    pip install -r requirements.txt
4. Run the Streamlit application:


    streamlit run main.py
This command will start the app, normally accessible at http://localhost:8501 in your browser.

5. Add tasks
Enter your task in the input box.

Click the Add button to add the task to your list.

Your tasks will be displayed below the input.

(Note: The app uses Streamlit’s session state to save and display tasks during the session.)
