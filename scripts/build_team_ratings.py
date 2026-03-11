"""
Script to build NBA team ratings based on historical results.

This module reads game results from the processed data directory,
computes offensive and defensive ratings with an exponential
decay factor for recency, and outputs updated team ratings to
 a CSV file in the processed data directory.

Usage:
    python scripts/build_team_ratings.py

The script will require the ODDS_API_KEY in a .env file for any
external data calls. Do not commit your API key to version control.
"""

# TODO: Implement the build_team_ratings functionality.


def main():
    """Entry point for building team ratings."""
    pass


if __name__ == "__main__":
    main()
