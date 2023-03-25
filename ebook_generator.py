import os, urllib.request
import ebooklib
from ebooklib import epub
import markdown


# Convert multiple markdown files to a single epub book
def convert_multiple_md_to_epub(md_folder_path, epub_file_path):
    # Create a new epub book
    book = epub.EpubBook()

    # Set the title of the book
    book.set_title(os.path.splitext(os.path.basename(epub_file_path))[0])
    book.set_language('zh')

    # Add a table of contents
    book.toc = ()

    # Loop through all markdown files in the folder
    md_files = enumerate(filter(lambda x: x.endswith('.md'), os.listdir(md_folder_path)))
    for i, md_file_name in md_files:
        # Read the markdown file
        with open(os.path.join(md_folder_path, md_file_name), 'r', encoding='utf-8') as md_file:
            md_content = md_file.read()

        # Convert markdown to html
        html_content = markdown.markdown(md_content)

        # Add a new chapter to the book
        chapter_name = os.path.splitext(os.path.basename(md_file_name))[0]
        chapter = epub.EpubHtml(title=f'Chapter {i+1}', file_name=f'chapter_{i+1}.xhtml', lang='zh')
        chapter.content = html_content
            
        # Add all image tags in the HTML content to the chapter
        image_tags = chapter.content.split('<img')
        for j, image_tag in enumerate(image_tags[1:]):
            # Extract the image file name from the tag
            image_file_name = image_tag.split('src="')[1].split('"')[0]
            image_base_name = os.path.basename(image_file_name)

            # Add the image file to the chapter
            if image_file_name.startswith('http'):
                image_content = urllib.request.urlopen(image_file_name).read()
                # reference the local image file embed in ebook
                chapter.content = chapter.content.replace(image_file_name, image_base_name)
            else:
                image_path = os.path.join(md_folder_path, image_file_name)
                image_content = open(image_path, 'rb').read()

            image_id = f'image_{i+1}_{j+1}'
            image_item = epub.EpubImage(uid=image_id, file_name=image_base_name,
                                        media_type='image/jpeg',
                                        content=image_content)
            book.add_item(image_item)
            # chapter.content += '<br/><img src="{}"/>'.format(image_base_name)

        book.add_item(chapter)

        # Add the chapter to the table of contents
        book.toc += (epub.Link(f'chapter_{i+1}.xhtml', f'Chapter {i+1} {chapter_name}', f'chapter_{i+1}'),)

        # Add the chapter to the spine of the book
        book.spine.append(chapter)

    # Add a table of contents file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    if os.path.exists(epub_file_path):
        os.remove(epub_file_path)
    
    # Save the book to the epub file
    epub.write_epub(epub_file_path, book, {})

convert_multiple_md_to_epub(r"E:/workspace/ebooks/notes", '伯克希尔股东大会笔记.epub')
# convert_multiple_md_to_epub(r"..\ebooks", 'hello3.epub')
# convert_multiple_md_to_epub(f".", 'test.epub')