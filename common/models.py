"""
Common base model with timestamp and soft-delete support.
All HRMS models should inherit from BaseModel or TimestampedModel.
"""

import uuid
from django.db import models
from django.utils import timezone


class TimestampedModel(models.Model):
    """
    Abstract base model providing created_at and updated_at timestamps.
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class BaseModel(TimestampedModel):
    """
    Abstract base model with UUID primary key, timestamps and soft-delete.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_active = models.BooleanField(default=True, db_index=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        """Mark record as deleted without removing from database."""
        self.deleted_at = timezone.now()
        self.is_active = False
        self.save(update_fields=['deleted_at', 'is_active', 'updated_at'])

    def restore(self):
        """Restore a soft-deleted record."""
        self.deleted_at = None
        self.is_active = True
        self.save(update_fields=['deleted_at', 'is_active', 'updated_at'])

    @property
    def is_deleted(self):
        return self.deleted_at is not None


class ActiveManager(models.Manager):
    """Manager that returns only non-deleted, active records."""

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True, is_active=True)
