# Shared Spaces Application

This application is a graphical user interface (GUI) built using Python, which allows users to create and visualize 3D shapes in a virtual space. It incorporates audio features, interactive dialogs, and a visually appealing background.

## Features

- **3D Shape Creation**: Users can create various shapes (Cube, Sphere, Pyramid) at specified coordinates in a 3D environment using VPython.
- **Text-to-Speech**: The application utilizes the `pyttsx3` library to read aloud prompts and user inputs, enhancing accessibility.
- **Graphical User Interface**: Built with `tkinter`, the GUI provides an intuitive interface for interaction, including buttons and input dialogs.
- **Customizable Background**: Users are greeted with a custom background image that enhances the visual appeal of the application.

## Requirements

To run this application, you need to have the following Python libraries installed:


- `vpython`
- `pygame`
- `tkinter` (comes with standard Python installations)
- `pyttsx3`

You can install the necessary libraries using pip:

```bash
pip install vpython pygame pyttsx3
```

## Usage Instructions
Start the Application: Launch the application, and you will see the welcome interface.
Create Shapes:
Click the "Start" button to initiate shape creation.
Follow the prompts read aloud to enter the number of shapes you want to create.
Specify the type of shape (Cube, Sphere, Pyramid) and its position coordinates (x, y, z).
Visualize Shapes: The created shapes will be displayed in the 3D space.
Thank You Page: After creating the shapes, a "Thank You" page will appear to conclude the interaction.

## Code Overview
The main functionalities are encapsulated in several functions:
start_button_clicked(): Initializes the audio and starts the shape creation process.
display_thank_you_page(): Displays a thank-you message after shape creation.
speak_text(text): Uses text-to-speech to read aloud provided text.
create_shape(shape_type, x, y, z): Generates the specified shape at the given coordinates.
