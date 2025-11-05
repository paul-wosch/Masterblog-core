"""Masterblog-core: reusable blog engine core.

This package provides:
- Blog and Post models
- Storage helpers for JSON persistence

It is intended as a learning project and for reuse in other
projects, not for production use.
"""

__version__ = "0.1.0"

from .models import Blog, Post
from . import storage

__all__ = ["Blog", "Post", "storage", "__version__"]
