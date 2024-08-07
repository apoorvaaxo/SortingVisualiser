from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random
import sys
from random import uniform

SORT_NO = 5  # Updated number of sorting algorithms
MAX = 5  # Number of values the array can take
SPEED = 1000
sort_menu = 1
a = [0 for i in range(MAX)]
sorted_indices = [False for _ in range(MAX)]  # Track which indices are sorted
swapflag = 0
i, j = 0, 0
flag = 0
dirflag = 0
count = 0
k = 1
sorting = 0
sort_count = 1
sort_string = [0, 'BubbleSort', 'InsertionSort', 'QuickSort', 'MergeSort', 'SelectionSort']

def bitmap_output(x, y, st):
    glRasterPos2f(x, y)
    for char in st:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))

def display_text():
    global sorting
    glColor3f(1, 0, 1)
    bitmap_output(150, 665, "Sorting Visualizer")
    bitmap_output(10, 625, 'This program sorts a random set of numbers in ascending order')
    bitmap_output(10, 605, 'Bars with varying height')
    
    if sort_menu == 0:
        bitmap_output(10, 575, 'Menu')
        bitmap_output(10, 555, 'Press S to SORT')
        bitmap_output(10, 535, 'Press c to select the sort algorithm')
        bitmap_output(10, 515, 'Press r to randomize')

        if sort_count == 1:
            bitmap_output(150, 495, 'Bubble sort selected')
        elif sort_count == 2:
            bitmap_output(150, 495, 'Insertion sort selected')
        elif sort_count == 3:
            bitmap_output(150, 495, 'Quick sort selected')
        elif sort_count == 4:
            bitmap_output(150, 495, 'Merge sort selected')
        elif sort_count == 5:
            bitmap_output(150, 495, 'Selection sort selected')
    elif sort_menu == 1:
        glColor3f(0.5, 0.5, 0.5)
        bitmap_output(10, 555, 'Choose sorting algorithm:')
        bitmap_output(10, 535, '')  # Empty line for spacing

        bitmap_output(10, 515, 'Press i for insertion sort')
        bitmap_output(10, 495, '')  # Empty line for spacing

        bitmap_output(10, 475, 'Press b for bubble sort')
        bitmap_output(10, 455, '')  # Empty line for spacing

        bitmap_output(10, 435, 'Press q for quick sort')
        bitmap_output(10, 415, '')  # Empty line for spacing

        bitmap_output(10, 395, 'Press m for merge sort')
        bitmap_output(10, 375, '')  # Empty line for spacing

        bitmap_output(10, 355, 'Press s for selection sort')


        glColor3f(0.0, 0.0, 0.0)

    if sorting == 0 and not notsorted():
        glColor3f(0, 1, 0)
        bitmap_output(300, 450, "Sorting Completed")

def Initialise():
    global MAX, a, sorted_indices
    for temp in range(MAX):
        a[temp] = random.randint(0, 101)
    sorted_indices = [False for _ in range(MAX)]  # Reset sorted indices

    global i, j, dirflag, count, flag
    i = j = dirflag = flag = 0
    count = 1
    glClearColor(0.9, 0.9, 0.9, 0.9)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 699, 0, 799)

def notsorted():
    global MAX, a
    for q in range(MAX - 1):
        if a[q] > a[q + 1]:
            return 1
    return 0

def display():
    global k, MAX, a, swapflag, sorting, j, sort_menu, sorted_indices

    glClear(GL_COLOR_BUFFER_BIT)
    if k == 1:
        display_text()
        if sort_menu == 0:
            bar_width = (700 / (MAX + 1)) * 0.8  # Bar width reduced to 80% of the space
            gap_width = (700 / (MAX + 1)) * 0.2  # Gap width is 20% of the space

            for ix in range(MAX):
                color = [uniform(0.0, 1.0) for _ in range(3)]
                if sorted_indices[ix]:  # If the index is sorted, color it blue
                    color = [0, 0, 1]
                glColor3fv(color)
                glBegin(GL_POLYGON)
                glVertex2f(10 + ix * (bar_width + gap_width), 50)
                glVertex2f(10 + ix * (bar_width + gap_width) + bar_width, 50)
                glVertex2f(10 + ix * (bar_width + gap_width) + bar_width, 50 + a[ix] * 4)
                glVertex2f(10 + ix * (bar_width + gap_width), 50 + a[ix] * 4)
                glEnd()

                glColor3f(0, 0, 0)  # Text color black for better visibility
                bitmap_output(12 + ix * (bar_width + gap_width), 35, str(a[ix]))

    glFlush()

# Bubble Sort
def bubblesort():
    global i, j, MAX, a, swapflag, sorting, sorted_indices
    if i < MAX - 1:
        if j < MAX - 1 - i:
            if a[j] > a[j + 1]:
                swapflag = 1
                a[j], a[j + 1] = a[j + 1], a[j]  # Swap elements
            j += 1
        else:
            sorted_indices[MAX - 1 - i] = True  # Mark the sorted index
            j = 0
            i += 1
    else:
        sorting = 0  # Sorting complete
        sorted_indices = [True for _ in range(MAX)]  # Mark all as sorted

