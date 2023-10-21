
import os

from src.salesEntry import enterSalesData

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

PDF_TEMPLATE = os.path.join(ROOT_DIR, 'data', 'Sales-Receipt-Template.pdf')  # Sales PDF file
COMPLETE_FORM = os.path.join(ROOT_DIR, 'data', 'completed_form.pdf')


if __name__ == '__main__':
    company_info = {
        'Receipt Number' : 'R123456',
        'Date' : 'October 21, 2023',
        'Merchant Name' : 'ABC Electronics',
        'Merchant Phone Number' : '555-555-5555',
        'Merchant Street Address' : '23 Main Street',
        'CityStateZIP' : 'New York, NY 10001'
    }

    customer_info = {
        'Name'  : 'Alice Johnson',
        'Company Name'  : 'ABC Inc',
        'Street Address'  : '456 Elm Street',
        'CityStateZIP_2'  : 'San Francisco, CA 94101',
        'Phone Number'  : '(123) 456-7890'
    }

    financial_info = {
        'Subtotal' : '1000',
        'Discount' : '20',
        'Sales Tax' : '8',
        'Total' : '980',
        'Amount Paid' : '78.40'
    }

    payment_info = {
        'Payment Method' : 'Credit Card',
        'CardCheck Number' : 'Visa: 4111 1111 1111 1111'
    }

    items = [
        {'Description' : 'Cappuccino (Regular)', 'Quantity' : '2', 'Price/Unit' : '$1.80', 'Line Total' : '$3.60'},
        {'Description' : 'Espresso (Double Shot)', 'Quantity' : '1', 'Price/Unit' : '$2.00', 'Line Total' : '$2.00'},
        {'Description' : 'Latte (Large)', 'Quantity' : '3', 'Price/Unit' : '$1.50', 'Line Total' : '$4.50'},
        {'Description' : 'Mocha (Regular)', 'Quantity' : '1', 'Price/Unit' : '$2.00', 'Line Total' : '$2.00'},
        {'Description' : 'Americano (Small)', 'Quantity' : '2', 'Price/Unit' : '$1.20', 'Line Total' : '$2.40'},
        {'Description' : 'Iced Coffee (Large)', 'Quantity' : '4', 'Price/Unit' : '$2.20', 'Line Total' : '$8.80'},
        {'Description' : 'Caramel Macchiato (Regular)', 'Quantity' : '1', 'Price/Unit' : '$2.00', 'Line Total' : '$2.00'},
        {'Description' : 'Tea (Green, Small)', 'Quantity' : '3', 'Price/Unit' : '$1.50', 'Line Total' : '$4.50'},
        {'Description' : 'Tea (Green, Large)', 'Quantity' : '2', 'Price/Unit' : '$2.00', 'Line Total' : '$4.00'},
        {'Description' : 'Latte (Small)', 'Quantity' : '3', 'Price/Unit' : '$1.50', 'Line Total' : '$4.50'},
    ]

    # Combine the dictionaries and fill the form
    data = {**company_info, **customer_info, **financial_info, **payment_info}
    # Loop through the items and update the 'data' dictionary
    for i, item in enumerate(items, start=1):
        data.update({
            f'DescriptionRow{i}': item['Description'],
            f'QuantityRow{i}': item['Quantity'],
            f'PriceUnitRow{i}': item['Price/Unit'],
            f'Line TotalRow{i}': item['Line Total'],
        })

    enterSalesData(PDF_TEMPLATE, COMPLETE_FORM, data)