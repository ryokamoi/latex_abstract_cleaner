import re

if __name__ == "__main__":
    with open("original.txt", "r") as f:
        abstract = f.read()
    
    # remove comments (row after %)
    abstract = re.sub(r"%.*", "", abstract)
    
    # remove texts in \rui{} and \ryo{}
    # e.t., "\ryo{this is a comment}" -> ""
    for func in ["rui", "ryo"]:
        abstract = re.sub(r"\\{}{{.*?}}".format(func), "", abstract)
    
    # replace to spaces
    replace_to_space = ["~"]
    abstract = re.sub("|".join(replace_to_space), " ", abstract)
    
    # remove
    remove_list = ["{}"]
    abstract = re.sub("|".join(remove_list), "", abstract)
    
    # replace
    replace_list = [["\\visonlyqa", "VisOnlyQA"]]
    for replace in replace_list:
        abstract = abstract.replace(replace[0], replace[1])
    
    # remove line breaks
    abstract = abstract.replace("\n", " ")
    
    # remove double spaces
    abstract = re.sub(r"\s+", " ", abstract)
    
    with open("converted.txt", "w") as f:
        f.write(abstract)
    