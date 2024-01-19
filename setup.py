import setuptools

with open("README.md" , "r" , encoding="utf-8") as f:
    long_desc = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summerizer-Project"
AUTHOR_USER_NAME= "PreetKumarPanchani"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL= "preet@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summerizer Project",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir = {"" : "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',

)