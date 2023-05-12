from django.contrib import admin
from forarmenians_app.models import *
from django.utils.safestring import mark_safe
from forarmenians_app.forms import UsefulResourcesForm, NewsForm
# from modeltranslation.admin import admin.ModelAdmin


admin.site.register(AdImage)


class ImgInLine(admin.StackedInline):
    model = AdImage
    readonly_fields = ("image",)
    list_display = ('img', 'image', )
    extra = 1

    @staticmethod
    def image(obj):
        return mark_safe(f'<img src = {obj.img.url} with = "100" height = "100"')


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    model = Ad
    list_display = ('created_by', 'title', 'created_date', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]


admin.site.register(AdAddress)
admin.site.register(AdCountry)
admin.site.register(AdState)
admin.site.register(Location)
admin.site.register(AdComment)
admin.site.register(AdLike)


@admin.register(RatingStar)
class Ratings(admin.ModelAdmin):
    model = RatingStar
    list_display = ('id', 'value', )


admin.site.register(Rating)
admin.site.register(UserRating)
admin.site.register(ABCCategory)


@admin.register(ABCAd)
class Product(admin.ModelAdmin):
    model = ABCAd
    list_display = ('title', 'address', 'price', 'currency', 'is_active', 'category', 'start_time', 'end_time', )
    inlines = [ImgInLine, ]


admin.site.register(ABCService)


@admin.register(UsefulResources)
class UsefulResourcesAdmin(admin.ModelAdmin):
    exclude = ('id',)
    form = UsefulResourcesForm


admin.site.register(VehicleCondition)
admin.site.register(VehicleType)
admin.site.register(VehicleBrand)
admin.site.register(VehicleModel)
admin.site.register(VehicleCarcaseType)
admin.site.register(VehicleDriveUnit)
admin.site.register(VehicleMotorType)
admin.site.register(VehicleYear)


@admin.register(VehicleAd)
class VehicleAd(admin.ModelAdmin):
    model = VehicleAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]


@admin.register(JobWorkGraphic)
class JobWorkGraphicAdmin(admin.ModelAdmin):
    model = JobWorkGraphic
    fields = ('graphic', )


@admin.register(JobEducation)
class JobEducationAdmin(admin.ModelAdmin):
    model = JobWorkGraphic
    fields = ('education', )

@admin.register(JobFrequencyOfPayment)
class JobFrequencyOfPaymentAdmin(admin.ModelAdmin):
    model = JobFrequencyOfPayment
    fields = ('fop', )

admin.site.register(JobAd)
admin.site.register(JobKeySkills)
admin.site.register(JobWorkExperience)
admin.site.register(JobLanguageSkill)
admin.site.register(JobVacancy)
admin.site.register(JobResume)

admin.site.register(NewsCategory)


@admin.register(News)
class NewssAdmin(admin.ModelAdmin):
    exclude = ('id', )
    form = NewsForm


admin.site.register(NewsTag)
admin.site.register(EntertainmentType)


@admin.register(EntertainmentAd)
class Product(admin.ModelAdmin):
    model = EntertainmentAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]


@admin.register(CafeAd)
class Product(admin.ModelAdmin):
    model = CafeAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]


admin.site.register(CafeType)
admin.site.register(CafeKitchenType)
admin.site.register(CafeSpecificType)
admin.site.register(CafeKitchen)
admin.site.register(CafeSpecific)
admin.site.register(ServiceCategory)


@admin.register(ServiceAd)
class Product(admin.ModelAdmin):
    model = ServiceAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]
# admin.site.register(ServiceReview)


admin.site.register(EventCategory)


@admin.register(EventAd)
class Product(admin.ModelAdmin):
    model = EventAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]


admin.site.register(PropertyCategory)
admin.site.register(PropertyType)
admin.site.register(PropertyRentalPeriod)
admin.site.register(PropertyCondition)
admin.site.register(PropertyBedrooms)
admin.site.register(PropertyBathrooms)
admin.site.register(PropertySquare)


@admin.register(PropertyAd)
class Product(admin.ModelAdmin):
    model = PropertyAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]


admin.site.register(MarketCategory)
admin.site.register(MarketSticker)


@admin.register(MarketAd)
class Product(admin.ModelAdmin):
    model = MarketAd
    list_display = ('title', 'price', 'currency', 'is_active', )
    inlines = [ImgInLine, ]
