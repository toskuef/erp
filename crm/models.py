from django.db import models


class CrmLead(models.Model):
    """Модель таблицы с лидами"""
    pass


class CrmLeadStatus(models.Model):
    """Модель таблицы со статусами лида"""
    pass


class CrmLeadSource(models.Model):
    """Модель таблицы со списком источников лида"""
    pass


class CrmCustomer(models.Model):
    """Модель таблицы с клиентами"""
    pass


class CrmCustomerStatus(models.Model):
    """Модель с юридическими статусами клиента"""
    pass


class CrmTask(models.Model):
    """Модель с задачами"""
    pass


class CrmTaskStatus(models.Model):
    """Модель со статусами задачи"""
    pass


class CrmTaskType(models.Model):
    """Модель с типами задачи"""
    pass


class CrmDeal(models.Model):
    """Модель со сделками"""
    pass


class CrmDealStatus(models.Model):
    """Модель со статусами сделки"""
    pass
