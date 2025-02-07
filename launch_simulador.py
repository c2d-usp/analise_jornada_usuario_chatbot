import subprocess
import sys
import os

from source.tests.chatbot_test import test_chatbot

DATABASE_PATH = "checkpoints.db"

# This function initializes the database if it does not exist.
# It does so by creating an initial interaction between the chatbots
def create_database():
    if not os.path.exists(DATABASE_PATH):
        test_chatbot()

def run_streamlit():
    try:
        # Construct the command based on the operating system
        command = ["streamlit", "run", "./tools/visualizador_interacoes/frontend/st_frontend.py"]

        # Execute the command
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Capture output and errors
        for line in process.stdout:
            print(line, end="")

        for err in process.stderr:
            print(err, end="", file=sys.stderr)

        # Wait for process to complete
        process.wait()
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    create_database()
    run_streamlit()
