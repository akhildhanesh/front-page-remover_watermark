from PyPDF4 import PdfFileWriter, PdfFileReader, pdf 
import PyPDF4 
import sys
  

def put_watermark(input_pdf, output_pdf, watermark, fp): 
    PyPDF4.PdfFileReader(inp_file) 

    if remove:
        watermark_instance = PdfFileReader('static/remover.pdf')
    else:
        watermark_instance = PdfFileReader(watermark)
    first_page = PdfFileReader(fp) 
      
    watermark_page = watermark_instance.getPage(0) 

    pdf_reader = PdfFileReader(input_pdf) 
       
    pdf_writer = PdfFileWriter() 
  
    for page in range(first_page.getNumPages()):
        front_page = first_page.getPage(page)
        pdf_writer.addPage(front_page)


    for page in range(pdf_reader.getNumPages()): 
        if remove:
            if page == 0:
                continue
        page = pdf_reader.getPage(page) 
        page.mergePage(watermark_page)  
        pdf_writer.addPage(page) 
    

    out_file = 'output/' + output_pdf
    try:
        with open(out_file, 'wb') as out: 
            pdf_writer.write(out) 
    except:
        print('error occured during file creation')
    else:
        print('pdf file generated with name', output_pdf)

if __name__ == "__main__": 

    file = 'static/water.pdf'
    front_page = 'static/front_page.pdf'

    pdf_format = sys.argv[1]
    pdf_format = pdf_format.split('.')
    
    if pdf_format[-1] == 'pdf':
        inp_file = sys.argv[1]
        o_file = sys.argv[1]
    else:
        inp_file = sys.argv[1] + '.pdf'
        o_file = sys.argv[1] + '.pdf'
    
    try:
        if sys.argv[2] == 'remove' or bool(sys.argv[2]) == True:
            remove = True
    except:
        remove = False

    try:
        put_watermark(input_pdf = inp_file,
                    output_pdf = o_file,
                    watermark =  file,
                    fp = front_page) 
    except FileNotFoundError as e:
        print(e)
    except:
        print('error')