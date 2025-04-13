from transformers import pipeline
from transformers import AutoTokenizer

class AbstractiveSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.max_input_tokens = self.tokenizer.model_max_length

    def split_text_into_chunks(self, text, max_tokens):
        words = text.split()
        chunks = []
        current_chunk = []

        for word in words:
            current_chunk.append(word)
            tokenized = self.tokenizer(" ".join(current_chunk), return_tensors="pt", truncation=False)
            if tokenized.input_ids.shape[1] > max_tokens:
                current_chunk.pop()
                chunks.append(" ".join(current_chunk))
                current_chunk = [word]

        if current_chunk:
            chunks.append(" ".join(current_chunk))

        return chunks

    def summarize(self, text, max_length=130, min_length=30):
        chunks = self.split_text_into_chunks(text, self.max_input_tokens)

        summaries = []
        for chunk in chunks:
            try:
                summary = self.summarizer(chunk, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
                summaries.append(summary)
            except Exception as e:
                print(f"[Error summarizing chunk]: {e}")
                continue

        return " ".join(summaries)