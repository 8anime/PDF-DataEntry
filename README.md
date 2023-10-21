# PDFSalesDataEntryForm

PDFSalesDataEntryForm is a Python application that facilitates the extraction of form field names from a given PDF template and the filling of PDF forms with sales data. It consists of two main functions, `getFormFields` and `enterSalesData`.

## Functions

### `getFormFields(pdfTemplate, outputTextFile)`

- **Description**: Extracts and writes the form field names from a given PDF template to a text file.

- **Parameters**:
  - `pdfTemplate (str)`: The path to the PDF template file to be analyzed.
  - `outputTextFile (str)`: The path to the text file where the form field names will be written.

- **Returns**: None

- **Functionality**: This function reads the PDF template file and identifies form fields within each page of the document. It then writes the names of these form fields to a specified text file. The text file can be used for reference in subsequent form filling or data extraction operations.

- **Example**:
  ```python
  getFormFields('template.pdf', 'form_fields.txt')


## enterSalesData(emptyPDFForm, completePDFForm, data)

- Description: Fill a PDF form with the given data and save the filled PDF to an output file.

Parameters:

`emptyPDFForm (str)`: Path to the input PDF file (template).
`completePDFForm (str)`: Path to save the output PDF (filled form).
`data (dict)`: A dictionary containing field names and their corresponding values.


## Application Structure

- The project structure includes the following components:

1. main.py: The entry point to the application.

2. data Directory: Contains the following files:

`Sales-Receipt-Template.pdf`: The PDF form template when it is empty.
`completed_form.pdf`: The PDF form when it is completed with sales data.
`form_fields.txt`: A text file that is generated and contains the extracted field names from the PDF template.


## Getting Started

- To use the PDFSalesDataEntryForm application, follow these steps:

1. Ensure you have the required Python environment set up.

2. Run the getFormFields function to extract form field names from a PDF template and generate the 'form_fields.txt' file.

3. Run the enterSalesData function to fill the PDF form with sales data and save the filled PDF to an output file.

4. Modify the 'data' directory to include your specific PDF templates and data as needed.




