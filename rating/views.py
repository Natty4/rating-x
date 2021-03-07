from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreatePollForm
from django.http import HttpResponse
from .models import Poll, Ses
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
        	form.save()
        	return redirect('home')
    else:
        form = CreatePollForm()

    context = {'form' : form}
    return render(request, 'rating/create.html', context)

def home(request):
    polls = Poll.objects.all()

    context = {
        'polls' : polls
    }
    return render(request, 'rating/home.html', context)


def results(request, pk):
    # poll = Poll.objects.get(pk=pk)
    poll = get_object_or_404(Poll,pk=pk)

    context = {
        'poll' : poll
    }
    return render(request, 'rating/results.html', context)

def vote(request, pk):
	poll = get_object_or_404(Poll,pk=pk)

	def get_client_ip(request):
		# x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		x_forwarded_for = request.META.get('HTTP_X_REAL_IP')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			# ip = request.META.get('REMOTE_ADDR')
			ip = request.META.get('REMOTE_ADDR')
		return ip
	Ips = []
	ip = get_client_ip(request)
	ips = Ses.objects.filter(active=True)
	for o in ips:
		Ips.append(o.ses)
	if ip in Ips:
		return redirect('home')
	else:
		Ses.objects.create(ses=ip, poll_id=pk)
	if request.method == 'POST':
		try:
			selected_option = request.POST['poll']
			if selected_option == 'option1':
				poll.option_one_count += 1
			elif selected_option == 'option2':
				poll.option_two_count += 1
			elif selected_option == 'option3':
				poll.option_three_count += 1
			else:
				return HttpResponse(400, 'Invalid form option')
		except:
			return redirect('/')
		Ses.objects.create(ses=ip, poll_id=pk)
		poll.save()
		return redirect('results', poll.id)

	print(ip)
	context = {'poll' : poll}
	return render(request, 'rating/vote.html', context)



