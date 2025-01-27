# processors/food.py
from . import BaseProcessor

class FoodProcessor(BaseProcessor):
    def __init__(self):
        super().__init__()
        self.supported_detection_modes = ['single', 'multiple']
        self.supported_metadata = ['basic', 'nutritional']
        
    def process(self, image_data, settings):
        """
        Process food items with nutritional data extraction
        """
        self.validate_settings(settings)
        
        detection_mode = settings.get('detection', 'single')
        metadata_type = settings.get('metadata', 'basic')
        
        if detection_mode not in self.supported_detection_modes:
            raise ValueError(f"Unsupported detection mode: {detection_mode}")
            
        if metadata_type not in self.supported_metadata:
            raise ValueError(f"Unsupported metadata type: {metadata_type}")

        try:
            # Example processing logic
            result = {
                'model_url': 'food_model.obj',
                'preview_url': 'food_preview.png',
                'detection_mode': detection_mode,
                'detected_items': [
                    {
                        'name': 'Example Food Item',
                        'confidence': 0.95,
                        'nutrition': {
                            'calories': 100,
                            'protein': 5,
                            'carbs': 20,
                            'fat': 2
                        } if metadata_type == 'nutritional' else None
                    }
                ],
                'processing_time': 8.5
            }
            
            return result
            
        except Exception as e:
            raise Exception(f"Food processing failed: {str(e)}")