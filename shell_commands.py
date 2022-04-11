from main.models import Worker, Document, Customer, VIPCustomer

customer = Customer(fullname='Customer')





e = Worker.objects.first()
p = Document(employee=e)
