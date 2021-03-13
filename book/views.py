from django.shortcuts import render,HttpResponse,redirect, get_object_or_404,Http404
from django.http import HttpResponseNotFound
from .forms import BookForm,CategoryForm
from .models import *
from django.views.generic import ListView,CreateView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.
#@login_required
def home(request):
    
    context={}
    context['data']=Book.objects.filter(user=request.user).select_related('category').order_by('name')
    
    return render (request,'book/book/home.html',context)
def about(request):
    return render (request,'book/about.html')
def create_book(request):
    if request.method=='GET':
        context={}
        context['form']=BookForm()
        return render (request,'book/book/create.html',context)
    else:
        form=BookForm(request.POST)
        if form.is_valid():
            
            book=form.save(commit=False)
            book.user=request.user
            book.save()
            return redirect ('book_home')

        else:
            context={}
            context['form']=form
            return render (request,'book/book/create.html',context)
def update(request,id):
    book=get_object_or_404(Book,id=id,user=request.user)
    #ANOTHER METHOD
    #try:
            #curbook=Book.objects.get(id=id)
        #except Book.DoesNotExist:
            #return HttpResponseNotFound()
        #another method
    if request.method=='GET':
        
        
            
        
        curbook=Book.objects.get(id=id)
        context={}
        context['form']=BookForm(instance=curbook)
        return render (request,'book/book/create.html',context)
    else:
        curbook=Book.objects.get(id=id)
        form=BookForm(data=request.POST,instance=curbook)
        if form.is_valid():
                
            form.save()
            return redirect ('book_home')

        else:
            context={}
            context['form']=form
            return render (request,'book/book/create.html',context)
        
@login_required  
def delete(request,id):
    if request.method=='GET':
        book= book=get_object_or_404(Book,id=id,user=request.user)
        book.delete()
        return redirect ('book_home')
class BookListView(LoginRequiredMixin, ListView):
    model=Book
    template_name='book/book/home.html'
    context_object_name='data'
    paginate_by=5
    #queryset=Book.objects.all().select_related('category').order_by('name')
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user).select_related('category').order_by('name')
    

class BookCreateView(LoginRequiredMixin,CreateView):
    model=Book
    template_name='book/book/create.html'
    #fields='__all__'
    form_class=BookForm
    success_url=reverse_lazy('book_home')

    def form_valid(self,form):
        book=form.save(commit=False)
        book.user=self.request.user
        book.save()
        return redirect (self.success_url)

class BookUpdateView(LoginRequiredMixin,UpdateView):
    model=Book
    template_name='book/book/create.html'
    #fields='__all__'
    form_class=BookForm
    pk_url_kwarg='id'
    success_url=reverse_lazy('book_home')

    def get_object(self):
        pk=self.kwargs.get('id')
        if pk is None:
            raise Http404()
        b=Book.objects.filter(pk=pk,user=self.request.user).first()
        if b is None:
            raise Http404()
        else:
            return b
class CategoryListView(LoginRequiredMixin,ListView):
    model=Category
    template_name='book/book/categorylist.html'
class CategoryCreateView(LoginRequiredMixin,CreateView):
    model=Category
    template_name='book/book/category.html'
    #fields='__all__'
    form_class=CategoryForm
    success_url=reverse_lazy('category_list')
class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    model=Category
    template_name='book/book/category.html'
    #fields='__all__'
    form_class=CategoryForm
    pk_url_kwarg='id'
    success_url=reverse_lazy('category_list')
@login_required
def deletecategory(request,id):
    if request.method=='GET':
        cat=get_object_or_404(Category,id=id)
        cat.delete()
        return redirect ('category_list')




