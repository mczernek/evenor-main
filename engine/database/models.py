from django.db import models

class User(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    facebook_id = models.CharField(max_length=50)

    join_date = models.DateTimeField('join date')
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Event(models.Model):
    creator = models.ForeignKey(User, default=-1)

    event_name = models.CharField(max_length=200)
    event_description = models.CharField(max_length=5000)
    begin_date = models.DateTimeField('begin date')
    end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.event_name

class Comment(models.Model):
    event = models.ForeignKey(Event)
    user = models.ForeignKey(User)

    creation_date = models.DateTimeField('comment date')
    text = models.CharField(max_length=400)
    votes = models.IntegerField(default=0) # redundant to upvoters
    upvoters = models.ManyToManyField(User, related_name='upvoters', blank=True)


    def __str__(self):
        return self.text