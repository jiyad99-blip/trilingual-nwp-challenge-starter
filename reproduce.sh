#!/bin/bash

# Trilingual Neural Weather Prediction Challenge - Reproduction Script
# This script sets up the environment and reproduces the baseline results

set -e  # Exit on any error

echo "Setting up Trilingual NWP Challenge environment..."

# Create and activate virtual environment
echo "Creating virtual environment..."
python -m venv trilingual-nwp-env
source trilingual-nwp-env/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing requirements..."
pip install -r requirements.txt

# Download language models for spaCy
echo "Downloading spaCy language models..."
python -m spacy download en_core_web_sm
python -m spacy download fr_core_news_sm
python -m spacy download de_core_news_sm

# Create necessary directories
echo "Creating directories..."
mkdir -p logs
mkdir -p models
mkdir -p results

# Download competition data
echo "Downloading competition data..."
python scripts/download_data.py

# Run baseline model (placeholder)
echo "Running baseline model..."
# TODO: Add baseline model training command here
# python scripts/train_baseline.py --config config/baseline.yaml

# Generate sample predictions
echo "Generating sample predictions..."
# TODO: Add prediction generation command here
# python scripts/generate_predictions.py --model models/baseline.pt --output predictions/baseline.csv

# Evaluate predictions
echo "Evaluating predictions..."
python scripts/evaluate.py \
    --predictions predictions/example.logprobs.csv \
    --ground_truth data/test_ground_truth.json \
    --output results/evaluation_results.json

echo "Evaluation complete! Results saved to results/evaluation_results.json"
echo "\nTo reproduce the full pipeline:"
echo "1. Ensure you have Python 3.8+ installed"
echo "2. Run: chmod +x reproduce.sh"
echo "3. Run: ./reproduce.sh"
echo "\nFor more information, see README.md"

echo "\nSetup complete! Virtual environment activated."
echo "To deactivate the environment, run: deactivate"
