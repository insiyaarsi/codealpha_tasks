Language Translation Tool

1. Project Description: 

The Language Translation Tool is a simple yet powerful application designed to translate text from one language to another using the Google Translate API. It features a graphical user interface (GUI) built with Tkinter, making it user-friendly and accessible to a wide audience. This project demonstrates the integration of Python's Tkinter library for GUI development with the Google Translate API for machine translation.

2. Installation

   To run this project locally, follow these steps:

   a. Create and Activate a Virtual Environment: 
   
   For Windows - <pre> 
    python -m venv venv <br>
    venv\Scripts\Activate </pre>

   For Mac/Linux - <pre>
   python3 -m venv venv <br>
   source venv/bin/activate </pre>

   b. Install Dependencies:
<pre>
   pip install -r requirements.txt </pre>

3. Usage

   For running the application, in the terminal type : <pre> python main.py </pre>

4. Libraries used:

   googletrans==4.0.0-rc1: For accessing the Google Translate API. <br>
   tkinter: For building the graphical user interface (GUI).

5. File Descriptions
   a. translator.py:<br>
   Contains the function translate_text which handles the text translation using the Google Translate API.
   Imports the LANGUAGES dictionary to provide a list of supported languages.

   b. main.py:

Builds the GUI using Tkinter.
Includes dropdown menus for selecting source and destination languages.
Contains text areas for input and output text.
Implements the on_translate function that ties the GUI to the translation logic.

c. requirements.txt:

Lists all the dependencies required to run the project.
   



   
