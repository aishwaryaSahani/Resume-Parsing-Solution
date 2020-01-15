import glob
import csv
import re
# import PyPDF4 as PyPDF
import docx
import ExtractFunctions as ef

# THIS METHOD PERFORMS TOKENIZATION OF TEXT
def get_tokens(doc):
    tokens = re.split(r"[^A-Za-z0-9']", doc)
    tokens = list(filter(len, tokens))
    return tokens

# THE PURPOSE OF THIS METHOD IS TO CONVERT DOCUMENT INTO PLAINTEXT. ALONG WITH THE PLAINTEXT, THIS METHOD ALSO IDENTIFIES THE NUMEROUS SECTIONS AND THEIR INDEX.
def convert_docx_to_txt(path):
    
#    python-docx library has been used to convert the document into plaintext. This is performed paragraph by paragraphs 
    doc = docx.Document(path)
    fullText = []
    boldSections = []
    index = set()
    count = -1
#     we also keep track of index along with the sections
    for para in doc.paragraphs: 
        count +=1
        if(para.text!=""):
            fullText.append(para.text)
            tokenize = get_tokens(para.text)
#             numerous features can be used, sentences in the doc with less than 2 words can be identified as the headers, apart from that capital letters or bolds can also be identified
            if len(tokenize)<3 and len(tokenize)>0:
                boldSections.append(para.text)
                index.add(count)
                continue
            bold = []
            for run in para.runs:
    #             tokenize = para.text.split(" ")
                if run.bold and len(tokenize)<3 and run.text!="":
                    if run.text.strip() !="" and run.text not in ['\n', '\t'] :
                        bold.append(run.text)
                        index.add(count)
        
            if(bold != []):
                boldSections.append((bold))
#     while '' in boldSections:
#         boldSections.remove('')
#     boldSections = [item for item in boldSections if item not in ['\n', '\t']]

    return '\n'.join(fullText), (boldSections), list(sorted(index))

def main():
#     Writing a train method for semi supervised training
#     train()
    
#     Creating a csv file as output with all the desired rows
    with open('parsed_CV.csv', mode='w') as file:
        file = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow(["Name","Email","Phone","Skills","Education","Experience"])
        
#         Input FOlder which consists of all resumes to be parsed
        path = "InputFolder/"
#         Finding all docs 
        mylist = [f for f in glob.glob(path+"*.docx")]
        for resume in mylist:
            plainText, sections, index = convert_docx_to_txt(resume)    #converting doc into plaintext along with sections
            for sec in range(len(sections)):
                sections[sec] = re.sub('\W+',' ', sections[sec]).strip()
            print(sections)
#             print(index)
#             ef.namedEntityRecognition(plainText)

#             Calling methods to extract different entities 

            name = ef.extractPersonName(plainText)
#             print("Name :"+name)
            email = ef.extractEmailId(plainText)
#             print("Email:"+email)
            phone = ef.extractMobileNumber(plainText)
#             print("Phone:"+phone)

#             Finding the sections corresponding to the entity

            skillText = (ef.findSection(resume,"Skills",index, sections))
            skills = list(ef.extractSkills(skillText))
        #     print("Skills:"+skills)
            eduText = (ef.findSection(resume,"Education",index, sections))
            if eduText =="":
                eduText = plainText
            edu =ef.extractEducation(eduText)
#             print("Education:"+ef.extractEducation(eduText))
            expText = (ef.findSection(resume,"Experience",index, sections))
            exp = ef.extractExperience(expText)
#             print("Experience:"+ef.extractExperience(expText))
             
#             Writing the output in csv
            file.writerow([name, email, phone, skills, edu, exp])
     
#     Displaying the output
    with open('parsed_CV.csv', 'r') as csvfile:
        file = csv.reader(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in file:
            print(', '.join(row))
    
# THIS train() METHOD WAS USED TO GENERATE SECTIONAL HEADING. THE METHOD WOULD TAKE THE PATH AS INPUT, CALL THE  convert_docx_to_txt() METHOD TO GENERATE SECTIONS. 
# THIS SECTIONS WERE MANUALLY ADDED TO THE RULES TO DEFINE THE SIMILAR WORDS FOR EACH SECTION.
# THIS WORD WERE MANUALLY ADDED TO THE LABELS
 
def train():
    path = "Train/"
    mylist = [f for f in glob.glob(path+"*.docx")]
    for resume in mylist:
#         print(resume)
        plainText, sections, index = convert_docx_to_txt(resume)
        for sec in range(len(sections)):
            sections[sec] = re.sub('\W+',' ', sections[sec]).strip()
        print(sections)
        
        
if __name__ == '__main__':
    main()