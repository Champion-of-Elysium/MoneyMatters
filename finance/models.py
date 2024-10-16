from django.db import models
from django.db.models import Sum
from users.models import User
from .variables import CurrencyTypeChoices, TransactionTypeChoices, TransactionCategoryChoices

class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=100, blank=False, verbose_name="Financial Accounts")
    account_type = models.CharField(max_length=100, blank=False, verbose_name="Account Type")
    balance = models.DecimalField(max_digits=12, decimal_places=2, blank=False, verbose_name="Account Balance")
    currency = models.CharField(max_length=6, choices=CurrencyTypeChoices.choices)

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=7, choices=TransactionTypeChoices.choices, verbose_name="Transaction Type")
    amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, verbose_name="Amount of Transaction")
    category = models.CharField(max_length=50, choices=TransactionCategoryChoices.choices, verbose_name="Transaction Category")
    date = models.DateTimeField(blank=False)
    descrioption = models.TextField(blank=False)

    @staticmethod
    def get_income_total(user):
        return Transaction.objects.filter(user=user, transaction_type="income").aggregate(total_income=Sum('amount'))['total_income'] or 0

    @staticmethod
    def get_expense_total(user):
        return Transaction.objects.filter(user=user, transaction_type="expense").aggregate(total_expense=Sum('amount'))['total_expense'] or 0

class SavingsGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goal_name = models.CharField(max_length=100, blank=False, verbose_name="Goal Name")
    target_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, verbose_name="Target Amount")
    current_amount = models.DecimalField(max_digits=12, decimal_places=2, blank=False, verbose_name="Current Amount")
    due_date = models.DateField(blank=False)
    descrioption = models.TextField(blank=False)