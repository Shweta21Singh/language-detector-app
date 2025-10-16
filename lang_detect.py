from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

def detect_language(text):
    try:
        lang_code = detect(text)
        return lang_code
    except:
        return "Could not detect language."

if __name__ == "__main__":
    text = input("Enter text: ")
    language = detect_language(text)
    print(f"Detected language code: {language}")
