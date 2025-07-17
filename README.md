# Formatly

A web application for converting images between different formats.

## Technology Stack

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

**Backend:** Python, Flask, Pillow (PIL), Gunicorn  
**Frontend:** HTML5, CSS3, Vanilla JavaScript  
**Image Processing:** Pillow + ImageMagick (optional)  

</div>

## Interface Preview

<div align="center">

![Formatly Interface](assets/formatly-screenshot.png)

![Formatly in Action](assets/formatly-screenshot2.png)

</div>

## Supported Formats

**Common:** PNG, JPEG, JPG, GIF, BMP, TIFF, WEBP, ICO, TGA, PCX

**Advanced:** HEIC, RAW, PSD, EXR, SVG, EPS, PDF, AI, CDR, APNG, SVGZ, DDS, JFIF, AVIF, PIC, XCF, DNG

*Advanced formats require ImageMagick*

## Deployment

### Railway (Recommended)

Railway is the recommended hosting platform for Formatly as it supports system dependencies like ImageMagick.

1. **Fork or clone this repository**
2. **Connect to Railway:**
   - Go to [Railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your Formatly repository
3. **Deploy:**
   - Railway will automatically detect the Python app
   - It will install ImageMagick and Python dependencies
   - Your app will be deployed with full functionality

**Railway automatically handles:**
- ImageMagick installation
- Python dependency management
- SSL certificates
- Custom domains
- Auto-deployment from GitHub

### Local Development

#### Prerequisites
- Python 3.8+
- ImageMagick (optional, for advanced formats)

#### Setup

```bash
git clone https://github.com/colepuls/Formatly.git
cd Formatly
pip install -r requirements.txt
python3 app.py
```

Open http://localhost:5001

#### ImageMagick Installation

**macOS:**
```bash
brew install imagemagick
```

**Windows:**
Download from [ImageMagick Downloads](https://imagemagick.org/script/download.php#windows)

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install imagemagick
```

## Usage

1. Upload an image by dragging or clicking
2. Select output format
3. Click convert
4. Download converted image

## Project Structure

```
Formatly/
├── app.py              # Main application
├── image_converter.py  # Conversion logic
├── templates/
│   └── index.html     # Web interface
├── requirements.txt   # Dependencies
├── railway.json       # Railway configuration
├── nixpacks.toml      # Build configuration
├── Dockerfile         # Docker configuration
└── wsgi.py           # WSGI entry point
```

## Configuration Files

- **`railway.json`**: Railway deployment settings
- **`nixpacks.toml`**: Build configuration with ImageMagick
- **`Dockerfile`**: Alternative Docker deployment
- **`Procfile`**: Process management for gunicorn

---

**Made by Cole Puls**
