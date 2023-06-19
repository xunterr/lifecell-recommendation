class Question:
    def __init__(self, question, variants: list, prep_variants: list) -> None:
        self.question:list = question
        self.variants:list = variants
        self.prepared_variants:list = prep_variants
