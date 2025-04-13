# Automatic Text Summarization

This repository contains a project for automatic text summarization using natural language processing (NLP) techniques.

## Features

- Extraction of texts directly from the news website [BBC News - Latin America](https://www.bbc.com/news/world/latin_america) and saving them in a JSON file with the filename indicating the date and time of extraction.
- Cleaning and tokenization of the extracted texts for data preparation.
- Summarization of texts in two formats:
    - **Extractive**: Selection of the most relevant sentences from the original text.
    - **Abstractive**: Generation of a summary using natural language with the help of the pre-trained **BART** model, creating sentences that are not necessarily in the original text.

## Technologies Used

- **NLTK**: Library for natural language processing.
- **Transformers**: Pre-trained models from Hugging Face.
- **BeautifulSoup**: Library for extracting data from HTML and XML files.
- **Requests**: Library for HTTP requests.

## How to Use

1. Clone the repository:
        ```bash
        git clone https://github.com/your-username/automatic-text-summarization.git
        ```
2. Install the dependencies:
        ```bash
        pip install -r requirements.txt
        ```
3. Run the main script:
        ```bash
        python main.py
        ```

## Project Structure

- `main.py`: Main file for running the project.
- `preprocessing/`: Auxiliary functions for text preprocessing.
- `scrapers/`: Scripts for extracting data from external sources.
- `summarization/`: Models and functions related to summarization.
- `data/`: Contains the data used in the project:
    - `raw/`: JSON data resulting from the scrapers.
    - `processed/`: Data resulting from preprocessing and summarization.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For questions or suggestions, contact via email: **davi.komura@gmail.com**.