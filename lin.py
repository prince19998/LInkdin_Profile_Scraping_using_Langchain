import streamlit as st
from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_groq import ChatGroq
from langchain_community.utilities import GoogleSerperAPIWrapper, SerpAPIWrapper
import pandas as pd
import json
import os
from datetime import datetime
import time

# Set up directory
DATA_DIR = "linkedin_data"
os.makedirs(DATA_DIR, exist_ok=True)

# App UI
st.title("🔎 LinkedIn Profile Scraper (Bulk)")
st.write("Enter 100 to 200 names to fetch LinkedIn profile info using Groq + Serper/SerpAPI")

# Sidebar configs
groq_api_key = st.sidebar.text_input("🔐 Groq API Key", type="password")
search_api_key = st.sidebar.text_input("🔍 Search API Key", type="password")
search_api = st.sidebar.selectbox("Search API", ["Google Serper", "SerpAPI"])
model_name = st.sidebar.selectbox("Groq Model", ["llama3-70b-8192", "llama3-8b-8192", "mixtral-8x7b-32768"])

# Input
names_input = st.text_area("📋 Paste 100–200 names (one per line)", height=300)
names = [n.strip() for n in names_input.split("\n") if n.strip()]
name_count = len(names)
st.caption(f"✅ {name_count} names detected.")

# Validate input
if name_count > 200:
    st.error("⚠️ Limit is 200 names max.")
elif name_count < 100:
    st.warning("⚠️ Minimum 100 names required.")

# Set up Agent
def setup_agent(groq_key, search_key, api_choice, model):
    llm = ChatGroq(temperature=0.7, model_name=model, groq_api_key=groq_key)
    search_tool = GoogleSerperAPIWrapper(serper_api_key=search_key) if api_choice == "Google Serper" else SerpAPIWrapper(serpapi_api_key=search_key)
    tools = [Tool(name="Search", func=search_tool.run, description="Find LinkedIn profiles and public details")]
    return initialize_agent(tools, llm, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True, handle_parsing_errors=True, max_iterations=5)

# Profile Finder
def extract_profile(name, agent):
    prompt = f"""
    Find the LinkedIn profile for: {name}

    Extract in JSON format:
    {{
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
    }}
    Use "Not found" if unavailable.
    """
    try:
        result = agent.run(prompt)
        profile = json.loads(result) if isinstance(result, str) else result
        profile["search_timestamp"] = datetime.now().isoformat()
        profile["search_query"] = name
        return profile
    except Exception as e:
        return {"name": name, "error": str(e), "search_timestamp": datetime.now().isoformat(), "search_query": name}

# Save profiles
def save_bulk_data(profiles):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_file = os.path.join(DATA_DIR, f"linkedin_profiles_{timestamp}.json")
    csv_file = os.path.join(DATA_DIR, f"linkedin_profiles_{timestamp}.csv")

    with open(json_file, "w") as f:
        json.dump(profiles, f, indent=2)

    df = pd.DataFrame(profiles)
    df.to_csv(csv_file, index=False)

    return json_file, csv_file

# RUN
if st.button("🚀 Start Scraping (100–200 Profiles)"):
    if not (groq_api_key and search_api_key):
        st.error("🔑 Please enter both API keys.")
    elif 100 <= name_count <= 200:
        agent = setup_agent(groq_api_key, search_api_key, search_api, model_name)
        all_profiles = []

        progress = st.progress(0)
        status = st.empty()

        for i, name in enumerate(names):
            status.text(f"🔍 Searching {i+1}/{name_count}: {name}")
            profile = extract_profile(name, agent)
            all_profiles.append(profile)
            progress.progress((i + 1) / name_count)
            time.sleep(1)  # Respect rate limit

        progress.empty()
        status.success("✅ Done!")

        # Save results
        json_path, csv_path = save_bulk_data(all_profiles)

        st.success(f"📁 Data saved to `{DATA_DIR}`")
        with open(json_path, "r") as f:
            st.download_button("⬇️ Download JSON", f.read(), file_name=os.path.basename(json_path), mime="application/json")

        with open(csv_path, "rb") as f:
            st.download_button("⬇️ Download CSV", f, file_name=os.path.basename(csv_path), mime="text/csv")
    else:
        st.error("⚠️ Please input between 100 and 200 names.")

# Sidebar Info
st.sidebar.markdown("### 💾 Save Location")
st.sidebar.info(f"Saved in `{DATA_DIR}` directory.")

st.sidebar.markdown("### 🔧 Configuration")
st.sidebar.code(f"""
Model: {model_name}
Search: {search_api}
Names: {name_count}
""")
