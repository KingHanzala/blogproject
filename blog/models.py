from django.db import models

# Create a Blog Model
class Blog(models.Model):
    title=models.CharField(max_length=255)
    pubdate=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title
    def pd(self):
        return self.pubdate.strftime("%e %b %Y")
    def id(self):
        return self.ID

# migrate

# admin


