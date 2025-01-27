# processors/art.py
from . import BaseProcessor
import subprocess
import os

class ArtProcessor(BaseProcessor):
    def __init__(self):
        super().__init__()
        self.supported_styles = ['realistic', 'stylized']
        
    def process(self, image_data, settings):
        """
        Process art assets with specific style settings
        """
        self.validate_settings(settings)
        
        style = settings.get('style', 'realistic')
        output_format = settings.get('format', 'obj')
        
        if style not in self.supported_styles:
            raise ValueError(f"Unsupported style: {style}")
            
        if output_format not in self.supported_formats:
            raise ValueError(f"Unsupported format: {output_format}")

        # Here we'll add the instant-ngp processing
        try:
            # Example processing logic
            result = {
                'model_url': f'processed_model.{output_format}',
                'preview_url': 'preview.png',
                'processing_time': 10.5,
                'style': style,
                'format': output_format
            }
            
            return result
            
        except Exception as e:
            raise Exception(f"Art processing failed: {str(e)}")