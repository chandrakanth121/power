from django.shortcuts import render,get_object_or_404
from testapp.models import Post
from django.views.generic import ListView
from testapp.forms import commentform


def Postview(request):
    Post_list=Post.objects.all()
    

    return render(request,'testapp/Post_list.html',{'Post_list':Post_list,})

def Post_detail(request,year,month,day,post):
    post=get_object_or_404(Post, slug=post,
                                 status='published',
                                 publish__year=year,
                                 publish__month=month,
                                 publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=='POST ':
        form=commentform(request.POST)
        if form.is_valid():
            new_comment.save()
            csubmit=True
    else:
        form=commentform()


    return render(request,'testapp/post_detail.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
