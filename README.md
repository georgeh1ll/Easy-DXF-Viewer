# Easy-DXF-Viewer
![Screenshot 2023-07-29 195253](https://github.com/georgeh1ll/Easy-DXF-Viewer/assets/11806169/654db9c5-e5e0-4d3b-96b1-54d3fc53a820)

**Easy DXF Viewer** is a simple Python application that allows users to view and measure distances in 2D DXF (Drawing Exchange Format) files. The application provides a graphical user interface (GUI) for loading DXF files, visualizing them on a canvas, and enabling a measure mode for distance measurement between two points.

## Features

- Open and view 2D DXF files.
- Measure distances between two points in the DXF file.
- Display arrows and the distance value for measurements.
- Clear measurement arrows and distance labels for taking new measurements.
- Developed using Python and the Tkinter, ezdxf and Matplotlib libraries.

  Please note polylines are converted into regular lines, so fillets and other curves may not look as expected. 

## Requirements

- Python 3.x
- ezdxf (to handle DXF files)
- Matplotlib (for plotting)
- Tkinter (for the GUI)

## How to Use Python Version

1. Clone the repository to your local machine.
2. Install the required libraries using: "pip install -r requirements.txt" or manually. 
3. Run the `Easy_DXF_Viewer.py` script.
4. The application will open in full-screen mode, and you will see the "Open DXF" button.
5. Click the "Open DXF" button to load a DXF file for viewing.
6. After loading the DXF file, the "Measure Mode" and "Clear Measurement" buttons will become active.
7. Click the "Measure Mode" button to activate measure mode.
8. Click on two points in the DXF plot to measure the distance between them.
9. The distance will be displayed on the plot.
10. Click the "Clear Measurement" button to remove the measurement arrows and distance label and take a new measurement.

## How to Use the Windows Version 

1. Locate the windows version of the program under the **[releases]([(https://github.com/georgeh1ll/Easy-DXF-Viewer/releases)])** section of the repository.
2. Download the .exe file and run on a Windows machine. 
3. The application will open in full-screen mode, and you will see the "Open DXF" button.
4. Click the "Open DXF" button to load a DXF file for viewing.
5. After loading the DXF file, the "Measure Mode" and "Clear Measurement" buttons will become active.
6. Click the "Measure Mode" button to activate measure mode.
7. Click on two points in the DXF plot to measure the distance between them.
8. The distance will be displayed on the plot.
9. Click the "Clear Measurement" button to remove the measurement arrows and distance label and take a new measurement.


## Contributing

Contributions are welcome! If you have any feature suggestions, bug reports, or improvements, please create a pull request or open an issue.

## About

This project was developed by **[George Hill](https://github.com/georgeh1ll)**. It was created to provide a simple tool for viewing and measuring DXF files after discovering the lack of open-source, free options for simple .dxf file viewing. Other applications claim to be free but end up being free trials or have certain features heavily limited, this is completely free and I will continue to work on it during my spare time. 

## Acknowledgments

- The [ezdxf](https://github.com/mozman/ezdxf) library for handling DXF files.
- The [Matplotlib](https://matplotlib.org/) library for plotting.
- The [Tkinter](https://docs.python.org/3/library/tkinter.html) library for the GUI.


