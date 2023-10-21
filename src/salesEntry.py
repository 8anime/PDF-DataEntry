
from PyPDFForm import PyPDFForm

def enterSalesData(emptyPDFForm, completePDFForm, data):
    """
    Fill a PDF form with the given data and save the filled PDF to an output file.

    :param emptyPDFForm: Path to the input PDF file (template).
    :param completePDFForm: Path to save the output PDF (filled form).
    :param data: A dictionary containing field names and their corresponding values.
    """

    try:
        # Load the empty PDF File
        emptyFile = PyPDFForm(emptyPDFForm)

        # Populate the empty file with the provided data and read its content
        completeFile = emptyFile.fill(data).read()

        with open(completePDFForm, 'wb+') as output:
            output.write(completeFile)
    
        print("PDF form has been successfully filled and saved to the output file.")
    except FileNotFoundError as file_not_found_error:
        print(f"Error: {str(file_not_found_error)}. Ensure the input and output file paths are correct.")
    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")





