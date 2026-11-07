"""Static data for the Hindu cosmos map: worlds, descriptions, rings and geometry."""

# name, subtitle, band height, colour, group ("up" = upper, "tri" = Bhur/Bhuvar/Svar, "low")
LAYERS = [
    ("Satyaloka", "Brahma, no rebirth", 9, "#FBEFC0", "up"),
    ("Tapoloka", "Ascetic sages", 6, "#F8E3B0", "up"),
    ("Janaloka", "Brahma's sons", 6, "#F2D9C3", "up"),
    ("Maharloka", "Great sages", 6, "#E9D0DE", "up"),
    ("Svarloka", "Indra and the devas", 10, "#CFE3F6", "tri"),
    ("Bhuvarloka", "Sun, moon, planets", 9, "#B5D4F4", "tri"),
    ("Bhurloka", "Earth and humans", 8, "#DCEBF7", "tri"),
    ("Atala", "", 2.4, "#9C8FE0", "pat"),
    ("Vitala", "", 2.4, "#7FA7E8", "pat"),
    ("Sutala", "", 2.4, "#6FC3A0", "pat"),
    ("Talatala", "", 2.4, "#E7B94E", "pat"),
    ("Mahatala", "", 2.4, "#E58B6E", "pat"),
    ("Rasatala", "", 2.4, "#D96C9A", "pat"),
    ("Patala", "", 2.4, "#7B6AD0", "pat"),
    ("Naraka", "Yama's hells", 9, "#4A3A3A", "low"),
    ("Shesha", "Serpent beneath all worlds", 12.2, "#26323B", "low"),
]

PATALA_TEXT = (
    "one of the seven underworlds (Atala, Vitala, Sutala, Talatala, Mahatala, Rasatala, Patala). "
    "Nagas, daityas and danavas live in jewel-lit cities, and the King Bali rules Sutala."
)
DESC = {
    "Satyaloka": "Satyaloka: Brahma's own world (Brahmaloka). Beings who reach it are not reborn until the whole universe dissolves.",
    "Tapoloka": "Tapoloka: world of ascetics, reached through intense austerity.",
    "Janaloka": "Janaloka: world of Brahma's mind-born sons, such as Sanaka and Sanandana. Sages of Maharloka retreat here when the lower worlds burn.",
    "Maharloka": "Maharloka: world of great sages such as Bhrigu. It outlasts the fire at the end of each day of Brahma, though its sages withdraw upward.",
    "Svarloka": "Svarloka (Svarga): Indra's heaven on and above Mount Meru, with its capital Amaravati. A reward for merit; rebirth follows when merit runs out.",
    "Bhuvarloka": "Bhuvarloka: the sky between earth and the pole star. Sun, moon, planets and stars circle Meru here, along with siddhas and spirits.",
    "Bhurloka": "Bhurloka: the earth, a flat disc with Jambudvipa at its centre, Mount Meru at its axis and Bharatavarsha (the Indian subcontinent) in the south.",
    "Naraka": "Naraka: realms of punishment under Yama's justice. Punishment is temporary and ends in rebirth, not damnation.",
    "Shesha": "Shesha (Ananta): the thousand-headed serpent beneath all worlds, who is also Vishnu's couch between universes.",
    "Beyond": "Vaikuntha (Vishnu), Kailasa (Shiva) and Goloka (Krishna) lie beyond the egg, depending on the sectarian tradition.",
    "Night": "Night of Brahma: at the end of each day of Brahma the three lower worlds (Bhur, Bhuvar, Svar) are consumed by fire and flood, "
             "and the sages of Maharloka retreat to Janaloka. Creation resumes at dawn.",
    "Day": "Day of Brahma: the worlds are in existence. A day lasts about 4.32 billion years.",
}
for _n in ("Atala", "Vitala", "Sutala", "Talatala", "Mahatala", "Rasatala", "Patala"):
    DESC[_n] = f"{_n}: {PATALA_TEXT}"

# Top view rings: name, outer radius (schematic, not to scale), colour, description
RINGS = [
    ("Jambudvipa", 31, "#E9B949", "Jambudvipa: the central continent, named for the jambu (rose-apple) tree. Mount Meru stands at its centre and Bharatavarsha lies in its south."),
    ("Lavana, salt ocean", 45, "#85B7EB", "Lavana: the salt ocean surrounding Jambudvipa. Seven liquid oceans alternate with seven continents."),
    ("Plakshadvipa", 63, "#97C459", "Plakshadvipa: named for the plaksha fig tree. In the Bhagavata Purana each continent and ocean is twice as wide as the one inside it (rings here are schematic)."),
    ("Ikshu, sugarcane juice", 76, "#E3E39A", "Ikshu: the ocean of sugarcane juice."),
    ("Shalmalidvipa", 94, "#7FB069", "Shalmalidvipa: named for the silk-cotton (shalmali) tree."),
    ("Sura, wine", 106, "#B04A6A", "Sura: the ocean of wine."),
    ("Kushadvipa", 124, "#639922", "Kushadvipa: named for sacred kusha grass."),
    ("Sarpis, ghee", 137, "#F2C94C", "Sarpis: the ocean of clarified butter (ghee)."),
    ("Krauncadvipa", 155, "#4F9A6A", "Krauncadvipa: named for the Krauncha mountain."),
    ("Dadhi, curd", 167, "#F4F0E6", "Dadhi: the ocean of curd (yogurt)."),
    ("Shakadvipa", 185, "#3F8A4F", "Shakadvipa: named for the teak (shaka) tree."),
    ("Kshira, milk", 198, "#FFFFFF", "Kshira: the ocean of milk. Popular tradition links it with the Kshira Sagara where Vishnu rests; texts differ on the identification."),
    ("Pushkaradvipa", 216, "#2F7A5A", "Pushkaradvipa: named for the lotus (pushkara). The Manasottara mountain splits it into two rings."),
    ("Svadu, fresh water", 228, "#9FD8E8", "Svadu: the ocean of sweet, fresh water, the last of the seven."),
]
LOKALOKA_R, DARK_R = 238, 262
DESC["Lokaloka"] = "Lokaloka: the ring of mountains at the edge of the world. Light falls inside it; darkness lies outside."
DESC["Dark"] = "Beyond Lokaloka lies darkness (aloka), and then the concentric shells of the cosmic egg."

# Side-view geometry: top of the stack, egg centre and egg width/height
TOP, CX, CY, EW, EH = 96.0, 50.0, 50.0, 70.0, 92.0
