🔎 LinkedIn Profile Scraper (Bulk)
Scrape 100–200 LinkedIn profiles in one go using Groq LLMs and Serper/SerpAPI via LangChain. This Streamlit app automates LinkedIn profile extraction and saves data in JSON and CSV formats.
![Single Name Profile Scrap] (https://github.com/user-attachments/assets/a5a5a64a-8d6e-4f08-995f-9375a93daf21)
![Multiple Name Profile Scrape] (https://github.com/user-attachments/assets/f6fe120a-bacf-4d1d-b57f-8bdd1a38e94b)



🚀 Features
✅ Paste 100–200+ names and get full LinkedIn profile details

🤖 Uses Groq’s LLMs via LangChain for structured JSON output

🔍 Choose between Serper or SerpAPI as the search engine

📁 Outputs saved as downloadable JSON & CSV files

🧠 Extracts: name, position, company, experience, education, skills, location, summary, LinkedIn URL

📸 Demo
![Demo](https://github.com/user-attachments/assets/abb83809-acfa-4c39-a79f-5babb838fccc)


📦 Installation
1. Clone the Repository

git clone https://github.com/your-username/linkedin-bulk-scraper.git
cd linkedin-bulk-scraper
2. Create Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies

pip install -r requirements.txt
Note: If you don’t have a requirements.txt, generate one:


pip freeze > requirements.txt
🔐 Required API Keys
You need two API keys:

Groq API Key → Get it here

Serper or SerpAPI Key

Serper API Key

SerpAPI Key

🧾 How to Use
Run the app:


streamlit run app.py
In the sidebar, fill in:

Groq API Key

Serper/SerpAPI Key

Choose your preferred model and search API

Paste 100 to 200+ names, one per line

Click 🚀 Start Scraping and wait for results

Download your output as .json or .csv

🧠 Output Format (Example)


{
  "name": "John Doe",
  "current_position": "Software Engineer at Google",
  "current_company": "Google",
  "previous_experience": ["Software Engineer at Meta", "Intern at IBM"],
  "education": ["B.Sc. - MIT", "M.Sc. - Stanford"],
  "skills": ["Python", "AI", "Cloud"],
  "location": "San Francisco, CA",
  "summary": "Experienced developer with a passion for AI...",
  "profile_url": "https://www.linkedin.com/in/johndoe",
  "search_timestamp": "2025-04-07T12:00:00Z",
  "search_query": "John Doe"
}
📂 Output Directory
All outputs are saved in the linkedin_data/ folder:

linkedin_profiles_YYYYMMDD_HHMMSS.json

linkedin_profiles_YYYYMMDD_HHMMSS.csv

⚠️ Notes
⛔️ Limit: 100–200 names per run

⏱ Adds delay between requests to avoid rate-limiting

🧹 If a profile isn't found, fields will return "Not found"

🛑 If an error occurs, it's saved in an "error" field

💡 Troubleshooting
Problem	Solution
API key invalid	Double-check your keys and usage quota
App stuck during run	Reduce input size or switch search provider
Empty profiles	Some profiles may not be indexed or public
Decoding error	Try again—sometimes LLMs return non-JSON content
🙌 Contributing
Feel free to submit PRs or open issues for enhancements, bugs, or feature requests!

📜 License
MIT License © 2025 Your Name



