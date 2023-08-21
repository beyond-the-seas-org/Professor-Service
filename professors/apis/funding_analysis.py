from nltk.tokenize import word_tokenize

# If you haven't downloaded the punkt tokenizer, do so first
# nltk.download('punkt')

def extract_keywords(text, cs_terms):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Filter out the tokens based on the computer science terms list
    keywords = [word for word in tokens if word in cs_terms]
    
    # Make the list unique
    keywords = list(set(keywords))
    
    return keywords

# A predefined list of computer science terms (this can be expanded)
cs_terms = {
    "artificial intelligence", "neural networks", "optimization", "logistics", 
    "transportation", "finance", "engineering", "machine learning", "data mining", 
    "deep learning", "natural language processing", "algorithm", "computational", 
    "database", "security", "cryptography", "software engineering", "computer graphics", 
    "quantum computing", "distributed systems", "bioinformatics", "robotics", "computer vision",
    "computer architecture", "operating systems", "computer networks", "human-computer interaction",
    "computer science", "computer", "science", "computing", "computers", "software", "hardware",
    
}

funding_post = """
Combinatorial optimization problems are ubiquitous across various industries, ranging from logistics 
and transportation to finance and engineering. This research project seeks to leverage the capabilities 
of neural networks to develop novel approaches for solving these intricate problems more efficiently and 
effectively than traditional methods. By combining the strengths of artificial intelligence and optimization, 
we aim to push the boundaries of what's possible and create innovative solutions with real-world impact.
"""

keywords = extract_keywords(funding_post, cs_terms)
print(keywords)
