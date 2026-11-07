   **Live 3D version:** https://itsmn10.github.io/hindu-cosmos/
# Hindu cosmos, animated

An animated map of the Hindu cosmos in Python, based on the common Puranic model.

## What it shows

- **Side view:** the Brahmanda (cosmic egg) with its 14 worlds, from Satyaloka down to the Patalas, Naraka and Shesha, with Mount Meru at the axis. The sun and moon circle Meru, stars and gems twinkle, and flames flicker in Naraka.
- **Top view:** Bhumandala, the disc of the earth. Jambudvipa sits in the centre, surrounded by alternating continents and oceans (salt water, sugarcane juice, wine, ghee, curd, milk, fresh water), out to the Lokaloka mountains.
- **Night of Brahma:** a toggle that fades the three lower worlds (Bhur, Bhuvar, Svar), as at the end of each day of Brahma.

Ring widths in the top view are schematic, not to scale. Hindu cosmology varies by text and tradition, so this is one common model, not the only one.

## Run it

```
pip install -r requirements.txt
python hindu_cosmos.py
```

Controls: press `n` or click the button for the night of Brahma, and click any world or ring to read about it.

To save instead of opening a window:

```
python hindu_cosmos.py --png cosmos.png
python hindu_cosmos.py --gif cosmos.gif
```

## Sources

The descriptions follow the Bhagavata Purana (canto 5) and the Vishnu Purana (book 2). Check the primary texts for details, since traditions differ.

## Ideas for next steps

- Hover highlights and tooltips
- A scene of Vishnu on Shesha in the cosmic ocean
- A clock for the yugas, mahayuga and kalpa
- A to-scale toggle for the continent and ocean rings
