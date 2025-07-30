
def load_help_documentation(section):
    """Carica la documentazione HTML da file esterni per la sezione richiesta."""
    import os
    base_path = os.path.join(os.path.dirname(__file__), "help_docs")
    section_file = os.path.join(base_path, f"{section}.html")
    if os.path.exists(section_file):
        with open(section_file, "r", encoding="utf-8") as f:
            return f.read()
    return f"<h1>Documentazione non trovata per: {section}</h1>"
