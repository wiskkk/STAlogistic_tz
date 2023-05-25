import os
import PyPDF2
import json


def write_pack(pack_num, pack_files, pdf_writer):
    with open(f'pack_{pack_num}.pdf', 'wb') as output:
        pdf_writer.write(output)
    result[f'pack_{pack_num}'] = pack_files


folder_path = 'pdf_example'
max_size = 100 * 1024  # 100 KB in bytes
pack_num = 1
pack_size = 0
pack_files = []
result = {}
pdf_writer = PyPDF2.PdfWriter()

for filename in sorted(os.listdir(folder_path)):
    if filename.endswith('.pdf'):
        file_path = os.path.join(folder_path, filename)
        file_size = os.path.getsize(file_path)
        if pack_size + file_size > max_size:
            write_pack(pack_num, pack_files, pdf_writer)
            pack_num += 1
            pack_size = 0
            pack_files = []
            pdf_writer = PyPDF2.PdfWriter()
        pack_files.append(filename)
        pack_size += file_size

        with open(file_path, 'rb') as f:
            pdf_reader = PyPDF2.PdfReader(f)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

if pack_files:
    write_pack(pack_num, pack_files, pdf_writer)

with open('result.json', 'w') as f:
    json.dump(result, f, indent=4)
