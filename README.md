# Easy-DXF-Viewer
![Screenshot 2023-07-29 195253](https://github.com/georgeh1ll/Easy-DXF-Viewer/assets/11806169/654db9c5-e5e0-4d3b-96b1-54d3fc53a820)

DXF Viewer is a simple Python application that allows users to view and measure distances in DXF (Drawing Exchange Format) files. The application provides a graphical user interface (GUI) for loading DXF files, visualizing them on a canvas, and enabling a measure mode for distance measurement between two points.

**Features
**

Open and view DXF files.
Measure distances between two points in the DXF file.

**Requirements for Python Verison
**

Python 3.x
ezdxf (to handle DXF files)
Matplotlib (for plotting)
Tkinter (for the GUI)

**How to Use
**

Clone the repository to your local machine.

Install the required libraries using pip:
pip install ezdxf matplotlib
Run the dxf_viewer.py script:
python dxf_viewer.py
The application will open in full-screen mode, and you will see the "Open DXF" button.

Click the "Open DXF" button to load a DXF file for viewing.

After loading the DXF file, the "Measure Mode" and "Clear Measurement" buttons will become active.

Click the "Measure Mode" button to activate measure mode.

Click on two points in the DXF plot to measure the distance between them.

The distance will be displayed on the plot.

Click the "Clear Measurement" button to remove the measurement arrows and distance label and take a new measurement.
