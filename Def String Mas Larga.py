def string_mas_larga(Texto, *Argumento):
    Palabras = list(Argumento)
    if Argumento:
        Palabras += [Texto]
        String_mas_larga = max(Palabras, key=len)
        return String_mas_larga



print(string_mas_larga("Python", "C Programming", "Java", "JavaScript"))
