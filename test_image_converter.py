import unittest
import os
import tempfile
from PIL import Image  # type: ignore
import numpy as np  # type: ignore
from image_converter import convert_image, convert_to_png, pillow_can_write, check_imagemagick
import shutil


class TestImageConverter(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Clean up after each test method."""
        # Recursively remove the test directory and all its contents
        shutil.rmtree(self.test_dir)
    
    def create_test_image(self, format_name, size=(100, 100), color=(255, 0, 0), mode='RGB'):
        """Helper method to create test images in different formats."""
        img = Image.new(mode, size, color)
        filename = f"test_image.{format_name.lower()}"
        filepath = os.path.join(self.test_dir, filename)
        
        # Handle format-specific saving
        if format_name.lower() == 'jpg':
            img.save(filepath, format='JPEG')
        else:
            img.save(filepath, format=format_name.upper())
        return filepath
    
    def test_pillow_can_write_function(self):
        """Test the pillow_can_write helper function."""
        # Test supported formats
        supported_formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        for fmt in supported_formats:
            with self.subTest(format=fmt):
                self.assertTrue(pillow_can_write(fmt))
                self.assertTrue(pillow_can_write(fmt.lower()))
        
        # Test unsupported formats
        unsupported_formats = ['SVG', 'PDF', 'AVIF', 'HEIC', 'UNSUPPORTED_FORMAT']
        for fmt in unsupported_formats:
            with self.subTest(format=fmt):
                self.assertFalse(pillow_can_write(fmt))
    
    def test_check_imagemagick_function(self):
        """Test the check_imagemagick helper function."""
        result = check_imagemagick()
        # This should return either 'magick', 'convert', or None
        self.assertIn(result, ['magick', 'convert', None])
    
    def test_convert_to_jpeg(self):
        """Test converting to JPEG format."""
        png_path = self.create_test_image('png')
        jpeg_path = os.path.join(self.test_dir, "output.jpg")
        
        result = convert_image(png_path, jpeg_path, 'JPEG')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(jpeg_path))
        
        with Image.open(jpeg_path) as img:
            self.assertEqual(img.format, 'JPEG')
            self.assertEqual(img.mode, 'RGB')  # JPEG should be RGB
    
    def test_convert_to_jpg(self):
        """Test converting to JPG format."""
        png_path = self.create_test_image('png')
        jpg_path = os.path.join(self.test_dir, "output.jpg")
        
        result = convert_image(png_path, jpg_path, 'JPG')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(jpg_path))
        
        with Image.open(jpg_path) as img:
            self.assertEqual(img.format, 'JPEG')
            self.assertEqual(img.mode, 'RGB')  # JPG should be RGB
    
    def test_convert_to_png(self):
        """Test converting to PNG format."""
        jpg_path = self.create_test_image('jpg')
        png_path = os.path.join(self.test_dir, "output.png")
        
        result = convert_image(jpg_path, png_path, 'PNG')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(png_path))
        
        with Image.open(png_path) as img:
            self.assertEqual(img.format, 'PNG')
    
    def test_convert_to_gif(self):
        """Test converting to GIF format."""
        png_path = self.create_test_image('png')
        gif_path = os.path.join(self.test_dir, "output.gif")
        
        result = convert_image(png_path, gif_path, 'GIF')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(gif_path))
        
        with Image.open(gif_path) as img:
            self.assertEqual(img.format, 'GIF')
    
    def test_convert_to_bmp(self):
        """Test converting to BMP format."""
        png_path = self.create_test_image('png')
        bmp_path = os.path.join(self.test_dir, "output.bmp")
        
        result = convert_image(png_path, bmp_path, 'BMP')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(bmp_path))
        
        with Image.open(bmp_path) as img:
            self.assertEqual(img.format, 'BMP')
            self.assertEqual(img.mode, 'RGB')  # BMP should be RGB
    
    def test_convert_to_tiff(self):
        """Test converting to TIFF format."""
        png_path = self.create_test_image('png')
        tiff_path = os.path.join(self.test_dir, "output.tiff")
        
        result = convert_image(png_path, tiff_path, 'TIFF')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(tiff_path))
        
        with Image.open(tiff_path) as img:
            self.assertEqual(img.format, 'TIFF')
    
    def test_convert_to_webp(self):
        """Test converting to WebP format."""
        png_path = self.create_test_image('png')
        webp_path = os.path.join(self.test_dir, "output.webp")
        
        result = convert_image(png_path, webp_path, 'WEBP')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(webp_path))
        
        with Image.open(webp_path) as img:
            self.assertEqual(img.format, 'WEBP')
    
    def test_convert_to_ico(self):
        """Test converting to ICO format."""
        png_path = self.create_test_image('png')
        ico_path = os.path.join(self.test_dir, "output.ico")
        
        result = convert_image(png_path, ico_path, 'ICO')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(ico_path))
        
        with Image.open(ico_path) as img:
            self.assertEqual(img.format, 'ICO')
            self.assertEqual(img.mode, 'RGBA')  # ICO should be RGBA
    
    def test_convert_to_tga(self):
        """Test converting to TGA format."""
        png_path = self.create_test_image('png')
        tga_path = os.path.join(self.test_dir, "output.tga")
        
        result = convert_image(png_path, tga_path, 'TGA')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(tga_path))
        
        with Image.open(tga_path) as img:
            self.assertEqual(img.format, 'TGA')
            self.assertEqual(img.mode, 'RGB')  # TGA should be RGB
    
    def test_convert_to_pcx(self):
        """Test converting to PCX format."""
        png_path = self.create_test_image('png')
        pcx_path = os.path.join(self.test_dir, "output.pcx")
        
        result = convert_image(png_path, pcx_path, 'PCX')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(pcx_path))
        
        with Image.open(pcx_path) as img:
            self.assertEqual(img.format, 'PCX')
            self.assertEqual(img.mode, 'RGB')  # PCX should be RGB
    
    def test_convert_from_jpg_to_all_formats(self):
        """Test converting from JPG to all supported formats."""
        jpg_path = self.create_test_image('jpg')
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(jpg_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    # Check that the format is correct
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_from_gif_to_all_formats(self):
        """Test converting from GIF to all supported formats."""
        gif_path = self.create_test_image('gif')
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(gif_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_from_bmp_to_all_formats(self):
        """Test converting from BMP to all supported formats."""
        bmp_path = self.create_test_image('bmp')
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(bmp_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_from_tiff_to_all_formats(self):
        """Test converting from TIFF to all supported formats."""
        tiff_path = self.create_test_image('tiff')
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(tiff_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_from_webp_to_all_formats(self):
        """Test converting from WebP to all supported formats."""
        webp_path = self.create_test_image('webp')
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(webp_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_with_transparency_to_rgba_formats(self):
        """Test converting transparent images to formats that support transparency."""
        # Create an image with transparency
        img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))
        png_input = os.path.join(self.test_dir, "transparent.png")
        img.save(png_input, 'PNG')
        
        # Test formats that should preserve transparency
        rgba_formats = ['PNG', 'WEBP', 'ICO', 'TIFF']
        
        for format_name in rgba_formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(png_input, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_with_transparency_to_rgb_formats(self):
        """Test converting transparent images to formats that don't support transparency."""
        # Create an image with transparency
        img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))
        png_input = os.path.join(self.test_dir, "transparent.png")
        img.save(png_input, 'PNG')
        
        # Test formats that should convert to RGB
        rgb_formats = ['JPEG', 'JPG', 'BMP', 'TGA', 'PCX']
        
        for format_name in rgb_formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(png_input, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                        self.assertEqual(img.mode, 'RGB')
                    else:
                        self.assertEqual(img.format, format_name)
                        self.assertEqual(img.mode, 'RGB')
    
    def test_convert_with_grayscale(self):
        """Test converting grayscale images to all formats."""
        img = Image.new('L', (100, 100), 128)
        grayscale_path = os.path.join(self.test_dir, "grayscale.jpg")
        img.save(grayscale_path, 'JPEG')
        
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(grayscale_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_with_palette(self):
        """Test converting palette-based images to all formats."""
        img = Image.new('P', (100, 100))
        palette_path = os.path.join(self.test_dir, "palette.gif")
        img.save(palette_path, 'GIF')
        
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(palette_path, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_with_different_sizes(self):
        """Test converting images with different sizes to all formats."""
        sizes = [(50, 50), (200, 150), (1000, 800)]
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for width, height in sizes:
            for format_name in formats:
                with self.subTest(size=(width, height), format=format_name):
                    jpg_path = self.create_test_image('jpg', size=(width, height))
                    output_path = os.path.join(self.test_dir, f"output_{width}x{height}.{format_name.lower()}")
                    
                    result = convert_image(jpg_path, output_path, format_name)
                    
                    self.assertTrue(result)
                    self.assertTrue(os.path.exists(output_path))
                    
                    with Image.open(output_path) as img:
                        # ICO format has size restrictions, so we don't check exact size for ICO
                        if format_name != 'ICO':
                            self.assertEqual(img.size, (width, height))
                        if format_name in ['JPEG', 'JPG']:
                            self.assertEqual(img.format, 'JPEG')
                        else:
                            self.assertEqual(img.format, format_name)
    
    def test_unsupported_format_defaults_to_png(self):
        """Test that unsupported formats default to PNG."""
        jpg_path = self.create_test_image('jpg')
        output_path = os.path.join(self.test_dir, "output.unsupported")
        
        result = convert_image(jpg_path, output_path, 'UNSUPPORTED_FORMAT')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_path))
        
        with Image.open(output_path) as img:
            self.assertEqual(img.format, 'PNG')
    
    def test_nonexistent_input_file(self):
        """Test handling of nonexistent input file."""
        nonexistent_path = os.path.join(self.test_dir, "nonexistent.jpg")
        output_path = os.path.join(self.test_dir, "output.png")
        
        result = convert_image(nonexistent_path, output_path, 'PNG')
        
        self.assertFalse(result)
        self.assertFalse(os.path.exists(output_path))
    
    def test_invalid_input_file(self):
        """Test handling of invalid input file."""
        # Create a text file instead of an image
        invalid_path = os.path.join(self.test_dir, "invalid.txt")
        with open(invalid_path, 'w') as f:
            f.write("This is not an image file")
        
        output_path = os.path.join(self.test_dir, "output.png")
        
        result = convert_image(invalid_path, output_path, 'PNG')
        
        self.assertFalse(result)
        self.assertFalse(os.path.exists(output_path))
    
    def test_output_directory_does_not_exist(self):
        """Test creating output directory if it doesn't exist."""
        jpg_path = self.create_test_image('jpg')
        non_existent_dir = os.path.join(self.test_dir, "new_dir")
        output_path = os.path.join(non_existent_dir, "output.png")
        
        result = convert_image(jpg_path, output_path, 'PNG')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_path))
        self.assertTrue(os.path.exists(non_existent_dir))
    
    def test_backward_compatibility_convert_to_png(self):
        """Test that the old convert_to_png function still works."""
        jpg_path = self.create_test_image('jpg')
        png_path = os.path.join(self.test_dir, "output.png")
        
        result = convert_to_png(jpg_path, png_path)
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(png_path))
        
        with Image.open(png_path) as img:
            self.assertEqual(img.format, 'PNG')
    
    def test_convert_with_different_colors(self):
        """Test converting images with different colors to all formats."""
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 255), (0, 0, 0)]
        formats = ['JPEG', 'JPG', 'PNG', 'GIF', 'BMP', 'TIFF', 'WEBP', 'ICO', 'TGA', 'PCX']
        
        for color in colors:
            for format_name in formats:
                with self.subTest(color=color, format=format_name):
                    jpg_path = self.create_test_image('jpg', color=color)
                    output_path = os.path.join(self.test_dir, f"output_{color[0]}_{color[1]}_{color[2]}.{format_name.lower()}")
                    
                    result = convert_image(jpg_path, output_path, format_name)
                    
                    self.assertTrue(result)
                    self.assertTrue(os.path.exists(output_path))
                    
                    with Image.open(output_path) as img:
                        if format_name in ['JPEG', 'JPG']:
                            self.assertEqual(img.format, 'JPEG')
                        else:
                            self.assertEqual(img.format, format_name)
    
    def test_convert_with_alpha_channel(self):
        """Test converting images with alpha channel to different formats."""
        # Create an image with alpha channel
        img = Image.new('RGBA', (100, 100), (255, 0, 0, 128))
        rgba_input = os.path.join(self.test_dir, "rgba.png")
        img.save(rgba_input, 'PNG')
        
        formats = ['PNG', 'WEBP', 'ICO', 'TIFF', 'JPEG', 'JPG', 'BMP', 'TGA', 'PCX']
        
        for format_name in formats:
            with self.subTest(format=format_name):
                output_path = os.path.join(self.test_dir, f"output.{format_name.lower()}")
                result = convert_image(rgba_input, output_path, format_name)
                
                self.assertTrue(result)
                self.assertTrue(os.path.exists(output_path))
                
                with Image.open(output_path) as img:
                    if format_name in ['JPEG', 'JPG']:
                        self.assertEqual(img.format, 'JPEG')
                        self.assertEqual(img.mode, 'RGB')  # Should convert to RGB
                    elif format_name in ['ICO']:
                        self.assertEqual(img.format, format_name)
                        self.assertEqual(img.mode, 'RGBA')  # Should preserve RGBA
                    else:
                        self.assertEqual(img.format, format_name)
    
    def test_convert_with_large_images(self):
        """Test converting large images to ensure performance."""
        large_sizes = [(1920, 1080), (2560, 1440), (3840, 2160)]
        formats = ['JPEG', 'PNG', 'WEBP']  # Test with most common formats
        
        for width, height in large_sizes:
            for format_name in formats:
                with self.subTest(size=(width, height), format=format_name):
                    jpg_path = self.create_test_image('jpg', size=(width, height))
                    output_path = os.path.join(self.test_dir, f"large_{width}x{height}.{format_name.lower()}")
                    
                    result = convert_image(jpg_path, output_path, format_name)
                    
                    self.assertTrue(result)
                    self.assertTrue(os.path.exists(output_path))
                    
                    with Image.open(output_path) as img:
                        self.assertEqual(img.size, (width, height))
                        if format_name in ['JPEG', 'JPG']:
                            self.assertEqual(img.format, 'JPEG')
                        else:
                            self.assertEqual(img.format, format_name)
    
    def test_convert_with_small_images(self):
        """Test converting very small images."""
        small_sizes = [(1, 1), (10, 10), (16, 16), (32, 32)]
        formats = ['JPEG', 'PNG', 'GIF', 'ICO', 'BMP']
        
        for width, height in small_sizes:
            for format_name in formats:
                with self.subTest(size=(width, height), format=format_name):
                    # Skip ICO for sizes smaller than 16x16
                    if format_name == 'ICO' and (width < 16 or height < 16):
                        self.skipTest('ICO format does not support images smaller than 16x16')
                    jpg_path = self.create_test_image('jpg', size=(width, height))
                    output_path = os.path.join(self.test_dir, f"small_{width}x{height}.{format_name.lower()}")
                    
                    result = convert_image(jpg_path, output_path, format_name)
                    
                    self.assertTrue(result)
                    self.assertTrue(os.path.exists(output_path))
                    
                    with Image.open(output_path) as img:
                        if format_name != 'ICO':  # ICO has size restrictions
                            self.assertEqual(img.size, (width, height))
                        if format_name in ['JPEG', 'JPG']:
                            self.assertEqual(img.format, 'JPEG')
                        else:
                            self.assertEqual(img.format, format_name)
    
    def test_convert_with_edge_cases(self):
        """Test converting with edge case formats and scenarios."""
        # Test with empty format string
        jpg_path = self.create_test_image('jpg')
        output_path = os.path.join(self.test_dir, "output.png")
        
        result = convert_image(jpg_path, output_path, '')
        
        self.assertTrue(result)
        self.assertTrue(os.path.exists(output_path))
        
        with Image.open(output_path) as img:
            self.assertEqual(img.format, 'PNG')
        
        # Test with None format (should use default PNG)
        output_path2 = os.path.join(self.test_dir, "output2.png")
        result2 = convert_image(jpg_path, output_path2, None)
        
        self.assertTrue(result2)
        self.assertTrue(os.path.exists(output_path2))
        
        with Image.open(output_path2) as img:
            self.assertEqual(img.format, 'PNG')


if __name__ == '__main__':
    unittest.main() 