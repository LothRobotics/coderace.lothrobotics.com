from django.db import models

# Create your models here.

LEVEL_CHOICES = (
    ('easy', 'EASY'),
    ('medium', 'MEDIUM'),
    ('hard', 'HARD'),
    ('expert', 'EXPERT'),
)

SKILL_CHOICES = (
    ('problem solving (basic)', 'PROBLEM SOLVING (BASIC)'),
    ('problem solving (intermediate)', 'PROBLEM SOLVING (INTERMEDIATE)'),
    ('problem solving (advanced)', 'PROBLEM SOLVING (ADVANCED)'),
)

SUBDOMAINS = (
    ('data structures', 'DATA STRUCTURES'),
    ('implementation', 'IMPLEMENTATION'),
    ('search', 'SEARCH'),
    ('graph theory', 'GRAPH THEORY'),
    ('dynamic programming', 'DYNAMIC PROGRAMMING'),
    ('constructive algorithms', 'CONSTRUCTIVE ALGORITHMS'),
    ('bit manipulation', 'BIT MANIPULATION'),
    ('recursion', 'RECURSION'),
    ('debugging', 'DEBUGGING'),
)

class PractiseQuestion(models.Model):
    question_title = models.CharField(max_length=40)
    question_level = models.CharField(max_length=50, choices=LEVEL_CHOICES, default='easy')
    question_skillreq = models.CharField(max_length=50, choices=SKILL_CHOICES, default='problem solving (basic)')
    question_subdomain = models.CharField(max_length=50, choices=SUBDOMAINS, default='data structures')
    users_solved = models.IntegerField(editable=False)
    users_tried = models.IntegerField(editable=False)

    question_desc = models.CharField(max_length=1500)
    function_description = models.CharField(max_length=300)
    input_format = models.CharField(max_length=300)
    constraints = models.CharField(max_length=150)
    output_format = models.CharField(max_length=300)
    sample_input = models.CharField(max_length=50)
    sample_output = models.CharField(max_length=50)
    explanation = models.CharField(max_length=200)