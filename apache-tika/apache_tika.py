import requests

# URL of your Tika server
TIKA_URL = 'http://localhost:9998/tika'
# Path to your PDF file
pdf_file_path = 'privacy_policy_v2.pdf'

headers = {
    'Accept': 'text/plain',
    'Content-Type': 'application/pdf'
}

with open(pdf_file_path, 'rb') as file:
    response = requests.put(TIKA_URL, headers=headers, data=file)

# The extracted text content from the PDF
print(response.text)

# Path to the output text file
output_file_path = 'output.txt'

# Write the extracted text content to the output file
with open(output_file_path, 'w') as output_file:
    output_file.write(response.text)
