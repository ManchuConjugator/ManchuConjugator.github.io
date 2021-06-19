def conjugate(stem): #back [a, o, ū] front [e] neutral [i,u]

    if stem[-3:] == "mbi":
        stem = stem[:-3]
    
    vowels = ["a", "i", "e", "o", "u", "ū"]
    back_vowels = ["a", "o", "ū"]
    front_vowels = ["e"]
    neutral_vowels = ["i", "u"]

    

    last_vowels = [i for i in stem[::-1] if i in vowels]

    def vowel_harmony(last_vowels):
        if len(last_vowels) == 1:
            if last_vowels[0] == "a":
                vowel_suffix = "a"
            elif last_vowels[0] == "o":
                vowel_suffix = "o"
            elif last_vowels[0] in ["i", "e", "u"]:
                vowel_suffix = "e"
        elif len(last_vowels) == 2:
            last_string = "".join(last_vowels)
            if last_string in ["aa", "ūa", "ua", "io", "iū", "ia", "iu", "ii"]:
                vowel_suffix = "a"
            elif last_string in ["oo", "oa"]:
                vowel_suffix = "o"
            elif last_string in ["ee", "eo", "ue", "ie", "ui", "uu"]:
                vowel_suffix = "e"
        elif len(last_vowels) >= 3:
            if last_vowels[0] in ["a", "e", "o"]:
                vowel_suffix = last_vowels[0]
            if last_vowels[0] in ["i", "u"]:
                if last_vowels[1] == "e":
                    vowel_suffix = "e"
                elif last_vowels[1] in ["a", "u", "ū"]:
                    vowel_suffix = "a"
            if last_vowels[0] == "ū":
                vowel_suffix = "a"
        return vowel_suffix

    letter = vowel_harmony(last_vowels)

    perf_exceptions = [
        ["algi", "ešu", "bisa", "dosi", "gala", "gūwaliya", "hami", "isi", "jalu", "jura", "tafa", "tafu", "wasi"], #ka
        ["je", "dule", "ebere", "elde", "fuse", "gere", "mukde", "tuci", "tuhe", "wesi"], #ke
        ["colgoro", "soro", "tohoro"] #ko
    ]

    perf_conv_exceptions = [
        ["sa", "juwa", "we", "yu", "je"], #mpi
        ["hūwaliya", "colgoro", "desere", "dule", "gūwaliya", "suma"] #pi
    ]
    

    results = {
        "imperative": stem,
        "imperfect participle": None,
        "perfect participle": None, 
        "imperfect converb": stem + "me",
        "perfect converb": None, 
        "conditional converb": stem + "ci",
        "concessive converb": stem + "cibe",
        "terminal converb": None, 
        "prefatory converb": None, 
        "desiderative 1": stem + "ki",
        "desiderative 2": stem + "kini",
        "optative": stem + "cina",
        "temeritive": stem + "rahū"
    }

    if last_vowels[0] == "a":
        results["imperfect participle"] = stem + "ra"
    elif last_vowels[0] in ["e", "i", "u", "ū"]:
        results["imperfect participle"] = stem + "re"
    elif last_vowels[0] == "o":
        results["imperfect participle"] = stem + "ro"
        
    if stem in [i for i in (perf_exceptions[0] + perf_exceptions[1] + perf_exceptions[2])]:
        if stem in perf_exceptions[0]:
            results["perfect participle"] = stem + "ka"
        elif stem in perf_exceptions[1]:
            results["perfect participle"] = stem + "ke"
        elif stem in perf_exceptions[2]:
            results["perfect participle"] = stem + "ko"
    else:
        if letter in back_vowels:
            results["perfect participle"] = stem + "ha"
        if (letter in front_vowels) and (letter != "o"):
            results["perfect participle"] = stem + "he"
        if letter == "o":
            results["perfect participle"] = stem + "ho"

    if stem in [i for i in (perf_conv_exceptions[0] + perf_conv_exceptions[1])]:
        if stem in perf_conv_exceptions[0]:
            results["perfect converb"] = stem + "mpi"
        elif stem in perf_conv_exceptions[1]:
            results["perfect converb"] = stem + "pi"
    else:
        results["perfect converb"] = stem + "fi"

    if letter in back_vowels:
        results["terminal converb"] = stem + "tala"
    elif (letter in front_vowels) and (letter != "o"):
        results["terminal converb"] = stem + "tele"
    elif letter == "o":
        results["terminal converb"] = stem + "tolo"

    if letter in back_vowels:
        results["prefatory converb"] = stem + "nggala"
    elif (letter in front_vowels) and (letter != "o"):
        results["prefatory converb"] = stem + "nggele"
    elif letter == "o":
        results["prefatory converb"] = stem + "nggolo"

    return results
    