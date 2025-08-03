# from django.shortcuts import render

# # Create your views here.

#from django.shortcuts import render
#from .models import Profile, Skill, Experience, Project

# def home(request):
#     profile = Profile.objects.first()  # نفترض أنه يوجد فقط ملف شخصي واحد
#     skills = Skill.objects.all()
#     education = Experience.objects.filter(type='education')
#     work = Experience.objects.filter(type='work')
#     projects = Project.objects.all()

#     context = {
#         'profile': profile,
#         'skills': skills,
#         'education': education,
#         'work': work,
#         'projects': projects,
#     }

#     return render(request, 'myprofil/home/index.html', context)

from .forms import ContactForm  # تأكدي أنك عملتي forms.py فيه ContactForm
from .models import ContactMessage, Profile, Skill, Experience, Project
from django.shortcuts import render,redirect
def home(request):
    profile = Profile.objects.first()
    skills = Skill.objects.all()
    education = Experience.objects.filter(type='education')
    work = Experience.objects.filter(type='work')
    projects = Project.objects.all()

    # فورم اتصل بي
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_email()  # ترسل الإيميل بعد الحفظ
            return redirect('home')  # يعيد تحميل الصفحة بعد الإرسال

    context = {
        'profile': profile,
        'skills': skills,
        'education': education,
        'work': work,
        'projects': projects,
        'form': form,  # أضفنا الفورم
    }

    return render(request, 'myprofil/home/index.html', context)


