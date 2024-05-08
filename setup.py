from setuptools import setup, find_packages
import os
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
setup(
    name="mdbook_pdf_summary",
    version="0.1.0",
    author="cmq2525",
    author_email="cmq2525@foxmail.com",
    description="Generate outline for pdf generated by `mdbook-pdf`.",
    packages=find_packages(),
    install_requires=["lxml", "pypdf"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "mdbook-pdf-summary=mdbook_pdf_summary.mdbook_pdf_summary:main"
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
)