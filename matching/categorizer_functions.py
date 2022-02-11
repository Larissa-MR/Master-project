# CUI Filtering function: consumes list of allowed CUIs (str) and doc.ents, returns only those entities that do have the specified CUIs.


def filterbycui(allowedcuis, ents):
    filteredents = []
    for ent in ents:
        for i in [item[0] for item in ent._.kb_ents]:
            if i in allowedcuis:
                filteredents.append(ent)
                break
    return filteredents


# Multiplication of a template pattern with a list of dictionaries that contain the desired attributes.
# Requires that the RIGHT_ID of the token whose attributes shall be alternated begin with "cncpt_"


def patternmultiply(template_pattern, concept_attributes, right_id):
    import copy

    outputpatterns = []
    foundsmth = False

    for num, d in enumerate(template_pattern):
        if d["RIGHT_ID"] == right_id:
            foundsmth = True
            for psbtok in concept_attributes:
                # print(psbtok)
                newpattern = copy.deepcopy(template_pattern)
                # print(newpattern[num])
                newpattern[num].update({"RIGHT_ATTRS": psbtok})
                # print(newpattern[num])
                outputpatterns.append(newpattern)

    if not foundsmth:
        raise Exception(
            "TemplateError: No RIGHT_ID with the value '"
            + right_id
            + "' was found in the provided template pattern!"
        )
    return outputpatterns


# Dummy Output function for Token Matcher: Written as a proof-of-concept, will most probably need more columns for debugging info.
# Should be extended by context and section information from medspacy components
# def outputfiller(outputdict, ):


def rawoutput(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    if start > end:
        start, end = end, start
    try:
        negation = any([tok._.is_negated for tok in doc[start : end + 1]])
    except:
        negation = None

    print(doc[start:end])
    if doc.vocab.strings[match_id] == "L1_Procedure":
        doc._.output["PatID"].append(doc._.metadata["patid"])
        doc._.output["Date"].append(doc._.metadata["date"])
        doc._.output["CoarseCat"].append("L1")
        doc._.output["FineCat"].append("L1 procedure")
        doc._.output["MatchSpan"].append(doc[start : end + 1])
        doc._.output["Negation"].append(negation)
    elif doc.vocab.strings[match_id] == "L1_Endoscopy":
        doc._.output["PatID"].append(doc._.metadata["patid"])
        doc._.output["Date"].append(doc._.metadata["date"])
        doc._.output["CoarseCat"].append("L1")
        doc._.output["FineCat"].append("L1 endoscopy")
        doc._.output["MatchSpan"].append(doc[start : end + 1])
        doc._.output["Negation"].append(negation)
    elif doc.vocab.strings[match_id] == "L1_Imaging":
        doc._.output["PatID"].append(doc._.metadata["patid"])
        doc._.output["Date"].append(doc._.metadata["date"])
        doc._.output["CoarseCat"].append("L1")
        doc._.output["FineCat"].append("L1 imaging")
        doc._.output["MatchSpan"].append(doc[start : end + 1])
        doc._.output["Negation"].append(negation)


# NOT OPERATIONAL


def drawoutput(matcher, doc, i, matches):
    match_id, startend = matches[i]
    start = min(startend)
    end = max(startend)
    try:
        negation = any([tok._.is_negated for tok in doc[start : end + 1]])
    except:
        negation = None

    if doc.vocab.strings[match_id] == "L1_Procedure":
        doc._.output["PatID"].append(doc._.metadata["patid"])
        doc._.output["Date"].append(doc._.metadata["date"])
        doc._.output["CoarseCat"].append("L1")
        doc._.output["FineCat"].append("L1 procedure")
        doc._.output["MatchSpan"].append(doc[start : end + 1])
        doc._.output["Negation"].append(negation)
    elif doc.vocab.strings[match_id] == "L1_Endoscopy":
        doc._.output["PatID"].append(doc._.metadata["patid"])
        doc._.output["Date"].append(doc._.metadata["date"])
        doc._.output["CoarseCat"].append("L1")
        doc._.output["FineCat"].append("L1 endoscopy")
        doc._.output["MatchSpan"].append(doc[start : end + 1])
        doc._.output["Negation"].append(negation)
    elif doc.vocab.strings[match_id] == "L1_Imaging":
        doc._.output["PatID"].append(doc._.metadata["patid"])
        doc._.output["Date"].append(doc._.metadata["date"])
        doc._.output["CoarseCat"].append("L1")
        doc._.output["FineCat"].append("L1 imaging")
        doc._.output["MatchSpan"].append(doc[start : end + 1])
        doc._.output["Negation"].append(negation)
