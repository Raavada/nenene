print("Hello")
from docxtpl import DocxTemplate
import datetime


company_name = input("Enter name of the Company : ") 
position_name = input("Enter name of the Position: ")


today_date = datetime.datetime.today().strftime('%m/%d/%Y')

doc = DocxTemplate("cv.docx")
context = { 'today_date': today_date, 
           'company_name' : company_name, 
           'position_name' : position_name}

doc.render(context)

doc.save('Cover_letter_'+company_name+'_'+position_name+'.docx')