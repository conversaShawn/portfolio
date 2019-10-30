from django.db import models

class Contact(models.Model):
    # this is like schema in express IssueItemSchema = mongoose.Schema({description : String, done : Boolean})
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=15)
    message = models.CharField(max_length=5000)
