from django.contrib import admin
from datetime import date
from main.models import Worker, Document


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'work_position', 'get_work_year', 'get_link')
    list_display_links = ('get_link',)

    @admin.display(description='Опыт работы')
    def get_work_year(self, obj):
       year = date.today().year - obj.birth_date.year
       return year

    @admin.display(description='Подробнее')
    def get_link(self, obj):
        return 'Подробнее'
    

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('get_worker_fullname', 'inn', 'card_id')

    @admin.display(description='ФИО')
    def get_worker_fullname(self, obj):
        return obj.worker.fullname

