# NBA Outcome Prediction Model

This repository contains a data-driven sports analytics project to predict NBA game outcomes, including team win probability, point spreads, and totals. The goal is to showcase modeling and data engineering skills for potential employers. It is not gambling advice; instead, it demonstrates a rigorous approach to building a predictive model using publicly available data.

## Project Structure

The project follows a clean and modular structure inspired by Cookiecutter Data Science:

```
├── data
│   ├── raw/              # Raw data dumps (not tracked in git)
│   ├── interim/          # Intermediate datasets during processing
│   └── processed/        # Final, cleaned datasets used for modeling
├── notebooks/            # Exploratory data analysis and project notebooks
├── reports/
│   └── figures/          # Generated graphics and plot outputs
├── src/                  # Source code for use in this project
│   ├── nba/              # NBA-specific data loading and feature engineering
│   ├── features/         # Feature engineering scripts
│   ├── models/           # Model training, scoring, and evaluation
│   ├── odds/             # Odds retrieval and processing
│   ├── viz/              # Visualization helpers
│   ├── config.py         # Central configuration (paths, parameters)
│   └── __init__.py
├── models/               # Serialized model objects and pipelines
├── tests/                # Unit tests to ensure correctness of critical functions
├── scripts/              # CLI scripts for reproducible runs (e.g. training, evaluation)
├── .env.example          # Template for environment variables (copy to .env)
├── .gitignore
├── LICENSE
└── README.md
```

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/shaanpatel-data/nba-outcome-prediction-model.git
   cd nba-outcome-prediction-model
   ```

2. **Set up a Python environment** and install requirements:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```

3. **Create a `.env` file** in the repository root based on `.env.example`. This file should include your API keys (e.g., `ODDS_API_KEY`) and other secrets. **Never commit your actual `.env` file.**

4. **Run the pipeline**:
   - Use scripts in the `scripts/` directory to download data, train models, and generate predictions.
   - For example:
     ```bash
     python scripts/download_games.py
     python scripts/build_team_ratings.py
     python scripts/train_model.py
     python scripts/evaluate_model.py
     ```

## Methodology

The NBA model uses a combination of ELO-based team ratings, offensive and defensive efficiencies, pace factors, and injury-adjusted lineup projections to simulate game outcomes. Key steps include:

- **Data Collection:** Historical NBA results, team statistics, and publicly available injury reports.
- **Feature Engineering:** Creation of rolling offensive/defensive metrics, pace adjustments, and home court advantage estimates.
- **Modeling:** Statistical simulations and probabilistic modeling (e.g., Monte Carlo) to generate win probabilities and expected point spreads.
- **Evaluation:** Backtesting the model on out-of-sample seasons to assess accuracy and calibration.

## Contributing

Contributions are welcome! Please open an issue to discuss improvements or submit a pull request for small changes. If you use this project as part of your portfolio, feel free to share your own modeling experiments and results.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
