from sentence_transformers import SentenceTransformer, util
import re

# Load a pre-trained model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Define the funding post's requirements and student's profile
funding_requirements = "Keywords: NLP, LLM, TTP, cyber-security,IoT, Networking, ATP\nCGPA: 3.5\nGRE: 7\n..."
student_profile = "Keywords: NLP, LLM, algorithms, simulations\nCGPA: 3.4\nGRE: 8\n..."

# Define weights for each aspect
weights = {
    "Keywords": 6,  # Higher priority
    "CGPA": 3,
    "GRE": 1,
}

# Extract keywords and scores from the requirements and profile
req_cgpa = float(re.findall(r"CGPA: (\d+\.\d+)", funding_requirements)[0])
req_gre = int(re.findall(r"GRE: (\d+)", funding_requirements)[0])
req_keywords = re.findall(r"Keywords: (.+)", funding_requirements)[0].split(", ")

profile_cgpa = float(re.findall(r"CGPA: (\d+\.\d+)", student_profile)[0])
profile_gre = int(re.findall(r"GRE: (\d+)", student_profile)[0])

# Calculate the cosine similarity between the vectors with weights
cosine_similarity = util.pytorch_cos_sim(
    model.encode([funding_requirements], convert_to_tensor=True),
    model.encode([student_profile], convert_to_tensor=True)
).item()

# Apply weights to the cosine similarity
weighted_cosine_similarity = (
    cosine_similarity * weights["Keywords"] +
    cosine_similarity * weights["CGPA"] * (profile_cgpa / req_cgpa) +
    cosine_similarity * weights["GRE"] * (profile_gre / req_gre)
)
# Normalize the weighted cosine similarity
weighted_cosine_similarity /= sum(weights.values())

#print the weighted cosine similarity
print("Weighted cosine similarity:", weighted_cosine_similarity)

missing_keyword_penalty = 0.1/len(req_keywords)


# Calculate the set difference of missing keywords
req_keywords = re.findall(r"Keywords: (.+)", funding_requirements)[0].split(", ")
missing_keywords = set(req_keywords) - set(re.findall(r"Keywords: (.+)", student_profile)[0].split(", "))

# Apply penalty for missing keywords
missing_keywords_penalty = len(missing_keywords) * missing_keyword_penalty

print("Missing keywords penalty:", missing_keywords_penalty)

# Calculate the matching percentage
matching_percentage = max(0, weighted_cosine_similarity - missing_keywords_penalty)

if profile_cgpa < req_cgpa:
    matching_percentage = 0
    print("CGPA is too low")
if profile_gre < req_gre:
    matching_percentage = 0
    print("GRE is too low")

print("Matching percentage:", matching_percentage)
#print the missing keywords
print("Missing keywords:", missing_keywords)
