import os
import requests
import ebooklib
from ebooklib import epub
import markdown

mds_path = os.path.curdir
# Create a new epub book
book = epub.EpubBook()

# Convert multiple markdown files to chapters
def convert_mds_to_chapters():
    # Loop through all markdown files in the folder
    md_files = enumerate(filter(lambda x: x.endswith('.md'), os.listdir(mds_path)))
    for i, md_file_name in md_files:
        f = os.path.join(mds_path, md_file_name)
        with open(f, 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()
        html_content = markdown.markdown(md_content)

        chapter_title = os.path.splitext(os.path.basename(md_file_name))[0]
        chapter = epub.EpubHtml(title=f'Chapter {i+1} {chapter_title}', 
                                file_name=f'chapter_{i+1}.xhtml')
        chapter.content = embed_images(html_content) if '<img' in html_content else html_content

        book.add_item(chapter) 
        # Add the chapter to the table of contents
        book.toc.append(epub.Link(chapter.file_name, chapter.title, chapter.id))

        # Add the chapter to the spine of the book
        book.spine.append(chapter)
    
# embed the images to book 
def embed_images(html):
    image_tags = html.split('<img')
    for i, image_tag in enumerate(image_tags[1:]):
        # Extract the image file name from the tag
        image_file_name = image_tag.split('src="')[1].split('"')[0]
        ext = os.path.splitext(image_file_name)[1]

        # Add the image file to the chapter
        if image_file_name.startswith('http'):
            image_content = requests.get(image_file_name).content
        # reference the local image file embed in ebook
        else:
            image_path = os.path.join(mds_path, image_file_name)
            image_content = open(image_path, 'rb').read()

        image_item = epub.EpubImage(media_type='image/jpeg', content=image_content)
        book.add_item(image_item)

        image_item.file_name = f"{image_item.id}{ext}"
        image_tags[i+1] = image_tag.replace(image_file_name, image_item.file_name)

    return '<img'.join(image_tags)
        
# Convert multiple markdown files to a single epub book
def convert_mds_to_epub(input_dir, out_file):
    global mds_path 
    mds_path = input_dir
    epub_file = out_file

    # Set the title of the book
    book.set_title(os.path.splitext(os.path.basename(epub_file))[0])
    book.set_language('zh')
    # Add a table of contents
    book.toc = []

    convert_mds_to_chapters()

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    if os.path.exists(epub_file):
        os.remove(epub_file)
    
    # Save the book to the epub file
    epub.write_epub(epub_file, book, {})

if __name__ == "__main__":
    convert_mds_to_epub(r"E:/workspace/ebooks/notes", '伯克希尔股东大会笔记.epub')