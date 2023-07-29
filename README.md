# Easy-DXF-Viewer
![Screenshot 2023-07-29 195253](https://github.com/georgeh1ll/Easy-DXF-Viewer/assets/11806169/654db9c5-e5e0-4d3b-96b1-54d3fc53a820)

**DXF Viewer** is a simple Python application that allows users to view and measure distances in DXF (Drawing Exchange Format) files. The application provides a graphical user interface (GUI) for loading DXF files, visualizing them on a canvas, and enabling a measure mode for distance measurement between two points.

## Features

- Open and view DXF files.
- Measure distances between two points in the DXF file.
- Display double-ended arrows and the distance value for measurements.
- Clear measurement arrows and distance labels for taking new measurements.
- Developed using Python and the Tkinter and Matplotlib libraries.

## Requirements

- Python 3.x
- ezdxf (to handle DXF files)
- Matplotlib (for plotting)
- Tkinter (for the GUI)

## How to Use

1. Clone the repository to your local machine.
2. Install the required libraries using pip:
3. Run the `dxf_viewer.py` script: dxf_viewer.py

4. The application will open in full-screen mode, and you will see the "Open DXF" button.
5. Click the "Open DXF" button to load a DXF file for viewing.
6. After loading the DXF file, the "Measure Mode" and "Clear Measurement" buttons will become active.
7. Click the "Measure Mode" button to activate measure mode.
8. Click on two points in the DXF plot to measure the distance between them.
9. The distance will be displayed on the plot.
10. Click the "Clear Measurement" button to remove the measurement arrows and distance label and take a new measurement.


## Contributing

Contributions are welcome! If you have any feature suggestions, bug reports, or improvements, please create a pull request or open an issue.

## About

This project was developed by **[George Hill](https://github.com/georgeh1ll)**. It was created provide a simple tool for viewing and measuring DXF files after discovering the lack of opensource, free options for simple .dxf viewing. 

## Acknowledgments

- The [ezdxf](https://github.com/mozman/ezdxf) library for handling DXF files.
- The [Matplotlib](https://matplotlib.org/) library for plotting.
- The [Tkinter](https://docs.python.org/3/library/tkinter.html) library for the GUI.


