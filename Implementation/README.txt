The Folder has a resume parser which parses all the docx formatted resumes ina  folder. The input folder is InputFolder. Please your docx formmated resumes in the InputFolder. Run the InputFileReader file. It will generate a csv named parsed_CV which will have extracted information.
The other files are extractFucntions which has the extraction methods for numerous entities.
There are 3 lists for pattern matching viz. majors-list for majors, job-phrase-list for job positions, all_linked_skills for skillset. The test cases folder consists of test cases for various entities.
The train folder consists of different documents which were used for semi supervised training. The folder also contains a Labels list which consists of different similar sectional names from SKills, Education and Expirience to assist in matching.
The folders contain sample resumes and personal resumes which i found over the internet. The lack of availability of categorized dataset resulted in manually downloading resumes from various sources.

External libraries used:
spacy
docx
re
csv
glob
PyPDF4

Dataset:
LinkedIn Skills Dataset: https://gist.github.com/bragboy/89777a2eacb8ca46d2c13e44bf928b7e
Position List Dataset: https://github.com/microsoft/LUIS-Samples/blob/master/documentation-samples/tutorials/job-phrase-list.csv
Majors List Dataset: https://github.com/fivethirtyeight/data/blob/master/college-majors/majors-list.csv

Steps to run:
1. Copy the implementation folder.
2. Put all your resumes in docx format in the InputFolder
3. Run the InputFileReader.py file
4. Check the Implementation folder for parsed_CV.csv where the columns represent the numerous entities viz. Name, Phone, Email, Skills, Education and Experience.
5. The rows correspond to numerous resumes.
6. Resume data will be extracted in each cell.
7. This csv can be used for further applications.
