from django.db import models

class CurrencyTypeChoices(models.TextChoices):
    DOLLAR = 'Dollar', '$'
    TOMAN = 'Toman', 'T'

class TransactionTypeChoices(models.TextChoices):
    INCOME = 'Income', 'Income'
    EXPENSE = 'Expense', 'Expense'

class TransactionCategoryChoices(models.TextChoices):
    DAILY_SHOPPING = 'Daily Shopping', 'Daily Shopping'
    CAFE_RESTAURANT = 'Cafe and Restaurant', 'Cafe and Restaurant'
    COMMUTING = 'Commuting', 'Commuting'
    HOUSEHOLD = 'House and Household', 'House and Household'
    BEAUTY_HEALTH = 'Beauty and Health', 'Beauty and Health'
    CHARGE_BILL = 'Charge and Bill', 'Charge and Bill'
    FASHION_CLOTHING = 'Fashion and Clothing', 'Fashion and Clothing'
    CULTURAL_ARTISTIC = 'Cultural and Artistic', 'Cultural and Artistic'
    FUN_ENTERTAINMENT = 'Fun and Entertainment', 'Fun and Entertainment'
    SAVINGS_CAPITAL = 'Savings and Capital', 'Savings and Capital'
    EXERCISE_WELLNESS = 'Exercise and Wellness', 'Exercise and Wellness'
    GIFT_CHARITY = 'Gift and Charity', 'Gift and Charity'
    LOAN_INSTALLMENTS = 'Loan Installments', 'Loan Installments'
    MONEY_TRANSFER = 'Money Transfer', 'Money Transfer'
    CASH_WITHDRAWAL = 'Cash Withdrawal', 'Cash Withdrawal'
    OTHER = 'Other', 'Other'