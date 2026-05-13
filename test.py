import google.generativeai as genai

genai.configure(api_key="AIzaSyBfx-1SsEflc-9vR4z01OawipJmpITQjYs")

for m in genai.list_models():
    print(m.name, m.supported_generation_methods)