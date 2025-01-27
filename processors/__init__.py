# processors/__init__.py
from abc import ABC, abstractmethod

class BaseProcessor(ABC):
    def __init__(self):
        self.supported_formats = ['obj', 'glb']
        self.max_resolution = 2048

    @abstractmethod
    def process(self, image_data, settings):
        """Process the input image data with given settings"""
        pass

    def validate_settings(self, settings):
        """Validate the processing settings"""
        if 'resolution' in settings:
            width, height = map(int, settings['resolution'].split('x'))
            if width > self.max_resolution or height > self.max_resolution:
                raise ValueError(f"Resolution exceeds maximum of {self.max_resolution}x{self.max_resolution}")

    def cleanup(self):
        """Cleanup any temporary files"""
        pass