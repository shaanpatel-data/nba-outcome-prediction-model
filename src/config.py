"""
Configuration module for the NBA Outcome Prediction Model.

Loads environment variables and defines directory paths used by the project.
"""

import os
from pathlib import Path

# Load The Odds API key from environment variables
ODDS_API_KEY: str | None = os.getenv("ODDS_API_KEY")

# Project base directory (two levels up from this file)
BASE_DIR = Path(__file__).resolve().parents[2]

# Data directories
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
INTERIM_DATA_DIR = DATA_DIR / "interim"

# Add other configuration constants as needed
