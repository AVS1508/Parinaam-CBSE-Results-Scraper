from setuptools import setup, find_packages

requires = ["selenium>=3.141.0"]

setup(
    name="CBSE-Results-Scraper",
    version="1.2.9",
    description=(
        "CBSE-Results-Scraper is a command-line Python application that scrapes and downloads student reports of CBSE (Central Board of Secondary Education) Class XII Results 2019 from http://cbseresults.nic.in."
    ),
    url="https://github.com/AVS1508/CBSE-Results-Scraper",
    download_url="https://github.com/AVS1508/CBSE-Results-Scraper/archive/master.zip",
    author="Aditya Vikram Singh",
    author_email="avsingh@umass.edu",
    license="Public Domain",
    packages=find_packages(),
    install_requires=requires,
    entry_points={"console_scripts": ["CBSE-Results-Scraper=cbse_results_scraper.app:main"],},
    zip_safe=False,
    keywords=["cbse", "results", "scraper", "download"],
)