from typing import Dict, List, Set, Tuple


survey_response: List[str] = ["C#", "Python", "JavaScript", "Java", "C++", "Python", "C#", "JavaScript", "Python", "Java", "C#", "C++", "Python", "JavaScript", "Java", "C#", "Python", "C++", "JavaScript", "Java"]


def calculate_frequencies(items: List[str]) -> Dict[str, int]:
    """returns a dictionary where keys are items and values are their frequencies"""
    frequencies: Dict[str, int] = {}
    for item in items:
        frequencies[item] = frequencies.get(item, 0) + 1
    return frequencies


def unique_items(items: List[str]) -> Set[str]:
    """returns a set of unique items from the list"""
    return set(items)

def top_n_items(frequencies: Dict[str, int], n: int) -> List[Tuple[str, int]]:
    """returns the top N most frequent items using dictionary items and tuple unpacking"""
    sorted_items: List[Tuple[str, int]] = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:n]

def print_summary(items: List[str], n: int = 3) -> None:
    """Print a clear, readable summary that shows frequencies, unique item count, and top results"""
    freqs = calculate_frequencies(items)
    unique_count = len(unique_items(items))
    top_items = top_n_items(freqs, n)

    print("Frequency Analysis Summary:")
    print(f"Total unique items: {unique_count}")
    print("Top items by frequency:")
    for item, freq in top_items:
        print(f"  {item}: {freq}")

if __name__ == "__main__":
    print_summary(survey_response)
    print_summary(survey_response, 6)