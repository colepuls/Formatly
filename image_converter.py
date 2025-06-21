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
        bool: True if conversion was successful, False otherwise
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_path):
            return False
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        fmt = output_format.upper()
        
        # If Pillow can handle this format, use it
        if pillow_can_write(fmt):
            with Image.open(input_path) as img:
                if fmt in ['JPEG', 'JPG']:
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'JPEG', quality=95)
                elif fmt == 'PNG':
                    if img.mode in ('RGBA', 'LA', 'P'):
                        if img.mode == 'RGBA':
                            converted_img = img.convert('RGBA')
                        else:
                            converted_img = img.convert('RGB')
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'PNG')
                elif fmt == 'GIF':
                    if img.mode == 'P':
                        converted_img = img
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'GIF')
                elif fmt == 'BMP':
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'BMP')
                elif fmt == 'TIFF':
                    if img.mode in ('RGBA', 'LA', 'P'):
                        converted_img = img
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'TIFF')
                elif fmt == 'WEBP':
                    if img.mode in ('RGBA', 'LA', 'P'):
                        if img.mode == 'RGBA':
                            converted_img = img.convert('RGBA')
                        else:
                            converted_img = img.convert('RGB')
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'WEBP')
                elif fmt == 'ICO':
                    converted_img = img.convert('RGBA')
                    converted_img.save(output_path, 'ICO')
                elif fmt == 'TGA':
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'TGA')
                elif fmt == 'PCX':
                    converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'PCX')
                else:
                    # Default to PNG for unsupported formats
                    if img.mode in ('RGBA', 'LA', 'P'):
                        if img.mode == 'RGBA':
                            converted_img = img.convert('RGBA')
                        else:
                            converted_img = img.convert('RGB')
                    else:
                        converted_img = img.convert('RGB')
                    converted_img.save(output_path, 'PNG')
            return True
        
        # For advanced formats, try ImageMagick
        else:
            magick_cmd = check_imagemagick()
            if magick_cmd:
                try:
                    if magick_cmd == 'magick':
                        # ImageMagick 7+ syntax
                        cmd = ['magick', input_path, output_path]
                    else:
                        # ImageMagick 6 syntax
                        cmd = ['convert', input_path, output_path]
                    
                    result = subprocess.run(cmd, capture_output=True, check=True, timeout=30)
                    return True
                except subprocess.TimeoutExpired:
                    print(f"ImageMagick conversion timed out for {input_path}")
                    return False
                except subprocess.CalledProcessError as e:
                    print(f"ImageMagick conversion failed: {e.stderr.decode()}")
                    return False
                except Exception as e:
                    print(f"ImageMagick error: {e}")
                    return False
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
                        
                        # Change output path to PNG
                        png_output = output_path.rsplit('.', 1)[0] + '.png'
                        converted_img.save(png_output, 'PNG')
                        
                        # If the original output path is different, rename
                        if png_output != output_path:
                            os.rename(png_output, output_path)
                        
                        return True
                except Exception as e:
                    print(f"Fallback conversion failed: {e}")
                    return False
                    
    except Exception as e:
        print(f"Error converting image: {e}")
        return False

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