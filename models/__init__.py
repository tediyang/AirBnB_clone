"""
    Make necessary imports
"""

from models.engine.file_storage import FileStorage

# Load the file from json format
storage = FileStorage()
storage.reload()
