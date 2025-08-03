from django.db import models

# Create your models here.


# معلوماتك الشخصية
class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='profile/')
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__ (self):
        return self.full_name

# # المهارات
# class Skill(models.Model):
#     name = models.CharField(max_length=100)
#     percentage = models.IntegerField(help_text="قيمة مئوية مثل 80")

#     def __str__ (self):
#         return self.name
class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField(help_text="قيمة مئوية مثل 80")
    icon_class = models.CharField(max_length=100, help_text="أدخل اسم الكلاس من Font Awesome مثل: fab fa-python")

    def str(self):
        return self.name
# التجارب التعليمية أو المهنية
class Experience(models.Model):
    TYPE_CHOICES = (
        ('education', 'Education'),
        ('work', 'Work'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()


    def __str__(self):
        return f"{self.title} at {self.organization}"

# المشاريع في صفحة Portfolio
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('app', ' Mobile Application'),
        ('product', 'Product'),
        ('brand', 'Brand'),
        ('web', 'Web Aplication'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    project_url = models.URLField(blank=True)

    def __str__ (self):
        return self.title

# رسائل الزوار
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"