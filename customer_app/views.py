from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer, FinancialRecord
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

def upload_customer(request):
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
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graph = base64.b64encode(image_png).decode('utf-8')
    
    return render(request, 'customer_graph.html', {'customer': customer, 'graph': graph})
