#!/usr/bin/env python3
"""
Evaluation script for trilingual neural weather prediction challenge.

This script evaluates model predictions against ground truth for:
- English, French, and German weather descriptions
- Log probability scoring
- Multi-lingual accuracy metrics
"""

import argparse
import json
import csv
import math
from typing import Dict, List, Tuple
from pathlib import Path

def load_predictions(file_path: str) -> List[Dict]:
    """Load predictions from CSV file."""
    predictions = []
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            predictions.append(row)
    return predictions

def load_ground_truth(file_path: str) -> List[Dict]:
    """Load ground truth from JSON file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def calculate_perplexity(log_probs: List[float]) -> float:
    """Calculate perplexity from log probabilities."""
    if not log_probs:
        return float('inf')
    
    avg_log_prob = sum(log_probs) / len(log_probs)
    return math.exp(-avg_log_prob)

def calculate_accuracy(predictions: List[str], ground_truth: List[str]) -> float:
    """Calculate exact match accuracy."""
    if len(predictions) != len(ground_truth):
        raise ValueError("Predictions and ground truth must have same length")
    
    correct = sum(1 for pred, truth in zip(predictions, ground_truth) if pred.strip().lower() == truth.strip().lower())
    return correct / len(predictions)

def evaluate_language(pred_data: List[Dict], gt_data: List[Dict], language: str) -> Dict[str, float]:
    """Evaluate predictions for a specific language."""
    pred_texts = [item[f'{language}_text'] for item in pred_data if f'{language}_text' in item]
    pred_logprobs = [float(item[f'{language}_logprob']) for item in pred_data if f'{language}_logprob' in item]
    
    gt_texts = [item[f'{language}_text'] for item in gt_data if f'{language}_text' in item]
    
    # Calculate metrics
    accuracy = calculate_accuracy(pred_texts, gt_texts) if pred_texts and gt_texts else 0.0
    perplexity = calculate_perplexity(pred_logprobs) if pred_logprobs else float('inf')
    
    return {
        'accuracy': accuracy,
        'perplexity': perplexity,
        'num_samples': len(pred_texts)
    }

def main():
    parser = argparse.ArgumentParser(description='Evaluate trilingual weather predictions')
    parser.add_argument('--predictions', '-p', required=True, help='Path to predictions CSV file')
    parser.add_argument('--ground_truth', '-g', required=True, help='Path to ground truth JSON file')
    parser.add_argument('--output', '-o', help='Path to save evaluation results')
    
    args = parser.parse_args()
    
    # Load data
    print("Loading predictions...")
    predictions = load_predictions(args.predictions)
    
    print("Loading ground truth...")
    ground_truth = load_ground_truth(args.ground_truth)
    
    # Evaluate each language
    languages = ['english', 'french', 'german']
    results = {}
    
    for lang in languages:
        print(f"Evaluating {lang}...")
        lang_results = evaluate_language(predictions, ground_truth, lang)
        results[lang] = lang_results
        
        print(f"{lang.capitalize()} Results:")
        print(f"  Accuracy: {lang_results['accuracy']:.4f}")
        print(f"  Perplexity: {lang_results['perplexity']:.4f}")
        print(f"  Samples: {lang_results['num_samples']}")
        print()
    
    # Calculate overall metrics
    overall_accuracy = sum(results[lang]['accuracy'] for lang in languages) / len(languages)
    overall_perplexity = sum(results[lang]['perplexity'] for lang in languages) / len(languages)
    
    results['overall'] = {
        'accuracy': overall_accuracy,
        'perplexity': overall_perplexity
    }
    
    print("Overall Results:")
    print(f"  Average Accuracy: {overall_accuracy:.4f}")
    print(f"  Average Perplexity: {overall_perplexity:.4f}")
    
    # Save results if output path provided
    if args.output:
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"\nResults saved to {args.output}")

if __name__ == "__main__":
    main()
