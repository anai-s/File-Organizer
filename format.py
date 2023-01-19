import os
import format_info as finfo

def find_format(file):
    """
    return the format of the file based on its extension.
    finfo.format: dictionnary with file formats as keys and values are tuples of file extensions 
    associated with the key format

    """
    name, extension = os.path.splitext(file)
    if extension == "":
        return None
    if (extension in finfo.format["img"]) and ("capture" in name.lower()):
        return "screenshot"
    for key,value in finfo.format.items():
        if extension in value:
            return key

class File:
    def __init__(self, file) -> None:
        self.format = find_format(file)
    
    def file_destination(self):
        """
        return the destination where 
        finfo.destination: dictionnary with the formats as keys and path of file destination

        """
        if self.format != None:
            return finfo.destination[self.format]
        else:
            return None
