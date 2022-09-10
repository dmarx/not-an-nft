from pathlib import Path

CONTENT_ROOT = 'content'
WEB_ROOT = 'gallery'

def get_images():
    #return list(Path(CONTENT_ROOT).glob('**/*.png'))
    return list(Path(CONTENT_ROOT).rglob('*.png'))

def get_new_images():
    content_page_fpath = Path(WEB_ROOT) / 'images.md'
    images = get_images()
    new_imgs = []
    if not content_page_fpath.exists():
        new_imgs = images
    else:
        with open(content_page_fpath, 'r') as f:
            page = f.read()
        for im in images:
            if not str(im) in page:
                new_imgs.append(im)
    return new_imgs
    
def impath2entry(im):
    return f"![](../{im})"


def add_images_to_gallery(new_images):
    ###
    # this is just temporary
    new_images = get_images()
    ###
    entries = ["# Images\n"] + [impath2entry(im) for im in new_images]
    content_page_fpath = Path(WEB_ROOT) / 'images.md'
    #with open(content_page_fpath, 'a') as f: 
    # this is also temporary
    with open(content_page_fpath, 'w') as f:
        f.write('  \n'.join(entries))

def update_gallery():
    img_paths = get_new_images()
    add_images_to_gallery(img_paths)
    
if __name__ == '__main__':
    update_gallery()
