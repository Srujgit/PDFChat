import unstructured
import unstructured.documents
import unstructured.documents.elements
from unstructured.partition.pdf import partition_pdf
import os


def parse_contents(files):
    if isinstance(files, list):
        texts, images, tables = [], [], []
        for file in files:
            txts, imgs, tbls = _parse_content(file)
            texts.append(txts)
            images.append(imgs)
            tables.append(tbls)
    else:
        texts, images, tables = _parse_content(files)
    
    return texts, images, tables

def _parse_content(file):
    elements = partition_pdf(
    filename = file,                  
    strategy = "hi_res",                                     
    extract_images_in_pdf = True,                            
    extract_image_block_types = ["Image", "Table"],          
    extract_image_block_to_payload = True,             
    chunking_strategy="by_title",
    max_characters = 10000,
    combine_text_under_n_chars = 2000,
    new_after_n_chars = 6000
    )
    texts, images, tables = [], [], []
    for element in elements[:1000]:
        if "unstructured.documents.elements.CompositeElement" in str(type(element)):
            texts.append(element)
        elif "unstructured.documents.elements.Table" in str(type(element)):
            tables.append(element)
    



if __name__ == "__main__":
    filepath = "C:\\Users\\Srujan\\Btech\\PapersToRead\\AgentQ.pdf"
    _parse_content(filepath)
    
