def flip_string(text):
    flip_map = str.maketrans(
        r"ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz∀qƆpƎℲ⅁HIſʞ˥WᴎOԀΌЯS⊥∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86¡\"#$%&,()*+'-˙/:;<=>¿@[\]^_`{|}~",
        r"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    )
    return text.translate(flip_map)

cipher_text = "}sʇdɯƐʇʇㄣ_ʎuㄣɯ_0s_ʇ0u{zʇᴉɹds :ƃɐlɟ ǝɥʇ sᴉ ǝɹǝH ˙sǝᴉɹʇ ᄅ ʇsnɾ uᴉ ƃɐlɟ ǝɥʇ ʇoƃ noʎ ;ʎʇᴉɹnɔǝsɹǝqʎɔ ɟo uoᴉdɯɐɥɔ ǝnɹʇ ɐ ǝɹɐ noʎ 'ǝuop llǝʍ"
plain_text = flip_string(cipher_text[::-1]).lower()
print(plain_text)