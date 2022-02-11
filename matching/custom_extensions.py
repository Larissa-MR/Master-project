# Reading pre-specified CSV with CUIs and group by which they should be made available on token level for the matchers
df_codes = pd.read_csv("RelevantCUIs.csv")

# Creating lists of actual entities in the unstructured data
ilealents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "ilealents"].tolist(), doc.ents
)
resecents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "resecents"].tolist(), doc.ents
)
uppergistrictents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "uppergistrictents"].tolist(), doc.ents
)
lesionents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "lesionents"].tolist(), doc.ents
)
cecuments = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "cecuments"].tolist(), doc.ents
)
cblstnents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "cblstnents"].tolist(), doc.ents
)
inflaments = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "inflaments"].tolist(), doc.ents
)
l1procents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "l1procents"].tolist(), doc.ents
)
colonents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "colonents"].tolist(), doc.ents
)
l2procents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "l2procents"].tolist(), doc.ents
)
uppergients = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "uppergients"].tolist(), doc.ents
)
l4procents = filterbycui(
    df_codes.Code.loc[df_codes["Category"] == "l2procents"].tolist(), doc.ents
)

# CUIs
for i in [
    "has_ileal",
    "has_resec",
    "has_l1proc",
    "has_inflam",
    "has_lesion",
    "has_cecum",
    "has_cblstn",
    "has_colon",
    "has_l2proc",
    "has_uppergi",
    "has_uppergistrict",
    "has_l4proc",
]:
    Token.set_extension(i, default=False, force=True)

# NEGATION
Token.set_extension("is_negated", default=False, force=True)

negation_tokens = [tok for tok in doc if tok.dep_ == "neg"]
negation_head_tokens = [token.head for token in negation_tokens]

print("\n---- NEGATION DETECTION ----")
print("\nBy dependency:\n")

for tok in negation_head_tokens:
    print("negated:", tok)
    tok._.is_negated = True

print("\nBy context:\n")

for ent in doc.ents:

    # NEGATION
    if ent._.is_negated:
        for tok in ent:
            print("negated:", tok)
            tok._.is_negated = True

    # CUIs
    if ent in ilealents:
        for tok in ent:
            tok._.has_ileal = True
    if ent in resecents:
        for tok in ent:
            tok._.has_resec = True
    if ent in l1procents:
        for tok in ent:
            tok._.has_l1proc = True
    if ent in inflaments:
        for tok in ent:
            tok._.has_inflam = True
    if ent in lesionents:
        for tok in ent:
            tok._.has_lesion = True
    if ent in cecuments:
        for tok in ent:
            tok._.has_cecum = True
    if ent in cblstnents:
        for tok in ent:
            tok._.has_cblstn = True
    if ent in colonents:
        for tok in ent:
            tok._.has_colon = True
    if ent in l2procents:
        for tok in ent:
            tok._.has_l2proc = True
    if ent in uppergients:
        for tok in ent:
            tok._.has_uppergi = True
    if ent in uppergistrictents:
        for tok in ent:
            tok._.has_uppergistrict = True
    if ent in l4procents:
        for tok in ent:
            tok._.has_l4proc = True
