# NGP-Server

A server implementation for converting Seeedstudio recamera images into 3D scenes using NVIDIA Instant NeRF.

## Features

- Multiple processing pipelines for different use cases:
  - Art & Assets: Optimized for artwork and physical objects
  - Food Scanner: Specialized for food recognition and 3D modeling
  - General Purpose: Standard 3D model generation
- GPU-accelerated processing using NVIDIA Instant NeRF
- RESTful API interface
- Configurable processing settings

## Cloud Deployment

### Prerequisites

- Google Cloud SDK installed
- Access to Google Cloud with GPU quotas enabled
- Git

### Deployment Steps

1. Clone the repository:
```bash
git clone https://github.com/Hey-Salad/NGP-Server.git
cd NGP-Server
```

2. Enable required Google Cloud APIs:
```bash
gcloud services enable compute.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

3. Deploy to Google Cloud:
```bash
gcloud app deploy app.yaml
```

## API Documentation

### Endpoints

- `GET /api/health` - Health check
- `GET /api/processors` - List available processors
- `GET /api/settings` - Get processing settings
- `POST /api/process` - Process an image

### Processing an Image

```bash
curl -X POST http://[YOUR-APP-URL]/api/process \
  -F "file=@image.jpg" \
  -F "type=art" \
  -F 'settings={"resolution": "1024x1024", "style": "realistic"}'
```

## Development

While the application is designed to run on Google Cloud with GPU support, you can run parts of it locally for development:

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (without GPU features)
python app.py
```

## License

Copyright (C) 2025-2026 HeySalad Inc.

Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only). See [LICENSE](LICENSE) and [NOTICE](NOTICE). If you run a modified version of this software to provide a network service, the AGPL requires you to offer its users the corresponding source code. Versions published before this change remain under their previous licence.
