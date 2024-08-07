
---

# Sorting Algorithms Visualizer using OpenGL and Python

## Overview

This project aims to develop an interactive sorting algorithm visualizer using OpenGL and Python. The primary objective is to visually demonstrate the functioning of various sorting algorithms, aiding in better understanding and educational purposes. The visualizer will display the sorting process in real-time, highlighting the comparisons and swaps made by the algorithm.

### Objectives

1. To create a visual representation of sorting algorithms.
2. To enhance the understanding of sorting algorithms through visualization.
3. To develop an interactive tool for educational purposes.
4. To provide a platform for comparing the performance of different sorting algorithms.

## User Interface

The user interface of the Sorting Algorithms Visualizer is designed to be intuitive and user-friendly, providing users with clear instructions and easy access to various features and functionalities. The interface guides users through the process of visualizing different sorting algorithms, allowing them to interact with the visualizer and customize their learning experience.

### Interface Components

1. **Main Window:**
   - **Title:** "Sorting Algorithms Visualizer"
   - **Description:** A brief description of the visualizer and its purpose.
   - **Menu Instructions:** Clear instructions on how to use the visualizer, including key bindings for different actions.

2. **Menu Options:**
   - **Press S to SORT:** Initiates the sorting process using the selected algorithm.
   - **Press C to select the sort algorithm:** Allows users to choose between different sorting algorithms (e.g., Insertion Sort, Selection Sort).
   - **Press R to randomize:** Randomizes the data set to be sorted.

3. **Algorithm Selection:**
   - Display the currently selected sorting algorithm (e.g., "Insertion sort selected" or "Selection sort selected").
   - Provide visual feedback to indicate the selected algorithm.

4. **Sorting Visualization Area:**
   - A graphical representation of the data set to be sorted.
   - Bars of varying heights representing different values in the data set.
   - Real-time animation of the sorting process, showing the movement and comparison of bars.

5. **Status Messages:**
   - Display messages indicating the current status of the sorting process (e.g., "Sorting Completed").

6. **Interaction Instructions:**
   - Provide clear instructions on how to interact with the visualizer using keyboard inputs.

### User Interaction

- **Initiating Sorting:** Users press the 'S' key to start sorting the data set using the currently selected algorithm.
- **Selecting Algorithms:** Users press the 'C' key to cycle through available sorting algorithms, with the selected algorithm displayed on the screen.
- **Randomizing Data:** Users press the 'R' key to generate a new random data set, resetting the visualization area for a new sorting demonstration.
- **Real-Time Feedback:** The interface provides immediate visual and textual feedback based on user actions, ensuring a responsive and engaging experience.
### SNAPSHOTS : 
To run the project i used anaconda prompt: 
![image](https://github.com/user-attachments/assets/2af3ce38-4fba-49de-b0cc-33edc0b73e0d)

1. Interface :
   ![image](https://github.com/user-attachments/assets/5319f941-16bf-429c-a508-5e2f3d456841)
2. Insertion sort selected
   ![image](https://github.com/user-attachments/assets/c42d1dcd-c4b2-4f05-a498-6f849a3fa285)
3. Sorted using Insertion Sort
  ![image](https://github.com/user-attachments/assets/c6c65c17-1acb-4ff9-af05-e2541c967d99)

### VIDEO DEMONSTRATION :

https://github.com/user-attachments/assets/c940be26-4189-4521-b83e-e1892c645669



### Visual Design

- **Color Scheme:** Utilize contrasting colors for different elements (e.g., bars, text) to enhance visibility and readability.
- **Font Style:** Use clear and legible fonts for instructions and status messages.
- **Layout:** Arrange interface components logically to ensure ease of use, with the menu options and visualization area prominently displayed.

## Purpose

The purpose of this project is to enhance the understanding of sorting algorithms by providing an interactive and engaging visualization tool. It aims to bridge the gap between theoretical concepts and practical comprehension, allowing learners to observe the step-by-step execution of various sorting techniques in real-time. This tool offers a more intuitive and tangible learning experience compared to traditional text-based or static image resources.

## Scope

The scope of this project encompasses the development of an interactive sorting algorithm visualizer that supports various sorting techniques, including Insertion Sort, Selection Sort, and others. The project aims to provide users with the ability to:

1. Visualize the sorting process step-by-step for better understanding.
2. Interact with the visualization by selecting different sorting algorithms.
3. Randomize the input data to see how different algorithms handle various data sets.
4. Use the visualizer across different platforms due to its reliance on OpenGL and GLUT, ensuring compatibility and ease of use.

The project is intended for students, educators, and anyone interested in gaining a deeper understanding of sorting algorithms through an engaging, hands-on approach.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sorting-algorithms-visualizer.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd sorting-algorithms-visualizer
   ```

3. **Install Dependencies:**
   - Make sure you have Python installed and then install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the Application:**
   ```bash
   python sortingvisualiser.py
   ```
## Acknowledgments

- **OpenGL:** For 3D graphics rendering.
- **Python:** For providing the programming language.
- **GLUT:** For creating the window and handling input.

---
