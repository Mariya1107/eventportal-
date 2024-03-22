from django.db import models


DEPARTMENTS = [
    ("CSE", "Computer Science and Engineering"),
    ("ECE", "Electronics and Communication Engineering"),
    ("EEE", "Electrical and Electronics Engineering"),
    ("ME", "Mechanical Engineering"),
    ("CE", "Civil Engineering"),
    (None, "None")
]
class Event(models.Model):
    title=models.CharField(max_length=30)
    venue=models.CharField(max_length=30)
    date=models.DateField
    time=models.CharField(max_length=30)
    desc=models.TextField
    img=models.ImageField(upload_to='event_img')
    dept=models.CharField(max_length=30,choices=DEPARTMENTS,default=None)
    reg_link=models.URLField(max_length=30)


