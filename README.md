# Formatly

A web application for converting images between different formats.

## Why I Built Formatly

I created Formatly out of personal frustration with existing image conversion tools. Many of them are cluttered with ads, require unnecessary clicks, or hide key features behind paywalls. I wanted a clean, fast, ad-free tool that I could trust and use regularly without hassle.

As someone who often needs to convert images for website submissions, projects, and platform compatibility, I realized a lot of people likely face the same issue. Formatly is built to be simple and functional, no distractions, just quick file conversions.

## Scalability

Formatly is designed with scalability in mind:

- **Modular Backend**: The image conversion logic is separated into its own module, making it easy to extend support for additional formats or processing features.
- **Flask API-Ready**: The app can easily be adapted into a RESTful API for integration with other applications or services.
- **Authentication & Storage (Future Scope)**: With minor additions, Formatly could support user accounts, saved conversion history, cloud storage, and usage analytics.
- **UI Enhancements**: The current frontend is built with vanilla JS, but could be migrated to React or another framework for a more dynamic experience.
- **Performance Optimization**: The current architecture supports easy integration of caching, CDN, and load balancing for high-traffic scenarios.

Whether used as a personal tool or expanded into a public service, Formatly is built to grow.

## Live Demo

**Try it online:** [https://web-production-1acc.up.railway.app/](https://web-production-1acc.up.railway.app/)

## Technology Stack

<div align="center">

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

**Backend:** Python, Flask, Pillow (PIL), Gunicorn  
**Frontend:** HTML5, CSS3, Vanilla JavaScript  
**Image Processing:** Pillow + ImageMagick 

</div>

## Interface Preview

<div align="center">

![Formatly Interface](assets/screenshot1.png)

![Formatly in Action](assets/screenshot2.png)

</div>

## Supported Formats

**Common:** PNG, JPEG, JPG, GIF, BMP, TIFF, WEBP, ICO, TGA, PCX

**Advanced:** HEIC, RAW, PSD, EXR, SVG, EPS, PDF, AI, CDR, APNG, SVGZ, DDS, JFIF, AVIF, PIC, XCF, DNG

*Advanced formats require ImageMagick*

## Local Development

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
└── wsgi.py           # WSGI entry point
```

---

**Made by Cole Puls**
