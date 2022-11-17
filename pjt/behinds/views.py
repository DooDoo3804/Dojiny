from django.shortcuts import render, redirect, get_object_or_404
from .forms import BehindForm
from .models import Behind


# Create your views here.
def index(request):
    behinds = Behind.objects.all()
    context = {
        'behinds': behinds,
    }
    return render(request, 'behinds/index.html', context)

# 생성 폼과 생성 페이지
def create(request):
    # 로그인 한 사용자 중에 권한이 있는 사용자(감독)
    if request.user.is_authenticated and request.user.behind_auth:
        if request.method == "POST":
            title = request.POST.get('title')
            content = request.POST.get('content')
            csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken')
            behind_values = {
                'title': title,
                'content': content,
                'csrfmiddlewaretoken': csrfmiddlewaretoken
            }
            form = BehindForm(behind_values)
            if form.is_valid():
                behind = form.save(commit=False)
                behind.user = request.user
                behind.save()
                return redirect('behinds:index')
            return render(request, 'behinds/create.html')
        else:
            return render(request, 'behinds/create.html')
    # 로그인을 했지만 권한이 없는 사용자
    elif request.user.is_authenticated :
        return redirect('behinds:index')
    # 로그인도 안했고 권한도 없는 사용자
    else:
        return redirect('http://127.0.0.1:8000/')

# 디테일 페이지
def detail(request, behind_pk):
    behind = Behind.objects.get(pk=behind_pk)
    context = {
        'behind': behind,
    }
    return render(request, 'behinds/detail.html', context)


def delete(request, behind_pk):
    behind = Behind.objects.get(pk=behind_pk)
    if request.user == behind.user:
        behind.delete()
        return redirect('behinds:index')
    else:
        return redirect('behinds:detail', behind.pk)


def update(request, behind_pk):
    behind = get_object_or_404(Behind, pk=behind_pk)
    if request.user == behind.user:
        if request.method == 'POST':
            form = BehindForm(request.POST, instance=behind)
            if form.is_valid():
                form.save()
                return redirect('behinds:detail', behind_pk)
        else:
            form = BehindForm(instance=behind)
    else:
        return redirect('behinds:detail', behind_pk)
    form = BehindForm(instance=behind)
    context = {
        'behind': behind,
        'form': form
    }
    return render(request, 'behinds/update.html', context)