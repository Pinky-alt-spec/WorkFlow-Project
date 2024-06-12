from django.db import models

class Customer(models.Model):
    """
    Customer model to store customer information.

    Fields:
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        date_of_birth (date): The date of birth of the customer.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()

    def __str__(self):
        """
        String representation of the Customer model.

        Returns:
            str: The full name of the customer.
        """
        return f'{self.first_name} {self.last_name}'

class FinancialRecord(models.Model):
    """
    FinancialRecord model to store financial data for customers.

    Fields:
        customer (ForeignKey): The customer to which the financial record belongs.
        month (str): The month of the financial record.
        income (float): The income for the month.
        expense (float): The expense for the month.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    income = models.FloatField()
    expenses = models.FloatField()
