import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list
        print(pdf)
        merger.append(pdf)
    merger.write('super.pdf')


pdf_merger(inputs)


# with open('dummy.pdf', 'rb') as file:
#     reader = PyPDF2.PdfReader(file)
#     page = reader.pages[0]
#     page.rotate(270)
#     writer = PyPDF2.PdfWriter()
#     writer.add_page(page)
#     with open('tilt.pdf', 'wb') as new_file:
#         writer.write(new_file)