# Insertion Sort
def insertionsort():
    global i, j, MAX, a, swapflag, sorting, sorted_indices
    if i < MAX:
        if j > 0 and a[j] < a[j - 1]:
            swapflag = 1
            a[j], a[j - 1] = a[j - 1], a[j]  # Swap elements
            j -= 1
        else:
            sorted_indices[j] = True  # Mark the sorted index
            i += 1
            j = i
    else:
        sorting = 0  # Sorting complete
        sorted_indices = [True for _ in range(MAX)]  # Mark all as sorted

# Quick Sort
MAX = 5  # Define the maximum number of elements
a = [5, 3, 4, 2, 1, 0]  # Example list to sort

def quicksort(low, high):
    global sorting
    if low < high:
        pi = partition(low, high)
        quicksort(low, pi - 1)
        quicksort(pi + 1, high)

    if low == 0 and high == MAX - 1:  # When the entire list has been processed
        mark_sorted()
        sorting = 0  # Sorting complete

def partition(low, high):
    global a, sorted_indices
    pivot = a[high]
    i = low - 1
    for j in range(low, high):
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[high] = a[high], a[i + 1]
    sorted_indices[i + 1] = True
    return i + 1

def mark_sorted():
    global sorted_indices
    sorted_indices = [True for _ in range(MAX)]  # Mark all as sorted

# Initialize global variables
sorting = 1
sorted_indices = [False for _ in range(MAX)]  # Initially, none are sorted

# Run the quicksort algorithm
quicksort(0, MAX - 1)



# Merge Sort
MAX = 5  # Define the maximum number of elements
a = [5, 3, 4, 2, 1, 0]  # Example list to sort

def mergesort(low, high):
    global sorting
    if low < high:
        mid = (low + high) // 2
        mergesort(low, mid)
        mergesort(mid + 1, high)
        merge(low, mid, high)
    
    if low == 0 and high == MAX - 1:  # When the entire list has been processed
        mark_sorted()
        sorting = 0  # Sorting complete

def merge(low, mid, high):
    global a, sorted_indices
    left = a[low:mid + 1]
    right = a[mid + 1:high + 1]
    k = low
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            i += 1
        else:
            a[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        a[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a[k] = right[j]
        j += 1
        k += 1

    for index in range(low, high + 1):
        sorted_indices[index] = True

def mark_sorted():
    global sorted_indices
    sorted_indices = [True for _ in range(MAX)]  # Mark all as sorted

# Initialize global variables
sorting = 1
sorted_indices = [False for _ in range(MAX)]  # Initially, none are sorted

# Run the mergesort algorithm
mergesort(0, MAX - 1)


# Selection Sort
def selectionsort():
    global i, j, MAX, a, swapflag, sorting, sorted_indices
    if i < MAX - 1:
        min_idx = i
        for j in range(i + 1, MAX):
            if a[j] < a[min_idx]:
                min_idx = j
        
        if min_idx != i:
            swapflag = 1
            a[i], a[min_idx] = a[min_idx], a[i]  # Swap elements
        sorted_indices[i] = True  # Mark the index as sorted
        i += 1
    else:
        sorting = 0  # Sorting complete
        sorted_indices = [True for _ in range(MAX)]  # Mark all as sorted

def makedelay(_):
    global sorting, sort_count
    if sorting:
        if sort_count == 1:
            bubblesort()
        elif sort_count == 2:
            insertionsort()
        elif sort_count == 3:
            quicksort(0, MAX - 1)
        elif sort_count == 4:
            mergesort(0, MAX - 1)
        elif sort_count == 5:
            selectionsort()
    glutPostRedisplay()
    glutTimerFunc(SPEED, makedelay, 10)

def keyboard(key, x, y):
    global k, sorting, sort_count, SORT_NO, sort_menu
    k = 1
    if k == 1 and sorting != 1:
        if key == b'\x1b':  # Escape key
            sys.exit()
        elif key == b'S':
            sorting = 1
            sort_menu = 0
        elif key == b'r':
            sort_menu = 0
            Initialise()
        elif key == b'c':
            sort_menu = 1
            sort_count = (sort_count + 1) % SORT_NO
        elif key == b'b':
            sort_count = 1
            sort_menu = 0
        elif key == b'i':
            sort_count = 2
            sort_menu = 0
        elif key == b'q':
            sort_count = 3
            sort_menu = 0
        elif key == b'm':
            sort_count = 4
            sort_menu = 0
        elif key == b's':
            sort_count = 5
            sort_menu = 0

    if k == 1 and sorting == 1:
        if key == b'p':
            sorting = 0

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Sorting Algorithms Visualizer")
    Initialise()
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutTimerFunc(100, makedelay, 10)
    glutMainLoop()

if __name__ == "__main__":
    main()
