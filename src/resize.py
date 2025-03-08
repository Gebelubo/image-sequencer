from PIL import Image

def find_smallest_image(image_paths):
    smallest_image = None
    smallest_size = None

    for image_path in image_paths:
        if image_path:
            with Image.open(image_path) as img:
                size = img.size  
                
                if smallest_size is None or (size[0] * size[1] < smallest_size[0] * smallest_size[1]):
                    smallest_size = size
                    smallest_image = image_path

    return smallest_image, smallest_size

def resize_images_to_smallest(image_paths):
    smallest_image, smallest_size = find_smallest_image(image_paths)
    
    if smallest_image is None:
        return
    
    for image_path in image_paths:
        if image_path != smallest_image:
            with Image.open(image_path) as img:
                img = img.resize(smallest_size)  
                img.save(image_path) 



