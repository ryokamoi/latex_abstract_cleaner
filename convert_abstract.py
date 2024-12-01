import re
import csv

if __name__ == "__main__":
    with open("original.txt", "r") as f:
        abstract = f.read()

    # read replace list from CSV file
    replace_list = []
    with open("replace_list.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                replace_list.append(row)
    
    # add hardcoded replacements
    replace_list.append(["---", "&mdash;"])
    
    # replace
    for replace in replace_list:
        abstract = abstract.replace(replace[0], replace[1])
    
    # remove comments (row after %)
    abstract = re.sub(r"%.*", "", abstract)
    
    # remove texts like \rui{} and \ryo{}
    # but do not remove \url{}
    abstract = re.sub(r'\\(?!url\b)\w+\{.*?\}', "", abstract)
    
    # \url{text} -> text
    abstract = re.sub(r'\\url\{(.+?)\}', r'\1', abstract)
    
    # replace to spaces
    replace_to_space = ["~"]
    abstract = re.sub("|".join(replace_to_space), " ", abstract)
    
    # remove
    remove_list = ["{}"]
    abstract = re.sub("|".join(remove_list), "", abstract)
    
    # remove line breaks
    abstract = abstract.replace("\n", " ")
    
    # remove double spaces
    abstract = re.sub(r"\s+", " ", abstract)
    
    with open("converted.txt", "w") as f:
        f.write(abstract)
    