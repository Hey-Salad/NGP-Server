from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
from processors.art import ArtProcessor
from processors.food import FoodProcessor
from processors.general import GeneralProcessor
import uuid
from werkzeug.utils import secure_filename
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__, static_folder='static')
CORS(app)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Initialize processors
processors = {
    'art': ArtProcessor(),
    'food': FoodProcessor(),
    'general': GeneralProcessor()
}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def serve_static():
    return send_from_directory('static', 'index.html')

@app.route('/api/health')
def health_check():
    return jsonify({'status': 'healthy'})

@app.route('/api/processors')
def get_processors():
    """Get available processors and their configurations"""
    return jsonify({
        'processors': {
            'art': {
                'supported_styles': processors['art'].supported_styles,
                'supported_formats': processors['art'].supported_formats
            },
            'food': {
                'detection_modes': processors['food'].supported_detection_modes,
                'metadata_types': processors['food'].supported_metadata
            },
            'general': {
                'optimization_modes': processors['general'].optimization_modes,
                'supported_formats': processors['general'].supported_formats
            }
        }
    })

@app.route('/api/process', methods=['POST'])
def process_image():
    """Process an uploaded image"""
    try:
        # Check if a file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
            
        if not allowed_file(file.filename):
            return jsonify({'error': 'File type not allowed'}), 400

        # Get processing type and settings
        processor_type = request.form.get('type', 'general')
        settings = json.loads(request.form.get('settings', '{}'))

        if processor_type not in processors:
            return jsonify({'error': 'Invalid processor type'}), 400

        # Create unique filename
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        filepath = os.path.join(UPLOAD_FOLDER, unique_filename)

        # Save the file
        file.save(filepath)
        logger.info(f"Saved file: {filepath}")

        try:
            # Process the image
            processor = processors[processor_type]
            result = processor.process(filepath, settings)

            return jsonify({
                'status': 'success',
                'result': result
            })

        finally:
            # Cleanup
            try:
                os.remove(filepath)
                logger.info(f"Cleaned up file: {filepath}")
            except Exception as e:
                logger.error(f"Error cleaning up file {filepath}: {str(e)}")

    except Exception as e:
        logger.error(f"Processing error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/settings', methods=['GET'])
def get_settings():
    """Get available settings for all processors"""
    return jsonify({
        'art': {
            'resolution': ['512x512', '1024x1024', '2048x2048'],
            'style': processors['art'].supported_styles,
            'format': processors['art'].supported_formats
        },
        'food': {
            'resolution': ['512x512', '1024x1024'],
            'detection': processors['food'].supported_detection_modes,
            'metadata': processors['food'].supported_metadata
        },
        'general': {
            'resolution': ['512x512', '1024x1024', '2048x2048'],
            'optimization': processors['general'].optimization_modes,
            'format': processors['general'].supported_formats
        }
    })

if __name__ == '__main__':
    # Ensure upload directory exists
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    
    # Start the application
    app.run(host='0.0.0.0', port=8080, debug=True)