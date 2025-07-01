# Formatly - Image Format Converter

A sleek, modern web application for converting images between various formats with a beautiful dark-themed UI and smooth animations.

## Features

- 🎨 **Modern Dark UI** - Clean, professional interface with smooth animations
- 🔄 **Multiple Format Support** - Convert between 26+ image formats
- 📁 **Drag & Drop** - Easy file upload with drag and drop support
- ⚡ **Fast Conversion** - Powered by Pillow and ImageMagick
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- 🎭 **Animated Elements** - Rotating file type carousel for visual appeal

## Supported Formats

**Common Formats:** PNG, JPEG, JPG, GIF, BMP, TIFF, WEBP, ICO, TGA, PCX

**Advanced Formats:** HEIC, RAW, PSD, EXR, SVG, EPS, PDF, AI, CDR, APNG, SVGZ, DDS, JFIF, AVIF, PIC, XCF, DNG

*Note: Some advanced formats require ImageMagick to be installed (see optional installation below)*

## Prerequisites

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **ImageMagick** (optional) - For advanced format support

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/colepuls/Formatly.git
cd Formatly
```

### 2. Install Python Dependencies

```bash
# Create a virtual environment (recommended)
python -m venv formatly-env

# Activate virtual environment
# On Windows:
formatly-env\Scripts\activate
# On macOS/Linux:
source formatly-env/bin/activate

# Install required packages
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

### 4. Open in Browser

Open your web browser and navigate to:
```
http://localhost:5001
```

That's it! 🎉 You can now start converting images.

## Optional: ImageMagick Installation

For full format support (including PSD, EXR, AI, CDR, etc.), install ImageMagick:

### Windows
1. Download from [ImageMagick Downloads](https://imagemagick.org/script/download.php#windows)
2. Run the installer
3. Restart your command prompt

### macOS
```bash
# Using Homebrew
brew install imagemagick

# Using MacPorts
sudo port install ImageMagick
```

### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install imagemagick
```

### Linux (CentOS/RHEL)
```bash
sudo yum install ImageMagick
# or on newer versions:
sudo dnf install ImageMagick
```

## Usage

1. **Upload an Image**: Drag and drop a file or click to browse
2. **Select Output Format**: Choose from 26+ supported formats
3. **Convert**: Click the convert button
4. **Download**: Your converted image will be ready for download

## Supported Input Formats

The app accepts these input formats:
- PNG, JPG, JPEG, GIF, BMP, TIFF, WEBP
- HEIC, RAW, PSD, EXR, ICO, SVG, EPS
- PDF, AI, CDR, APNG, SVGZ, DDS, TGA
- JFIF, AVIF, PIC, XCF, DNG, PCX

## Project Structure

```
Formatly/
├── app.py              # Main Flask application
├── image_converter.py  # Image conversion logic
├── wsgi.py            # WSGI configuration
├── requirements.txt   # Python dependencies
├── templates/
│   └── index.html     # Web interface
├── uploads/           # Temporary upload storage
├── outputs/           # Converted files
└── test_image_converter.py  # Unit tests
```

## Running Tests

```bash
python -m pytest test_image_converter.py -v
```

## Troubleshooting

### "Conversion failed" errors
- **Check file format**: Ensure your input file is a valid image
- **Install ImageMagick**: Some formats require ImageMagick
- **File size**: Large files may take longer to process

### Port already in use
If port 5001 is busy, the app will show an error. You can:
1. Stop other applications using port 5001
2. Or modify `app.py` line 122 to use a different port:
   ```python
   app.run(host='0.0.0.0', port=5002, debug=False)
   ```

### Virtual environment issues
```bash
# Deactivate current environment
deactivate

# Remove old environment
rm -rf formatly-env

# Create new environment
python -m venv formatly-env
source formatly-env/bin/activate  # or formatly-env\Scripts\activate on Windows
pip install -r requirements.txt
```

## Development

### Adding New Formats
To add support for new formats:
1. Add the format to `ALL_FORMATS` list in `app.py`
2. Add the extension to `ALLOWED_EXTENSIONS` set
3. Test conversion in `image_converter.py`

### Modifying the UI
The web interface is in `templates/index.html` with inline CSS and JavaScript.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-format`)
3. Make your changes
4. Run tests (`python -m pytest`)
5. Commit changes (`git commit -am 'Add new format support'`)
6. Push to branch (`git push origin feature/new-format`)
7. Create a Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues:
1. Check the [Troubleshooting](#troubleshooting) section
2. Search existing [GitHub Issues](https://github.com/colepuls/Formatly/issues)
3. Create a new issue with details about your problem

---

**Made with ❤️ for easy image conversion**
