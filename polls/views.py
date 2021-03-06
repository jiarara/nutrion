from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from nutrion import settings
from polls.models import Question, Choice, Category, Banner, Article, Tag, Link

'''
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html', context)


'''
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})
'''


def html_page(request,path):
    # print("path::"+request.path)
    staticurl = "polls/digestion/"+path
    return render(request,staticurl)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def login_check(request):
    print( request.user.username)
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

# ??????
# ???models?????????Category???
#@login_required
def index(request):
    # login_check(request)
    # allcategory = Category.objects.all()  # ??????Category?????????????????????
    banner = Banner.objects.filter(is_active=True)[0:5]#?????????????????????????????????????????????
    tui = Article.objects.filter(tui__id=4)[:3]#???????????????ID???1?????????
    # allarticle = Article.objects.all().order_by('-id')[0:10]
    allarticle = Article.objects.all()
    #hot = Article.objects.all().order_by('?')[:10]#????????????
    #hot = Article.objects.filter(tui__id=3)[:10]   #????????????????????????????????????ID???3??????
    hot = Article.objects.all().order_by('views')[:10]#???????????????????????????
    # remen = Article.objects.filter(tui__id=2)[:6]
    # tags = Tag.objects.all()

    link = Link.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(allarticle, 8)
    try:
        allarticle = paginator.page(page) # ???????????????????????????
    except PageNotAnInteger:
        allarticle = paginator.page(1) # ??????????????????????????????????????????,?????????1????????????
    except EmptyPage:
        allarticle = paginator.page(paginator.num_pages) # ????????????????????????????????????????????????????????????,???????????????????????????
    return render(request, 'polls/index.html', locals())  # ??????????????????index.html??????


#????????????
def list(request,lid):
    list = Article.objects.filter(category_id=lid)#????????????URL????????????lid??????????????????????????????
    cname = Category.objects.get(id=lid)#??????????????????????????????
    # remen = Article.objects.filter(tui__id=2)[:6]#?????????????????????
    # allcategory = Category.objects.all()#??????????????????
    # tags = Tag.objects.all()#????????????????????????
    page = request.GET.get('page')#???URL????????????????????????
    paginator = Paginator(list, 5)#???????????????????????????list???????????????????????????5??????????????????
    try:
        list = paginator.page(page)#???????????????????????????
    except PageNotAnInteger:
        list = paginator.page(1)#??????????????????????????????????????????,?????????1????????????
    except EmptyPage:
        list = paginator.page(paginator.num_pages)#????????????????????????????????????????????????????????????,???????????????????????????
    return render(request, 'polls/list.html', locals())
# ?????????
def show(request,sid):
    show = Article.objects.get(id=sid)#????????????ID?????????
    # allcategory = Category.objects.all()#??????????????????
    # tags = Tag.objects.all()#??????????????????
    # remen = Article.objects.filter(tui__id=2)[:6]#??????????????????
    hot = Article.objects.all().order_by('?')[:10]#?????????????????????????????????????????????????????????
    previous_blog = Article.objects.filter(created_time__gt=show.created_time,category=show.category.id).first()
    netx_blog = Article.objects.filter(created_time__lt=show.created_time,category=show.category.id).last()
    show.views = show.views + 1
    show.save()
    return render(request, 'polls/show.html', locals())

def tag(request, tag):
    list = Article.objects.filter(tags__name=tag)#????????????????????????????????????
    # remen = Article.objects.filter(tui__id=2)[:6]
    # allcategory = Category.objects.all()
    tname = Tag.objects.get(name=tag)#??????????????????????????????
    page = request.GET.get('page')
    # tags = Tag.objects.all()
    paginator = Paginator(list, 5)
    try:
        list = paginator.page(page)  # ???????????????????????????
    except PageNotAnInteger:
        list = paginator.page(1)  # ??????????????????????????????????????????,?????????1????????????
    except EmptyPage:
        list = paginator.page(paginator.num_pages)  # ????????????????????????????????????????????????????????????,???????????????????????????
    return render(request, 'polls/tags.html', locals())

# ?????????
def search(request):
    ss=request.GET.get('search')#????????????????????????
    list = Article.objects.filter(title__icontains=ss)#????????????????????????????????????????????????
    # remen = Article.objects.filter(tui__id=2)[:6]
    # allcategory = Category.objects.all()
    page = request.GET.get('page')
    # tags = Tag.objects.all()
    paginator = Paginator(list, 10)
    try:
        list = paginator.page(page) # ???????????????????????????
    except PageNotAnInteger:
        list = paginator.page(1) # ??????????????????????????????????????????,?????????1????????????
    except EmptyPage:
        list = paginator.page(paginator.num_pages) # ????????????????????????????????????????????????????????????,???????????????????????????
    return render(request, 'polls/search.html', locals())


# ????????????
def about(request):
    # allcategory = Category.objects.all()
    return render(request, 'polls/page.html',locals())

def global_variable(request):
    allcategory = Category.objects.all()
    remen = Article.objects.filter(tui__id=4)[:6]
    tags = Tag.objects.all()
    return locals()