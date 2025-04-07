# 🔎 LinkedIn Profile Scraper (Bulk)
## Streamlit App
## LangChain
## Groq

A bulk LinkedIn profile scraper that processes 100-200 names at once using Groq's LLM and search APIs (Google Serper or SerpAPI).

## Features
Bulk Processing: Scrape 100-200 LinkedIn profiles in one run

Multiple APIs: Choose between Google Serper or SerpAPI for search

Groq Integration: Fast LLM processing with Groq's API (Llama 3 or Mixtral models)

Structured Output: Returns clean JSON data with profile details

Export Options: Download results as JSON or CSV

Progress Tracking: Real-time progress bar and status updates

## Installation
1.Clone the repository:
git clone https://github.com/yourusername/linkedin-profile-scraper.git
cd linkedin-profile-scraper

2.Install dependencies:
pip install -r requirements.txt

## Configuration
   You'll need API keys for:
    1.Groq
    2.Either Google Serper or SerpAPI

## Usage
## 1.Run the Streamlit app:
  streamlit run app.py

## 2.In the sidebar:
   Enter your Groq API key
   Enter your search API key (Serper or SerpAPI)
   Select your preferred Groq model
   Choose your search API provider

## 3.In the main panel:
   Paste 100-200 names (one per line)
   Click "Start Scraping"
   Wait for completion (takes several minutes)
   Download results as JSON or CSV  

## Output Format
Each profile includes:

{
    "name": "full name",
    "current_position": "title at company",
    "current_company": "company name",
    "previous_experience": ["list of previous positions"],
    "education": ["list of education items"],
    "skills": ["list of skills"],
    "location": "location",
    "summary": "profile summary",
    "profile_url": "URL if found",
    "search_timestamp": "timestamp",
    "search_query": "original search query"
}


## Rate Limits
The app includes a 1-second delay between requests to respect API rate limits. For large batches (200 names), expect the process to take ~3-4 minutes.

## Data Storage
All results are saved in the linkedin_data/ directory with timestamped filenames.

## Requirements
Python 3.8+

See requirements.txt for dependencies

## Disclaimer
This tool is for educational purposes only. Use in compliance with LinkedIn's Terms of Service and applicable laws. The developers are not responsible for misuse.

## License
MIT License
