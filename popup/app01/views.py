from django.shortcuts import render
from app01 import models


# Create your views here.

def popup_test(request):
    obj = models.UserGroup.objects.all()
    return render(request, 'popup_test.html', {'obj': obj})


def popup_add(request):
    if request.method == "GET":
        return render(request, 'popup_add.html')
    else:
        popup_tag_id = request.GET.get('popup_id')  # 获取select字段id
        print(popup_tag_id)
        title = request.POST.get('title')
        obj = models.UserGroup.objects.create(title=title)
        context = {'popup_tag_id': popup_tag_id, 'option_id': obj.pk, 'option_text': obj.title}
        return render(request, 'popup_response.html', context)
