import PyPDF2
with open("c:/Users/sadad/Desktop/Python-Basics/Projects/Working_with_PDFs/Git_Summary.pdf", "rb") as first_file:
    reader = PyPDF2.PdfReader(first_file)
    page = reader.pages[0]
    page.rotate(90)
    # we just have this file in memory so
    # we need to write it to a new file

    writer = PyPDF2.PdfWriter()
    writer.add_page(page)
    with open("Rotated.pdf", "wb") as new_file:
        writer.write(new_file)
#################################################################

# merging two pdf files

    with open("c:/Users/sadad/Desktop/Python-Basics/Projects/Working_with_PDFs/Git_Summary.pdf", "rb") as second_file:
        merger = PyPDF2.PdfMerger()
        file_names = [first_file, second_file]
        for file_name in file_names:
            merger.append(file_name)
        with open("Combined.pdf", "wb") as merged_file:
            merger.write(merged_file)
