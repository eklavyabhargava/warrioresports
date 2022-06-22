from django.db import models

class Update(models.Model):
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=60)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

class tdm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    pubg_id = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class tdmtournament(models.Model):
    time = models.DateTimeField()

    def __str__(self):
        return str(self.time)

class classic(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.IntegerField()
    pubg_id = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class classictournament(models.Model):
    time = models.DateTimeField()

    def __str__(self):
        return str(self.time)