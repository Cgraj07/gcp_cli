from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="gcp-cli",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="AI-powered CLI for executing GCP commands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/gcp-cli",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "google-cloud-aiplatform>=1.38.0",
        "click>=8.1.0",
        "PyYAML>=6.0",
        "rich>=13.0.0",
        "google-auth>=2.23.0",
        "google-cloud-storage>=2.10.0",
    ],
    entry_points={
        "console_scripts": [
            "gcp-cli=gcp_cli.cli:main",
        ],
    },
)
