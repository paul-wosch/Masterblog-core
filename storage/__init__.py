"""Provide functions for persistent data storage.

This package exports the following functions:
- `read_json_file`: Read data from a JSON file.
- `write_json_file`: Write data to a JSON file.
"""
from .filestore import read_json_file, write_json_file

__all__ = ["read_json_file", "write_json_file"]
