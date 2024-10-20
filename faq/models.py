from django.db import models

class FAQ(models.Model):
    """
    FAQ Model to store frequently asked questions and their answers.
    """
    question = models.CharField(max_length=255, help_text="Enter the FAQ question.")
    answer = models.TextField(help_text="Enter the answer for the FAQ.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQs'
        ordering = ['-created_at']

    def __str__(self):
        return self.question
