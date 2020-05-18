from django.db import models


# Create your models here.


class Toy(models.Model):
    """Model definition for Toy."""

    name = models.CharField(max_length=150, blank=False, default='')
    description = models.CharField(max_length=250, blank=True, default='')
    toy_category = models.CharField(max_length=200, blank=False, default='')
    was_included_in_home = models.BooleanField(default=False)
    release_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Toy."""

        verbose_name = 'Toy'
        verbose_name_plural = 'Toys'
        ordering = ('name',)

    def __str__(self):
        """Unicode representation of Toy."""
        return self.name
