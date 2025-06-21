from flask import Flask, render_template, request, jsonify, send_file  # type: ignore
import os
import uuid
from werkzeug.utils import secure_filename  # type: ignore
from image_converter import convert_image, check_imagemagick
import tempfile

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'

# Ensure directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

# All supported output formats
ALL_FORMATS = [
    'JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'HEIC', 'RAW', 'PSD', 'EXR', 'ICO', 'SVG', 'EPS', 'PDF', 'AI', 'CDR', 'APNG', 'SVGZ', 'DDS', 'TGA', 'JFIF', 'AVIF', 'PIC', 'XCF', 'DNG', 'PCX'
]

# Accept all as output, but restrict uploads to common image types
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff', 'webp', 'heic', 'raw', 'psd', 'exr', 'ico', 'svg', 'eps', 'pdf', 'ai', 'cdr', 'apng', 'svgz', 'dds', 'tga', 'jfif', 'avif', 'pic', 'xcf', 'dng', 'pcx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    # Check if ImageMagick is available
    imagemagick_available = check_imagemagick() is not None
    return render_template('index.html', all_formats=ALL_FORMATS, imagemagick_available=imagemagick_available)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400
    
    output_format = request.form.get('output_format', 'PNG').upper()
    if output_format not in ALL_FORMATS:
        return jsonify({'error': 'Invalid output format'}), 400
    
    try:
        # Generate unique filename
        file_id = str(uuid.uuid4())
        original_ext = file.filename.rsplit('.', 1)[1].lower()
        input_filename = f"{file_id}.{original_ext}"
        output_filename = f"{file_id}.{output_format.lower()}"
        
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], input_filename)
        output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)
        
        # Save uploaded file
        file.save(input_path)
        
        # Convert to selected format
        success = convert_image(input_path, output_path, output_format)
        
        if success:
            # Clean up input file
            os.remove(input_path)
            
            # Check if the output file was actually created
            if os.path.exists(output_path):
                return jsonify({
                    'success': True,
                    'filename': output_filename,
                    'original_name': file.filename,
                    'output_format': output_format
                })
            else:
                # If output file doesn't exist, the conversion might have failed silently
                return jsonify({'error': 'Conversion completed but output file not found'}), 500
        else:
            # Clean up on failure
            if os.path.exists(input_path):
                os.remove(input_path)
            
            # Check if ImageMagick is needed for this format
            from image_converter import pillow_can_write
            if not pillow_can_write(output_format):
                imagemagick_available = check_imagemagick() is not None
                if not imagemagick_available:
                    return jsonify({
                        'error': f'Conversion to {output_format} requires ImageMagick, which is not installed. Please install ImageMagick or try a different format.'
                    }), 500
                else:
                    return jsonify({'error': f'Conversion to {output_format} failed. The format might not be supported or the input file might be corrupted.'}), 500
            else:
                return jsonify({'error': 'Conversion failed. The input file might be corrupted or unsupported.'}), 500
            
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_file(
            os.path.join(app.config['OUTPUT_FOLDER'], filename),
            as_attachment=True,
            download_name=f"converted_{filename}"
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 404

@app.route('/cleanup/<filename>', methods=['DELETE'])
def cleanup_file(filename):
    try:
        file_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Production settings
    app.run(host='0.0.0.0', port=5001, debug=False) 