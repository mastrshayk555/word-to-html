from lib.word_to_html import Converter
from datetime import datetime

author_dict = {
    "Jordan": {
        "full_name": "Jen Jordan",
        "file_handle": "JenJordanMarketing",
        "article_category": "Sales and Marketing",
    },
    "Sherman": {
        "full_name": "Aliza Sherman",
        "file_handle": "SocialMedia",
        "article_category": "Technology",
    },
    "Pelland": {
        "full_name": "Dave Pelland",
        "file_handle": "tech",
        "article_category": "Technology",
    },
    "Wallace": {
        "full_name": "Arla Wallace",
        "file_handle": "ArlaWallace",
        "article_category": "Business Finance",
    },
    "Best": {
        "full_name": "Rich Best",
        "file_handle": "Best",
        "article_category": "Financial, Business",
    },
    "Boyd": {
        "full_name": "Sharon Boyd",
        "file_handle": "SharonBoydBusiness",
        "article_category": "",
    },
    "Gina": {
        "full_name": "Gina Blitstein",
        "file_handle": "Gina",
        "article_category": "",
    },
    "Ramsey": {
        "full_name": "Dave Ramsey",
        "file_handle": "RamseyBusiness",
        "article_category": "Business Finance",
    },
}

name = "Pelland"
doc_file_title = ""
title = ""
description = ""
date = "05/15/2021"


def convert_date(date_str):
    date_obj = datetime.strptime(date_str, "%m/%d/%Y")
    file_date = date_obj.strftime("%Y%b%d")
    return file_date


def convert_to_html(name, date):
    file_date = convert_date(date)
    file_name = author_dict.get(name).get("file_handle")
    file = Converter(
        author=author_dict.get(name).get("full_name"),
        title=title,
        description=description,
        category=author_dict.get(name).get("article_category"),
        date=date,
        input_file=doc_file_title,
        output_file=f"{file_name}_{file_date}.htm",
    )
    file.write_html()
    file.clean_html()


convert_to_html(name, date)
