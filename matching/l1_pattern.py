l1_resection_pattern = [
    {
        "RIGHT_ID": "anchor_resection",
        "RIGHT_ATTRS": {
        "ORTH": {"IN": ["resection", "resected", "removed", "excised", "cut out"]}
        },
    },
    {
        "LEFT_ID": "anchor_resection",
        "REL_OP": ";*",
        "RIGHT_ID": "resection_subject",
        "RIGHT_ATTRS": {"DEP": "nsubjpass", "_": {"has_ileal": True}},
    },
]


l1_endoscopy_patterns = [
    {
        "RIGHT_ID": "anchor_endoscopy",
        "RIGHT_ATTRS": {"ORTH": "findings"},
    },
    {
        "LEFT_ID": "anchor_endoscopy",
        "REL_OP": ">",
        "RIGHT_ID": "endoscopy_subject",
        "RIGHT_ATTRS": {"DEP": "nmod", "_": {"has_cecum": True}},
    },
]
