def ontcijfer(bericht, key):
    oncijferd_bericht= ""
    for letter in bericht:
        if letter in key:
            oncijferd_bericht += letter
    return oncijferd_bericht