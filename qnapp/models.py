from django.db import models

class AllQuestions(models.Model):
    id = models.AutoField(primary_key=True)
    Question_Title = models.TextField()
    Option_1 = models.TextField()
    Option_2 = models.TextField()
    Option_3 = models.TextField()
    Option_4 = models.TextField()
    Answer = models.TextField()
    Description = models.TextField()

    def save(self, *args, **kwargs):
        if self.Answer not in [self.Option_1, self.Option_2, self.Option_3, self.Option_4]:
            raise ValueError("Answer must match one of the options")
        super().save(*args, **kwargs)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(Answer=models.F('Option_1')) | 
                      models.Q(Answer=models.F('Option_2')) |
                      models.Q(Answer=models.F('Option_3')) |
                      models.Q(Answer=models.F('Option_4')),
                name="answer_matches_option"
            )
        ]
