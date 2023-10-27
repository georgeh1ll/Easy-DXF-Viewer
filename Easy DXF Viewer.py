import ezdxf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mplcursors
import tkinter as tk
from tkinter import filedialog

current_dxf_path = None
current_canvas = None
measure_mode = False
selected_points = []

def plot_line(ax, start, end):
    x_vals = [start[0], end[0]]
    y_vals = [start[1], end[1]]
    ax.plot(x_vals, y_vals, color='k')  # Set color to black

def plot_circle(ax, center, radius):
    circle = plt.Circle((center[0], center[1]), radius, fill=False, color='k')  # Set color to black
    ax.add_artist(circle)

def plot_double_arrow_between_points(ax, start, end):
    arrow_properties = dict(arrowstyle="wedge,tail_width=0.2,shrink_factor=0.1", color='r')
    ax.annotate('', xy=start, xytext=end, arrowprops=arrow_properties)


def plot_distance_label(ax, x, y, distance):
    ax.text(x, y, f"Measurement: {distance:.2f} units", fontsize=12, color='k', ha='center', va='top')  # Set color to black and align top

def translate_entities(entities):
    min_x = float('inf')
    min_y = float('inf')

    # Find the minimum x and y coordinates in the drawing
    for entity in entities:
        if entity.dxftype() == 'LINE':
            min_x = min(min_x, entity.dxf.start[0], entity.dxf.end[0])
            min_y = min(min_y, entity.dxf.start[1], entity.dxf.end[1])
        elif entity.dxftype() == 'CIRCLE':
            min_x = min(min_x, entity.dxf.center[0] - entity.dxf.radius)
            min_y = min(min_y, entity.dxf.center[1] - entity.dxf.radius)
        elif entity.dxftype() == 'LWPOLYLINE':
            vertices = list(entity.get_points('xy'))
            for vertex in vertices:
                min_x = min(min_x, vertex[0])
                min_y = min(min_y, vertex[1])

    # Translate entities based on the minimum x and y coordinates
    for entity in entities:
        if entity.dxftype() == 'LINE':
            entity.dxf.start = (entity.dxf.start[0] - min_x, entity.dxf.start[1] - min_y)
            entity.dxf.end = (entity.dxf.end[0] - min_x, entity.dxf.end[1] - min_y)
        elif entity.dxftype() == 'CIRCLE':
            entity.dxf.center = (entity.dxf.center[0] - min_x, entity.dxf.center[1] - min_y)
        elif entity.dxftype() == 'LWPOLYLINE':
            vertices = list(entity.get_points('xy'))
            new_vertices = [(vertex[0] - min_x, vertex[1] - min_y) for vertex in vertices]
            entity.set_points(new_vertices)

def measure_distance():
    global measure_mode, selected_points

    if measure_mode and len(selected_points) == 2:
        x1, y1 = selected_points[0]
        x2, y2 = selected_points[1]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        # Plot double-ended arrow between the points and display the distance label
        plot_double_arrow_between_points(ax, selected_points[0], selected_points[1])
        plot_distance_label(ax, (x1 + x2) / 2, min(y1, y2), distance)

        current_canvas.draw()

def toggle_measure_mode():
    global measure_mode

    measure_mode = not measure_mode

    if measure_mode:
        measure_button.configure(text="Measure Mode (ON)", bg="green")
        print("Measure mode activated. Click two points to measure the distance.")
    else:
        measure_button.configure(text="Measure Mode", bg="SystemButtonFace")
        print("Measure mode deactivated.")

def remove_measurements():
    global selected_points
    selected_points = []

    # Remove measurement arrows and distance label from the axes
    for annotation in ax.texts + ax.patches:
        annotation.remove()

    current_canvas.draw()

def on_click(event):
    global measure_mode, selected_points
    if measure_mode:
        x, y = event.xdata, event.ydata
        if x is not None and y is not None:
            selected_points.append((x, y))
            if len(selected_points) == 2:
                measure_distance()

def visualize_dxf(dxf_file=None):
    global current_dxf_path, current_canvas, ax

    if current_canvas:
        current_canvas.get_tk_widget().pack_forget()

    if dxf_file is not None:
        current_dxf_path = dxf_file

        doc = ezdxf.readfile(current_dxf_path)
        msp = doc.modelspace()

        # Translate entities to have bottom-left corner at (0,0)
        translate_entities(msp)

        current_figure, ax = plt.subplots()

        for entity in msp:
            if entity.dxftype() == 'LINE':
                plot_line(ax, entity.dxf.start, entity.dxf.end)
            elif entity.dxftype() == 'CIRCLE':
                plot_circle(ax, entity.dxf.center, entity.dxf.radius)
            elif entity.dxftype() == 'LWPOLYLINE':
                vertices = list(entity.get_points('xy'))
                for i in range(len(vertices)):
                    start = vertices[i]
                    end = vertices[i -1]
                    plot_line(ax, start, end)

        ax.set_aspect('equal')
        plt.title('DXF Viewer')

        # Enable interactive data cursor
        mplcursors.cursor(hover=True)

        current_canvas = FigureCanvasTkAgg(current_figure, master=plot_frame)
        current_canvas.mpl_connect('button_press_event', on_click)
        current_canvas.draw()
        current_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Enable the measurement and clear buttons after loading the DXF
        measure_button.config(state=tk.NORMAL)
        clear_button.config(state=tk.NORMAL)
    else:
        # If no DXF is loaded, show a blank canvas
        current_figure, ax = plt.subplots()
        ax.set_aspect('equal')
        plt.title('Easy DXF Viewer')

        current_canvas = FigureCanvasTkAgg(current_figure, master=plot_frame)
        current_canvas.draw()
        current_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Disable the measurement and clear buttons if no DXF is loaded
        measure_button.config(state=tk.DISABLED)
        clear_button.config(state=tk.DISABLED)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        visualize_dxf(file_path)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("DXF Viewer")

    # Set the main window to full-screen
    root.attributes("-fullscreen", True)

    # Configure font for buttons and text
    font = ("Arial", 14, "bold")
    bigger_font = ("Arial", 18, "bold")

    plot_frame = tk.Frame(root)
    plot_frame.pack(fill=tk.BOTH, expand=True)

    # Title label
    title_label = tk.Label(root, text="Easy DXF Viewer", font=bigger_font)
    title_label.pack(pady=20)

    label = tk.Label(root, text="Select a DXF file to view:", font=font)
    label.pack(pady=10)

    open_button = tk.Button(root, text="Open DXF", font=font, command=open_file)
    open_button.pack(pady=5)

    measure_button = tk.Button(root, text="Measure Mode", font=font, command=toggle_measure_mode, state=tk.DISABLED)
    measure_button.pack(pady=5)

    clear_button = tk.Button(root, text="Clear Measurement", font=font, command=remove_measurements, state=tk.DISABLED)
    clear_button.pack(pady=5)

    close_button = tk.Button(root, text="Close", font=font, command=root.quit)
    close_button.pack(pady=5)

    # Developer label in the top-right corner
    developer_label = tk.Label(root, text="Developed by George Hill", font=font)
    developer_label.place(x=root.winfo_screenwidth() - developer_label.winfo_reqwidth() - 10, y=10)

    root.mainloop()
