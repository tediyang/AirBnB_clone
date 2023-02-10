"""
    Make necessary imports
"""

from engine.file_storage import FileStorage

# Load the file from json format
storage = FileStorage()
storage.reload()