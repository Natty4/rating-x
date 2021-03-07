from django.db import models

class Poll(models.Model):
    # 1,Is the topic impactfull
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)

    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)
    
   

    image = models.ImageField(upload_to='profile/%y/%m/%d', blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def total(self):
    	return self.option_one_count + self.option_two_count + self.option_three_count
    def __str__(self):
    	return self.question

class Ses(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name = '+')
    ses = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)