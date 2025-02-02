from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG support

   

    def get_translated_faq(self, lang='en'):
        """Retrieve translated question & answer"""
        translated_ans = self.answer
        return {
            "id": self.id,
            "question": getattr(self, f"question_{lang}", self.question),
            "answer": translated_ans
            
        }

    def save(self, *args, **kwargs):
        """Auto-translate question when saving"""
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

