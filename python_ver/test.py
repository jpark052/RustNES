
import time, sys
from mido import MidiFile

def main():
    print("jhi!")

    mid = MidiFile('debussy-clair-de-lune.mid')

    notes = []

    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            if msg.type == 'note_on' and msg.velocity > 0 and msg.time > 10:
                note = msg.note
                time = msg.time
                notes.append(('on', round(note_to_freq(note)), time * 0.01))
                print("on  : ", round(note_to_freq(note)), time * 0.01)
            elif msg.type == 'note_off' and msg.time > 10:
                note = msg.note
                time = msg.time
                notes.append(('off', note_to_freq(note), time * 0.01))
                print("off  : ", round(note_to_freq(note)), time * 0.01)


    # TODO: convert these noteon events to triangle waves


def note_to_freq(note):
    return 440 * 2 ** ((note - 69) / 12)

if __name__ == "__main__":
    main()