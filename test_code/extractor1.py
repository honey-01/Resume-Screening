import io
import docx2txt
import io
import docx2txt
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import LAParams




def extract_text_from_doc(doc_path):
	temp = docx2txt.process(doc_path)
	text = [line.replace('\t', ' ') for line in temp.split('\n') if line]
	return ' '.join(text)

def extract_text_from_pdf(pdf_path):
	with open(pdf_path, 'rb') as fh:
		for page in PDFPage.get_pages(fh, caching=True,check_extractable=True):
			resource_manager = PDFResourceManager()
			fake_file_handle = io.StringIO()
			converter = TextConverter(resource_manager, fake_file_handle, codec='utf-8', laparams=LAParams())
			page_interpreter = PDFPageInterpreter(resource_manager, converter)
			page_interpreter.process_page(page)
			text = fake_file_handle.getvalue()
			yield text
			# close open handles
			converter.close()
			fake_file_handle.close()

def extract_text(file_path, extension='.pdf'):
	text = ''
	if extension == '.pdf':
		for page in extract_text_from_pdf(file_path):
			text += ' ' + page
	elif extension == '.docx' or extension == '.doc':
		text = extract_text_from_doc(file_path)
	return text
