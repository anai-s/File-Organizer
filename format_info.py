import os

format = {
    "audio": (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv"),

    "video": (".webm", ".MTS", ".M2TS", ".TS", ".mov",
            ".mp4", ".m4p", ".m4v", ".mxf", ".mpg"),

    "img": (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
        ".gif", ".webp", ".svg", ".apng", ".avif"),

    "csv": (".csv", ".xls", ".xlsx", ".xlsm", ".xltx"),

    "doc": (".odt", ".docx", ".doc", ".rtf"),

    "ppt": (".pptx", ".odp"),

    "other_formats": (".txt", ".ics", ".sas", ".egp", ".sas7bdat", ".dat"),

    "zip": (".zip", ".rar"),

    "pdf": (".pdf"),

    "py": (".py"),

    "ipynb": (".ipynb"),

    "sql": (".sql"),

    "exe": (".exe", ".msi")
}


destination = {

    "audio": "C:\\Users\\anais\\Music",
    "video": "C:\\Users\\anais\\Videos",
    "screenshot": "C:\\Users\\anais\\Pictures\\Screenshot",
    "img": "C:\\Users\\anais\\Pictures",
    "csv": "C:\\Users\\anais\\Documents\\To sort\\CSV",
    "ppt": "C:\\Users\\anais\\Documents\\To sort\\Powerpoint",
    "doc": "C:\\Users\\anais\\Documents\\To sort\\Documents",
    "pdf": "C:\\Users\\anais\\Documents\\To sort\\PDF",
    "py": "C:\\Users\\anais\\Documents\\Python Script",
    "ipynb": "C:\\Users\\anais\\Documents\\Notebook",
    "sql": "C:\\Users\\anais\\Documents\\SQL Script",
    "exe": "C:\\Users\\anais\\Downloads\\Exec Files",
    "zip": "C:\\Users\\anais\\Downloads\\ZIP",
    "other_formats": "C:\\Users\\anais\\Documents\\To sort\\Other formats"

}
