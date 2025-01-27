# processors/general.py
from . import BaseProcessor
import subprocess
import os

class GeneralProcessor(BaseProcessor):
    def __init__(self):
        super().__init__()
        self.optimization_modes = ['speed', 'quality']
        
    def process(self, image_data, settings):
        """
        General purpose processing with basic optimization settings
        """
        self.validate_settings(settings)
        
        optimization = settings.get('optimization', 'quality')
        output_format = settings.get('format', 'obj')
        
        if optimization not in self.optimization_modes:
            raise ValueError(f"Unsupported optimization mode: {optimization}")
            
        if output_format not in self.supported_formats:
            raise ValueError(f"Unsupported format: {output_format}")

        try:
            # Example processing logic
            result = {
                'model_url': f'general_model.{output_format}',
                'preview_url': 'preview.png',
                'processing_time': 12.0,
                'optimization': optimization,
                'format': output_format
            }
            
            return result
            
        except Exception as e:
            raise Exception(f"General processing failed: {str(e)}")