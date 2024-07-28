from django.contrib import admin

from .models import BaggageShippingModel, BaggageShippingSealsModel


class BaggageShippingSealsInline(admin.TabularInline):
    model = BaggageShippingSealsModel
    extra = 2


class BaggageShippingInline(admin.TabularInline):
    model = BaggageShippingModel
    extra = 3


@admin.register(BaggageShippingModel)
class BaggageShippingModelAdmin(admin.ModelAdmin):
    inlines = [BaggageShippingSealsInline]


admin.site.register(BaggageShippingSealsModel)
