from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .forms import RegisterForm
from django.utils import timezone
from .models import Tweet
# timezone,tweetのimportを追加


def index(request):
    context = {
        'user': request.user,
        'tweets':Tweet.objects.all()
    }
    # contextでコロン以下のデータを持ってきて、データ名を付けた。
    return render(request, 'polls/index.html', context)

@login_required
def profile(request):
    context = {
        'user': request.user,
    }
    return render(request, 'polls/profile.html', context)

def regist(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    return render(request, 'polls/regist.html', context)

@require_POST
def regist_save(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('polls:index')

    context = {
        'form': form,
    }
    return render(request, 'polls/regist.html', context)

# indexでtimeline的なのを表示させるため追加
def add(request):
    user=request.user
    tweet=Tweet(tweet_text=request.POST["text"],tweet_date =timezone.now(),user_id=user.id)
    tweet.save()
    return redirect('polls:index')

def delete(request):
    tweet=Tweet(id=int(request.POST["tweet_id"]))
    tweet.delete()
    return redirect('polls:index')
    # tweet_idはkey
