from django.shortcuts import render
from uploader.models import Uploader
from .models import Post, Image


def index(request):
	try:
		latest_post = Post.objects.latest('posted')
	except Post.DoesNotExist:
		latest_post = None

	try:
		posts = Post.objects.all()[1:5]
	except Post.DoesNotExist:
		posts = None

	try:
		images = Image.objects.filter(post=latest_post)
	except Image.DoesNotExist:
		images = None

	try:
		documents = Uploader.objects.filter(post=latest_post)
	except Uploader.DoesNotExist:
		documents = None

	context = {
		'posts': posts,
		'latest_post': latest_post,
		'images': images,
		'documents': documents,
	}

	return render(request, 'post_list.html', context)


def post_detail(request, post_id):
	post = Post.objects.get(pk=post_id)

	try:
		images = Image.objects.filter(post=post)
	except Image.DoesNotExist:
		images = None

	try:
		documents = Uploader.objects.filter(post=post)
	except Uploader.DoesNotExist:
		documents = None

	context = {
		'post': post,
		'images':images,
		'documents':documents,
	}

	return render(request, 'post_detail.html', context)


def news(request):
	all_posts = Post.objects.all()
	template = 'news.html'
	context = {
		'all_posts':all_posts,
	}

	return render(request, template, context)