from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# 1. Upload the SEPARATE file to the API
print("Uploading file...")
suspicious_file = genai.upload_file(path="/workspaces/CS4CS/AI Cybersecurity Research Project/suspicious_script.py")
suspicious_file_2 = genai.upload_file(path="/workspaces/CS4CS/AI Cybersecurity Research Project/suspicious_script_2.txt")

# 2. Create the prompt, including the file
prompt = [
    "You are a malware analysis expert. Analyze this Python script for any malicious behavior or security risks.",
    "Explain your findings, pointing out specific lines or code patterns that are suspicious. Conclude with a clear verdict: 'MALICIOUS' or 'BENIGN'.",
    suspicious_file,
]

# Use the model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

print("Generating analysis...")
response = model.generate_content(prompt)
print("--- ANALYSIS COMPLETE ---")
print(response.text)