import os

# Define the base directory
BASE_DIR = "data-science-track"

# Define the folder structure
FOLDERS = [
    f"{BASE_DIR}/01-mathematical-foundations/notebooks",
    f"{BASE_DIR}/01-mathematical-foundations/code",
    f"{BASE_DIR}/01-mathematical-foundations/resources",

    f"{BASE_DIR}/02-programming/notebooks",
    f"{BASE_DIR}/02-programming/code",
    f"{BASE_DIR}/02-programming/resources",

    f"{BASE_DIR}/03-machine-learning/notebooks",
    f"{BASE_DIR}/03-machine-learning/code",
    f"{BASE_DIR}/03-machine-learning/resources",

    f"{BASE_DIR}/04-data-visualization/notebooks",
    f"{BASE_DIR}/04-data-visualization/code",
    f"{BASE_DIR}/04-data-visualization/resources",

    f"{BASE_DIR}/05-applications/projects",
    f"{BASE_DIR}/05-applications/resources"
]

# Define README content
README_CONTENT = {
    f"{BASE_DIR}/README.md": "# Data Science Track 🚀\n\nA structured learning path for Data Science.",
    f"{BASE_DIR}/01-mathematical-foundations/README.md": "# Mathematical Foundations\n\nLinear Algebra, Calculus, Probability & Statistics.",
    f"{BASE_DIR}/02-programming/README.md": "# Programming\n\nPython, SQL, and programming essentials.",
    f"{BASE_DIR}/03-machine-learning/README.md": "# Machine Learning\n\nCore ML concepts, models, and techniques.",
    f"{BASE_DIR}/04-data-visualization/README.md": "# Data Visualization\n\nCharts, graphs, and storytelling with data.",
    f"{BASE_DIR}/05-applications/README.md": "# Applications\n\nReal-world projects and case studies."
}

def create_folders():
    """Create the folder structure."""
    for folder in FOLDERS:
        os.makedirs(folder, exist_ok=True)
    print("✅ Folder structure created successfully.")

def create_files():
    """Create README.md files in each folder."""
    for file_path, content in README_CONTENT.items():
        with open(file_path, "w") as file:
            file.write(content)
    print("📝 README.md files created.")

def main():
    print("🚀 Setting up Data Science Track repository...")
    create_folders()
    create_files()
    print("🎯 Setup complete! Your folder structure is ready.")

if __name__ == "__main__":
    main()
