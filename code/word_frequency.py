from collections import Counter
from pathlib import Path
import csv
import re


def load_text(file_path: Path) -> str:
    """Load text from a file and return it as lowercase."""
    return file_path.read_text(encoding="utf-8").lower()


def clean_text(text: str) -> list[str]:
    """
    Clean the text by keeping only letters and spaces,
    then split it into individual words.
    """
    cleaned = re.sub(r"[^a-z\s]", " ", text)
    return cleaned.split()


def count_terms(words: list[str], terms: list[str]) -> dict[str, int]:
    """Count how many times each target term appears in the text."""
    word_counts = Counter(words)
    return {term: word_counts[term] for term in terms}


def save_to_csv(results: dict[str, int], output_path: Path) -> None:
    """Save the term counts to a CSV file."""
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["term", "count"])

        for term, count in results.items():
            writer.writerow([term, count])


def main() -> None:
    # Define file paths
    input_path = Path("data/holocaust_museum_text.txt")
    output_path = Path("analysis/frequency_table.csv")

    # Define target terms for analysis
    terms = [
        "nazi",
        "hitler",
        "regime",
        "german",
        "state",
        "genocide",
        "atrocity",
        "crime",
        "violence",
        "persecution",
        "memory",
        "humanity",
        "victims",
        "lesson",
        "responsibility",
    ]

    # Load, clean, and analyze text
    text = load_text(input_path)
    words = clean_text(text)
    results = count_terms(words, terms)

    # Save results
    save_to_csv(results, output_path)

    print(f"Analysis complete. Results saved to: {output_path}")


if __name__ == "__main__":
    main()
