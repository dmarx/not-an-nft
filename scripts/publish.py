from pathlib import Path

def get_new_images():
    pass

def add_images_to_gallery(img_paths):
    pass
  
def update_gallery():
    img_paths = get_new_images()
    add_images_to_gallery(img_paths)
    
if __name__ == '__main__':
    update_gallery()
