import google.generativeai as genai

# Paste your API key here (or load from .env)
genai.configure(api_key="AIzaSyDR2p72-5KmLU_eX0e0NDaPmosW2biYFjU")

try:
    model = genai.GenerativeModel("models/gemini-flash-latest")
    response = model.generate_content("Say hello in one short sentence.")

    print("✅ API Key Working!")
    print("Response:", response.text)

except Exception as e:
    print("❌ API Key Error")
    print(e)
