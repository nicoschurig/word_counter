import os
import re
import PyPDF2
import matplotlib.pyplot as plt

#Path to .txt file with predefined words
wordlist_file = 'words.txt'

#Function that counts the number of words in a PDF file
def count_words_in_pdf(pdf_path, word_counts):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            page_text = page.extract_text()
            for word in defined_words:
                word = word.lower()
                count = len(re.findall(r'\b' + re.escape(word) + r'\b', page_text.lower()))
                word_counts[word].append(count)

#Reading predefined words from the .txt file
defined_words = []
with open(wordlist_file, 'r') as wordlist:
    defined_words = [word.strip() for word in wordlist.readlines()]
    print(defined_words)

#Directory path, containing the PDF files
pdf_folder = 'PDF_Files/Thorax'

word_counts = {word: [] for word in defined_words}
pdf_count = 0


#work through each PDF file and count the words
for pdf_filename in os.listdir(pdf_folder):
    if pdf_filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_folder, pdf_filename)
        count_words_in_pdf(pdf_path, word_counts)
        pdf_count += 1

#Calculating the mean number of references
word_avg_counts = {word: sum(counts) / pdf_count for word, counts in word_counts.items()}

#Removing words with an absolute number of references of 0
word_counts = {word: counts for word, counts in word_counts.items() if sum(counts) > 0}
word_avg_counts = {word: avg_count for word, avg_count in word_avg_counts.items() if word in word_counts}

#Generating graph
plt.figure(figsize=(10, 6))
plt.bar(word_counts.keys(), [sum(counts) for counts in word_counts.values()], label='Absolute Anzahl')
plt.bar(word_avg_counts.keys(), word_avg_counts.values(), label='Mittelwert')
plt.xlabel('analysierte Wörter', fontsize=20)
plt.ylabel('Anzahl an Erwähnungen', fontsize=20)
plt.xticks(rotation=45, fontsize=15)
plt.yticks(fontsize=10)
plt.legend(fontsize=15)
plt.tight_layout()

#Saving path as .jpg file
plt.savefig('word_counts.jpg')

#Show graph
plt.show()