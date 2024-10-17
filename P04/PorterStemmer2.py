import re

# Define a rule-based approach for guessing root forms
def rule_based_root(word):
    # Define rules for specific patterns
    rules = [
        (r'ly$', ''),            # Adverbs like "particularly" -> "particular"
        (r'd$', ''),            # Past tense like "believed" -> "believe"

        (r's$', ''),             # General plural removal
        (r'ly$', ''),            # Re-apply ly rule as needed
        (r'ness$', ''),          # Nouns like "happiness" -> "happy"
        (r'ful$', ''),           # Adjectives like "beautiful" -> "beauty"
        (r'ous$', ''),           # Adjectives like "dangerous" -> "danger"
        (r'able$', ''),          # Adjectives like "comfortable" -> "comfort"
        (r'less$', ''),          # Adjectives like "careless" -> "care"
        (r'ize$', ''),           # Verbs like "realize" -> "real"
        (r'ify$', ''),           # Verbs like "intensify" -> "intense"
        (r'ise$', ''),           # Verbs like "realise" -> "real"
        (r'ate$', ''),           # Verbs like "activate" -> "active"
        (r'al$', ''),            # Adjectives like "magical" -> "magic"
        (r'ing$', ''),           # Continuous tense like "sprawling" -> "sprawl"
    ]
    
    for pattern, repl in rules:
        if re.search(pattern, word):
            return re.sub(pattern, repl, word)
    
    return word  # Return the original word if no rule matches

# Example words
words = [
    "animals",
    "particularly",
    "oak",
    "its",
    "edge",
    "sprawling",
    "believed",
    "creatures",
    "magical"
]

# Process each word
for word in words:
    root_word = rule_based_root(word)
    print(f"Original: {word}, Root: {root_word}")
