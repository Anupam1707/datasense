# Database Analyzer

The purpose of this project is to develop a Python app, named Database Analyzer, that can analyze the sales data of the food industry stored in a Remote Database. The app provides both visual and numeric analysis of the data and offers a GUI interface for users to access and analyze the data directly from the Remote Database without any delays.

## Libraries and APIs Used

The app utilizes the following libraries and APIs:

- **oauth2client** module to authorize the user to the Google Database.
- **Google Drive API** and **Google Sheets API** to create a link between the user and the Google Sheet.
- **gspread** module to access the sales data from the Remote Database.
- **NumPy** for performing numerical analysis on the data.
- **Matplotlib** for creating graphs and visualizations of the data.
- **requests** library, **Python Image Library (PIL)**, and **Input/Output(io)** library for GUI enhancement and data handling.
- **SecuriPy**, a library developed by the app's developer, for security-related functionalities.

## Features Offered

1. **GUI interface** for accessing and analyzing sales data: Users can access the sales data directly from the Remote Database through a GUI interface and choose between visual or numeric analysis of the data.
2. **Visual analysis** of sales data: The app uses **Matplotlib** to create graphs and visualizations of the sales data, such as bar charts, histograms, etc., according to the parameters selected by the user.
3. **Numeric analysis** of sales data: The app uses **NumPy** to perform numerical analysis of the sales data, such as calculating the mean, median, mode, or standard deviation of the data.
4. **AI-Based** Suggestions of Analysis: The app is integrated with AI to provide suggestions based on the analysis of the sales data to enhance production and sales.
5. **Data export**: The app allows users to export the analyzed data in various formats, such as:
   - Graphs: **JPG, JPEG, PNG.**
   - Selected Data: **CSV, Excel.**

The expected output of the app can be one of the following:

1. A graph plotted based on the selected parameters.
2. Numeric data corresponding to the analysis performed.
3. Quick suggestions based on the analysis.

Users can utilize this output to gain insights into the sales data of the food industry.

Overall, the Database Analyzer app provides a user-friendly interface for accessing and analyzing sales data stored in the Remote Database and offers a range of analytical tools for visualizing and interpreting the data.
