
import os
import pdfrw

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))   # Script directory
ROOT_DIR = os.path.dirname(SCRIPT_DIR)                    # Root directory

PDF_TEMPLATE = os.path.join(ROOT_DIR, 'data', 'Sales-Receipt-Template.pdf')  # Sales PDF file
OUTPUT_TEXT_FILE = os.path.join(ROOT_DIR, 'data', 'form_fields.txt')            # Text file containing field names

# Annotations in the context of PDF documents refers to objects or elements that can be added to a PDF page to 
# provide additional information, interactivity, or comments. They include text comments, links, stamps, signatures,
# Form fields, Shapes and drawings and Highlighting and Underlining.
ANNOT_KEY = '/Annots'               # Represents the key used in a PDF file's structure to indicate annotations.
ANNOT_FIELD_KEY = '/T'              # The key used to specify the name of a form field or widget annotation. 
ANNOT_VAL_KEY = '/V'                # It holds the data or user input associated with the field.
ANNOT_RECT_KEY = '/Rect'            # The key used to specify the rectangle that defines the location and size of an annotation on a page in a PDF
SUBTYPE_KEY = '/Subtype'            # It helps determine the type of annotation, whether it's a text annotation, a link annotation, or some other type.
WIDGET_SUBTYPE_KEY = '/Widget'      # Widget annotations are typically used for interactive form fields, like checkboxes or radio buttons.


def getFormFields(pdfTemplate, outputTextFile):
    """
    Extracts and writes the form field names from a given PDF template to a text file.

    Parameters:
    pdfTemplate (str): The path to the PDF template file to be analyzed.
    outputTextFile (str): The path to the text file where the form field names will be written.

    Returns:
    None

    This function reads the PDF template file and identifies form fields within
    each page of the document. It then writes the names of these form fields to a
    specified text file. The text file can be used for reference in subsequent
    form filling or data extraction operations.

    Example:
    >>> getFormFields('template.pdf', 'form_fields.txt')

    The names of the form fields will be written to the 'form_fields.txt' file.
    """

    templatePdf = pdfrw.PdfReader(pdfTemplate)  # Read a PDF file
    fieldNames = []   # Store extracted field names

    for page in templatePdf.pages:       # Loop through every page in the PDF file
        annotations = page[ANNOT_KEY]    # Check if a page has annotations
        for annot in annotations:        # If annotations are available, loop through every annotation on the page
            if annot[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:  # Check if the annotation is a widget annotation
                if annot[ANNOT_FIELD_KEY]:                # Check if the widget annotation has field names 
                    key = annot[ANNOT_FIELD_KEY][1:-1]    # If it does extract the names from the first to last letter
                    fieldNames.append(key)                # Add the extracted name to a list
    
    try:
        with open(outputTextFile, 'w') as textFile:   # Open a text file in write mode
            for name in fieldNames:                   # Loop through every name in the fieldNames list
                textFile.write(name + '\n')           # Write every name in the list in a text file separated by a newline character
        print("Field names have been successfully written to the output text file.")  # User feedback
    except IOError as e:
        print(f"Error writing to the file: {str(e)}")
    except Exception as ex:
        print(f"An unexpected error occurred: {str(ex)}")
    

if __name__ == '__main__':
    getFormFields(PDF_TEMPLATE, OUTPUT_TEXT_FILE)


