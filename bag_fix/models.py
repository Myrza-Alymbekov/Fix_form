from django.db import models


class Complaints(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    importance = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Files(models.Model):
    file = models.FileField(upload_to='info', blank=True, null=True, verbose_name='Файл')
    complaint = models.ForeignKey(Complaints, blank=True, null=True, on_delete=models.CASCADE)


