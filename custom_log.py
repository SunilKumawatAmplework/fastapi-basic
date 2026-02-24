def debug_log(tag="", message=""):
    with open("log.txt", "w+") as log:
        log.write(f"{tag}: {message}")
