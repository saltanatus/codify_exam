from django.db import models
from datetime import datetime
from django.urls import reverse

class AbstractHuman(models.Model):
    fullname = models.CharField(max_length=50)
    birth_date = models.DateField()

    def get_age(self):
        return datetime.now().year - self.birth_date.year

    class Meta:
        abstract = True

class Worker(AbstractHuman):
    work_position = models.CharField(max_length=50)
    work_experience = models.DateField()

    def get_absolute_url(self, *args, **kwargs):
        return reverse('worker_detail', kwargs={'pk':self.id})

class Document(models.Model):
    inn = models.CharField(max_length=16)
    card_id = models.CharField(max_length=6)
    worker = models.OneToOneField(Worker, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        print(f'Сотрудник {self.worker.fulname} сохранен')
        super().save(*args, **kwargs)

class Project(models.Model):
    name = models.CharField(max_length=50)
    worker = models.ManyToManyField(Worker, through='Membership')

class Membership(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    date_joined = models.DateField()

class Customer(AbstractHuman):
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)

class VIPCustomer(Customer):
    vip_status_start = models.DateField()
    donation_amount = models.IntegerField()

