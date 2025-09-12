# Trilingual Neural Weather Prediction Challenge

## 🌤️ Competition Overview

Welcome to the **Trilingual Neural Weather Prediction Challenge**! This competition focuses on building neural models capable of generating weather descriptions in three languages: **English**, **French**, and **German**. Participants will develop systems that can understand meteorological data and produce accurate, natural language weather forecasts across multiple languages.

## 🎯 Objective

Develop a neural model that:
- Takes meteorological input data (temperature, humidity, wind speed, etc.)
- Generates coherent weather descriptions in English, French, and German
- Produces probability distributions over predicted text (log probabilities)
- Maintains accuracy and fluency across all three languages

## 📊 Evaluation Metrics

Models will be evaluated on:
1. **Accuracy**: Exact match with ground truth weather descriptions
2. **Perplexity**: Quality of probability distributions (lower is better)
3. **Cross-lingual Consistency**: Semantic consistency across languages
4. **Fluency**: Natural language quality in each target language

## 📁 Repository Structure

```
trilingual-nwp-challenge-starter/
├── data/                    # Dataset storage
│   └── .gitkeep            # Keeps folder in git
├── scripts/                 # Utility scripts
│   ├── download_data.py     # Data download script
│   └── evaluate.py          # Evaluation script
├── predictions/             # Model predictions
│   └── example.logprobs.csv # Example submission format
├── requirements.txt         # Python dependencies
├── reproduce.sh            # Environment setup script
└── README.md               # This file
```

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/jiyad99-blip/trilingual-nwp-challenge-starter.git
cd trilingual-nwp-challenge-starter
```

### 2. Set Up Environment
```bash
# Make the setup script executable
chmod +x reproduce.sh

# Run the complete setup
./reproduce.sh
```

### 3. Manual Setup (Alternative)
```bash
# Create virtual environment
python -m venv trilingual-nwp-env
source trilingual-nwp-env/bin/activate  # On Windows: trilingual-nwp-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download spaCy models
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm
python -m spacy download de_core_news_sm
```

## 📈 Data Format

### Input Data
Dataset: https://drive.google.com/drive/folders/18tUmoFbUOdSzKhwNjeUWpH85BoQB3cBJ?usp=sharing

### Output Format
Submissions should be CSV files with the following columns:
```csv
id,english_text,english_logprob,french_text,french_logprob,german_text,german_logprob
1,"Partly cloudy with light winds",-2.3456,"Partiellement nuageux avec vents légers",-2.8901,"Teilweise bewölkt mit leichten Winden",-3.1234
```

## 🔧 Usage

### Download Competition Data
```bash
python scripts/download_data.py
```

### Evaluate Predictions
```bash
python scripts/evaluate.py \
    --predictions predictions/your_model.csv \
    --ground_truth data/test_ground_truth.json \
    --output results/evaluation.json
```

## 🏆 Submission Guidelines

1. **Format**: Submit predictions as CSV files following the example format
2. **Filename**: Use format `team_name_submission_v1.csv`
3. **Content**: Include weather descriptions and log probabilities for all three languages
4. **Validation**: Test your submission format using the provided evaluation script

## 🌍 Language-Specific Notes

### English
- Standard meteorological terminology
- Clear, concise descriptions
- American English preferred

### French
- European French conventions
- Proper accent marks required
- Meteorological terms in French

### German
- Standard German (Hochdeutsch)
- Compound words for weather phenomena
- Proper capitalization rules

## 📚 Resources

- [Competition Guidelines](https://example.com/guidelines)
- [Dataset Documentation](https://example.com/data-docs)
- [Baseline Models](https://example.com/baselines)
- [Discussion Forum](https://example.com/forum)

## 🛠️ Development Tips

1. **Start Simple**: Begin with a basic multilingual model
2. **Data Augmentation**: Use back-translation and paraphrasing
3. **Cross-lingual Training**: Leverage shared representations
4. **Evaluation**: Regularly test on validation data
5. **Ensemble Methods**: Combine multiple model predictions

## 📝 Example Model Pipeline

```python
# 1. Load meteorological data
data = load_weather_data('data/train.json')

# 2. Preprocess and encode
encoded_features = preprocess_weather_features(data)

# 3. Train multilingual model
model = TrilingualWeatherModel()
model.train(encoded_features, target_descriptions)

# 4. Generate predictions
predictions = model.predict(test_features)

# 5. Calculate log probabilities
logprobs = model.get_log_probabilities(predictions)

# 6. Format for submission
submission = format_predictions(predictions, logprobs)
```

## 🐛 Troubleshooting

### Common Issues
- **Memory errors**: Reduce batch size or use gradient checkpointing
- **Language model errors**: Ensure proper tokenization for each language
- **Evaluation errors**: Check CSV format and column names

### Getting Help
- Check the [FAQ](https://example.com/faq)
- Post in the [discussion forum](https://example.com/forum)
- Review example submissions in `predictions/`

## 📋 Requirements

- Python 3.8+
- PyTorch 1.10+
- Transformers 4.15+
- spaCy 3.2+ with language models
- See `requirements.txt` for complete list

## 🏅 Leaderboard

Submissions will be ranked by:
1. Overall accuracy (40%)
2. Average perplexity (30%)
3. Cross-lingual consistency (20%)
4. Language fluency (10%)

## 📞 Contact

For questions about this challenge:
- **Email**: trilingual-nwp@example.com
- **GitHub Issues**: [Create an issue](https://github.com/jiyad99-blip/trilingual-nwp-challenge-starter/issues)
- **Discussion**: [Competition Forum](https://example.com/forum)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Happy coding and good luck with the challenge! 🚀**
