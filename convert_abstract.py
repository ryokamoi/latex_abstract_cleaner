import re

if __name__ == "__main__":
    with open("original.txt", "r") as f:
        abstract = f.read()

    # replace
    replace_list = [["\\visonlyqa", "VisOnlyQA"]]
    for replace in replace_list:
        abstract = abstract.replace(replace[0], replace[1])
    
    # remove comments (row after %)
    abstract = re.sub(r"%.*", "", abstract)
    
    # remove texts like \rui{} and \ryo{}
    abstract = re.sub(r"\\[a-z]+{.*?}", "", abstract)
    
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
    