from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer, FinancialRecord
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def upload_customer(request):
    """
    Handle customer information and Excel file upload.

    This view handles the form submission for customer information and the 
    upload of an Excel file containing financial data. It saves the customer 
    information and processes the Excel file to store financial records.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered HTML template for the form or a redirect 
        to the customer graph view.
    """
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            excel_file = request.FILES['excel_file']
            data = pd.read_excel(excel_file)

            customer.save()
            for _, row in data.iterrows():
                FinancialRecord.objects.create(
                    customer=customer,
                    month=row['Month'],
                    income=row['Income'],
                    expenses=row['Expenses']
                )
            return redirect('customer_graph', customer_id=customer.id)
    else:
        form = CustomerForm()
    return render(request, 'upload_customer.html', {'form': form})

def customer_graph(request, customer_id):
    """
    Render a temporal graph of customer financial data.

    This view retrieves financial data for a customer and renders a graph 
    showing income and expenses over the last 12 months.

    Args:
        request: The HTTP request object.
        customer_id (int): The ID of the customer.

    Returns:
        HttpResponse: The rendered HTML template with the financial graph.
    """
    customer = Customer.objects.get(id=customer_id)
    records = FinancialRecord.objects.filter(customer=customer)
    data = pd.DataFrame(list(records.values('month', 'income', 'expenses')))

    plt.figure(figsize=(10, 5))
    plt.plot(data['month'], data['income'], label='Income')
    plt.plot(data['month'], data['expenses'], label='Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount')
    plt.title('Income and Expenses Over 12 Months')
    plt.legend()
    
    buffer = io.BytesIO() # Create an in-memory bytes buffer.
    plt.savefig(buffer, format='png') # Save the plot to the buffer in PNG format.
    buffer.seek(0) # Rewind the buffer to the beginning.
    image_png = buffer.getvalue()# Get the PNG image data from the buffer.
    buffer.close()
    graph = base64.b64encode(image_png).decode('utf-8') # Encode the image data in base64 for embedding in HTML.
    
    return render(request, 'customer_graph.html', {'customer': customer, 'graph': graph})
