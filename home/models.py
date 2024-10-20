from django.db import models


class Contact(models.Model):
    """
    The Contact model represents messages sent through the contact us form.
    Stores user inquiries or feedback, including name, email, and the message itself.
    """
    name = models.CharField(max_length=254, help_text="The name of the user.")
    email = models.EmailField(help_text="The user's email address.")
    subject = models.CharField(max_length=254, help_text="The subject of the message.")
    message = models.TextField(help_text="The message content.")
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="The date and time when the message was sent.")
    
    def __str__(self):
        return f'Message from {self.name} - {self.subject}'

