TITLE = "AdTEC: A Unified Benchmark for Evaluating Text Quality in Search Engine Advertising"

AUTHORS = [
    {
        "name": "Peinan Zhang",
        "affiliations": ["CyberAgent"],
        "email": "zhang_peinan@cyberagent.co.jp",
        "url": "https://peinan.cc",
    },
    {
        "name": "Yusuke Sakai",
        "affiliations": ["Nara Institute of Science and Technology"],
        "email": "sakai.yusuke.sr9@is.naist.jp",
        "url": "https://aclanthology.org/people/y/yusuke-sakai/",
    },
    {
        "name": "Masato Mita",
        "affiliations": ["CyberAgent"],
        "email": "mita_masato@cyberagent.co.jp",
        "url": "https://aclanthology.org/people/m/masato-mita/",
    },
    {
        "name": "Hiroki Ouchi",
        "affiliations": ["Nara Institute of Science and Technology", "CyberAgent"],
        "email": "hiroki.ouchi@is.naist.jp",
        "url": "https://aclanthology.org/people/h/hiroki-ouchi/",
    },
    {
        "name": "Taro Watanabe",
        "affiliations": ["Nara Institute of Science and Technology"],
        "email": "taro@is.naist.jp",
        "url": "https://aclanthology.org/people/t/taro-watanabe/",
    },
]

UNIQUE_AFFILIATIONS = list(
    dict.fromkeys(  # Remove duplicates while preserving order
        [affiliation for author in AUTHORS for affiliation in author["affiliations"]]
    )
)

AFFILIATION_SYMBOLS = ["♠︎", "◇"]

AFFILIATION_SYMBOLS_MAP = {
    affiliation: symbol
    for affiliation, symbol in zip(UNIQUE_AFFILIATIONS, AFFILIATION_SYMBOLS)
}

CONFERENCE = "NAACL 2025"

MATERIALS = {
    "Paper": {
        "url": "https://arxiv.org/pdf/2408.05906",
        "icon": "file-text",
        "is_external": True,
    },
    "arXiv": {
        "url": "https://arxiv.org/abs/2408.05906",
        "icon": "graduation-cap",
        "is_external": True,
    },
    "Code": {
        "url": "https://github.com/cyberagentailab/adtec",
        "icon": "github",
        "is_external": True,
    },
    "Dataset": {
        "url": "https://huggingface.co/cyberagent",
        "icon": "database",
        "is_external": True,
    },
    "Poster": {
        "url": "",
        "icon": "camera",
        "is_external": True,
    },
    "Slides": {
        "url": "",
        "icon": "images",
        "is_external": True,
    },
    "Video": {
        "url": "",
        "icon": "video",
        "is_external": True,
    },
}

ABSTRACT_MD = (
    "With the increase in the fluency of ad texts automatically created by natural language generation technology, "
    "there is high demand to verify the quality of these creatives in a real-world setting. We propose **AdTEC** (**Ad** **T**ext "
    "**E**valuation Benchmark by **C**yberAgent), the first public benchmark to evaluate ad texts from multiple perspectives "
    "within practical advertising operations. Our contributions are as follows: (i) Defining five tasks for evaluating "
    "the quality of ad texts, as well as building a Japanese dataset based on the practical operational experiences of "
    "building a Japanese dataset based on the practical operational experiences of advertising agencies, which are "
    "typically kept in-house. (ii) Validating the performance of existing pre-trained language models (PLMs) and "
    "human evaluators on the dataset. (iii) Analyzing the characteristics and providing challenges of the benchmark. "
    "The results show that while PLMs have already reached practical usage level in several tasks, humans still "
    "outperform in certain domains, implying that there is significant room for improvement in this area."
)

BIBTEX = """@inproceedings{zhang2025adtec,
  title={{AdTEC}: A Unified Benchmark for Evaluating Text Quality in Search Engine Advertising},
  author={Peinan Zhang and Yusuke Sakai and Masato Mita and Hiroki Ouchi and Taro Watanabe},
  booktitle={Proceedings of the 2025 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT)},
  year={2025},
  publisher={Association for Computational Linguistics},
  eprint={2408.05906},
  primaryClass={cs.CL},
  url={https://arxiv.org/abs/2408.05906},
}
"""
