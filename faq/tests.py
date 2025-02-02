import pytest
from faq.models import FAQ

@pytest.mark.django_db
def test_get_translated_faq():
    """Test if get_translated_faq() correctly returns translated question & answer"""

    # Create an FAQ entry with translations
    faq = FAQ.objects.create(
        question="What is Django?",
        answer="Django is a Python web framework.",
    )

    # Test English (default)
    result_en = faq.get_translated_faq(lang="en")
    assert result_en["question"] == "What is Django?"
    assert result_en["answer"] == "Django is a Python web framework."
