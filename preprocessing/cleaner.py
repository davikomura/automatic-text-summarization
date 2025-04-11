import re

class TextCleaner:
    def clean(self, text: str) -> str:

        text = re.sub(r'https?://\S+', '', text)

        text = re.sub(r'\s+', ' ', text).strip()

        text = text.encode('ascii', 'ignore').decode()

        text = re.sub(r'([?.!])\1+', r'\1', text)

        text = text.replace('"', "'")  

        return text