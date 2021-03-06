from __future__ import unicode_literals

# Start of the question model

import aristotle_mdr
from django.db import models


class Question(aristotle_mdr.models.concept):
    template = "extension_test/concepts/question.html"
    questionText = models.TextField(blank=True, null=True)
    responseLength = models.PositiveIntegerField(blank=True, null=True)
    collectedDataElement = models.ForeignKey(
        aristotle_mdr.models.DataElement,
        related_name="questions",
        null=True,
        blank=True
    )

# End of the question model


class Questionnaire(aristotle_mdr.models.concept):
    # Questionnaire is a test of a lazy developer who has done the bare minimum
    # To get an object in the system. This is a test of how little a dev can to
    # get a functional object. Ideally the string 'Questionnaire' should exist only here.
    edit_page_excludes = ['questions']
    # template = "extension_test/concepts/question.html"  # Blank to test default template
    questions = models.ManyToManyField(
        Question,
        related_name="questionnaires",
        null=True,
        blank=True
    )

    # Start of get_download_items
    def get_download_items(self):
        from collections import OrderedDict
        return OrderedDict([
            (
                Question,
                self.questions.all().order_by('name')
            ),
            (
                aristotle_mdr.models.DataElement,
                aristotle_mdr.models.DataElement.objects.filter(questions__questionnaires=self).order_by('name')
            ),
        ])
    # End of get_download_items
