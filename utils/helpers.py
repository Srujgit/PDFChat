from unstructured.partition.pdf import partition_pdf
## Enable these to display images/ tables
#import base64
#import io
#from PIL import Image
#import streamlit as st #To display tabels use streamlit run
import markdownify



def parse_contents(files):
    if isinstance(files, list):
        texts, images, tables = [], [], []
        for file in files:
            txts, imgs, tbls = _parse_contents(file)
            texts.append(txts)
            images.append(imgs)
            tables.append(tbls)
    else:
        texts, images, tables = _parse_contents(files)
    
    return texts, images, tables


def _parse_contents(file):
    elements = partition_pdf(
        filename = file,                  
        strategy = "hi_res", 
        infer_table_structure= True,
        extract_images_in_pdf = True,                            
        extract_image_block_types = ["Image",],          
        extract_image_block_to_payload = True,             
        chunking_strategy="by_title",
        max_characters = 10000,
        combine_text_under_n_chars = 2000,
        new_after_n_chars = 6000
    ) 
    
    texts, images, tables = [], [], []
    for element in elements:
        if "unstructured.documents.elements.CompositeElement" in str(type(element)):## Extracts all texts and appends to list
            texts.append(element.text)
            
            metadata = element.metadata.orig_elements## Metadata contains all images and tables

            for data in metadata:
                if "unstructured.documents.elements.Image" in str(type(data)): ## Appends all images to list in base64 encoding
                    images.append(data.metadata.image_base64) 

                if "unstructured.documents.elements.Table" in str(type(data)): ## Appends all tables in HTML encoding
                    tables.append(data.metadata.text_as_html)
    if len(tables)>0: 
        for i in range(len(tables)):
            tables[i] = _convert_html_to_markdown(tables[i])
    return texts, images, tables

def _convert_html_to_markdown(table): ## Convert tables to markdown for easier processing
    return markdownify.markdownify(table)


if __name__ == "__main__":
    filepath = "C:\\Users\\Srujan\\Btech\\PapersToRead\\Titans.pdf"
    texts, images, tables = parse_contents(filepath)

    #print(len(texts), len(images), len(tables))

    #for i in images:
    #    img = Image.open(io.BytesIO(base64.b64decode(i)))
    #    img.show()
    
    #st.markdown(tables[0], unsafe_allow_html=True)

    ##On windows use "chcp 65001" in the terminal before running the file
    #for i in texts:
        #print(i)
    ## Texts parsed in the hi_res mode are not decoded properly
    print(markdownify.markdownify(tables[0]))