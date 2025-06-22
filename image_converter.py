import os
import subprocess
from PIL import Image  # type: ignore

# Formats Pillow can write
PILLOW_FORMATS = {
    'JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX'
}

def pillow_can_write(fmt):
    return fmt.upper() in PILLOW_FORMATS

def check_imagemagick():
    """Check if ImageMagick is available"""
    try:
        # Try 'magick' command first (ImageMagick 7+)
        result = subprocess.run(['magick', '-version'], capture_output=True, check=True)
        return 'magick'
    except:
        try:
            # Try 'convert' command (ImageMagick 6)
            result = subprocess.run(['convert', '-version'], capture_output=True, check=True)
            return 'convert'
        except:
            return None

def convert_image(input_path, output_path, output_format='PNG'):
    """
    Convert any supported image format to the specified output format.
    Uses Pillow for common formats, falls back to ImageMagick for advanced formats.
    
    Args:
        input_path (str): Path to the input image file
        output_path (str): Path where the output file should be saved
        output_format (str): Desired output format (PNG, JPEG, GIF, etc.)
    
    Returns:
        tuple: (success: bool, actual_format: str, actual_filename: str)
    """
    try:
        if not os.path.exists(input_path):
            return False, None, None
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        fmt = output_format.upper() if output_format else 'PNG'
        # If Pillow can handle this format, use it
        if pillow_can_write(fmt):
            with Image.open(input_path) as img:
                if fmt in ['JPEG', 'JPG']:
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'JPEG', quality=95)
                    return True, 'JPEG', output_path
                elif fmt == 'PNG':
                    if img.mode in ('RGBA', 'LA', 'P'):
                        if img.mode == 'RGBA':
                            converted_img = img.convert('RGBA')
                        else:
                            converted_img = img.convert('RGB')
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'PNG')
                    return True, 'PNG', output_path
                elif fmt == 'GIF':
                    if img.mode == 'P':
                        converted_img = img
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'GIF')
                    return True, 'GIF', output_path
                elif fmt == 'BMP':
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'BMP')
                    return True, 'BMP', output_path
                elif fmt == 'TIFF':
                    if img.mode in ('RGBA', 'LA', 'P'):
                        converted_img = img
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'TIFF')
                    return True, 'TIFF', output_path
                elif fmt == 'WEBP':
                    if img.mode in ('RGBA', 'LA', 'P'):
                        if img.mode == 'RGBA':
                            converted_img = img.convert('RGBA')
                        else:
                            converted_img = img.convert('RGB')
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'WEBP')
                    return True, 'WEBP', output_path
                elif fmt == 'ICO':
                    converted_img = img.convert('RGBA')
                    converted_img.save(output_path, 'ICO')
                    return True, 'ICO', output_path
                elif fmt == 'TGA':
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'TGA')
                    return True, 'TGA', output_path
                elif fmt == 'PCX':
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'PCX')
                    return True, 'PCX', output_path
                else:
                    # Default to PNG for unsupported formats
                    if img.mode in ('RGBA', 'LA', 'P'):
                        if img.mode == 'RGBA':
                            converted_img = img.convert('RGBA')
                        else:
                            converted_img = img.convert('RGB')
                    else:
                        converted_img = img.convert('RGB')
                    # Change output_path to .png
                    png_output = output_path.rsplit('.', 1)[0] + '.png'
                    converted_img.save(png_output, 'PNG')
                    return True, 'PNG', png_output
        # For advanced formats, try ImageMagick
        else:
            magick_cmd = check_imagemagick()
            if magick_cmd:
                try:
                    if magick_cmd == 'magick':
                        cmd = ['magick', input_path, output_path]
                    else:
                        cmd = ['convert', input_path, output_path]
                    result = subprocess.run(cmd, capture_output=True, check=True, timeout=30)
                    return True, fmt, output_path
                except subprocess.TimeoutExpired:
                    print(f"ImageMagick conversion timed out for {input_path}")
                    return False, None, None
                except subprocess.CalledProcessError as e:
                    print(f"ImageMagick conversion failed: {e.stderr.decode()}")
                    return False, None, None
                except Exception as e:
                    print(f"ImageMagick error: {e}")
                    return False, None, None
            else:
                # If ImageMagick is not available, convert to PNG as fallback
                print(f"ImageMagick not available, converting {fmt} to PNG instead")
                try:
                    with Image.open(input_path) as img:
                        if img.mode in ('RGBA', 'LA', 'P'):
                            if img.mode == 'RGBA':
                                converted_img = img.convert('RGBA')
                            else:
                                converted_img = img.convert('RGB')
                        else:
                            converted_img = img.convert('RGB')
                        png_output = output_path.rsplit('.', 1)[0] + '.png'
                        converted_img.save(png_output, 'PNG')
                        return True, 'PNG', png_output
                except Exception as e:
                    print(f"Fallback conversion failed: {e}")
                    return False, None, None
    except Exception as e:
        print(f"Error converting image: {e}")
        return False, None, None

def convert_to_png(input_path, output_path):
    """
    Convert any supported image format to PNG (backward compatibility).
    
    Args:
        input_path (str): Path to the input image file
        output_path (str): Path where the PNG file should be saved
    
    Returns:
        bool: True if conversion was successful, False otherwise
    """
    return convert_image(input_path, output_path, 'PNG')