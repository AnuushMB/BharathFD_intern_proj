from django.db import models

# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator
from django.core.cache import cache

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG support

    # Translations for multiple languages
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)


    def get_translated_faq(self, lang='en'):
        """Retrieve translated question & answer"""
        
        if lang == "hi":
            translated_qn = self.question_hi
        elif lang == "bn":
            translated_qn = self.question_bn
        else:
            translated_qn = self.question
        return {
            "id": self.id,
            "question":  translated_qn,
            "answer": self.answer
            
        }

    def save(self, *args, **kwargs):
        """Auto-translate question when saving"""
        translator = Translator()
        self.question_hi = translator.translate(self.question, dest='hi').text
        self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question

