from django.db import models

# Create your models here.

class Info(models.Model):
    first_name = models.CharField(max_length=30),
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    phone = models.IntegerField(max_length=10)
    email = models.CharField(max_length=60)
    address_line_1 = models.CharField(max_length=200)
    address_line_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    ss = models.IntegerField()
    married_yes = 'YES'
    married_no = 'NO'
    MARRIED_CHOICES = [
        (married_yes, 'Yes'),
        (married_no, 'No')
    ]
    married = models.CharField(
        max_length = 3,
        choices = MARRIED_CHOICES,
        default = married_yes,
    )
    eligible_yes = "YES"
    eligible_no = 'NO'
    ELIGIBLE_CHOICES = [
        (eligible_yes, "Yes"),
        (eligible_no, "No")
    ]
    eligible = models.CharField(
        max_length=3,
        choices=ELIGIBLE_CHOICES,
        default = eligible_yes
    )