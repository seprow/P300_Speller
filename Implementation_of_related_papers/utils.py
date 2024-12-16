import numpy as np


def extract_channels(eloc_path, num_channels=64):

    channels = []

    try:
        with open(eloc_path, 'r') as file:
            for line in file.read().split('\n'):
                if line.strip(): 
                    channel_name = line.split('\t')[-1].split('.')[0]
                    channels.append(channel_name)

        channels = channels[:num_channels]

    except FileNotFoundError:
        print(f"Error: The file at {eloc_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return channels


def prepare_raw_signal(Signal):

    split_signal= [Signal[i] for i in range(Signal.shape[0])]
    concatenated_signal = np.concatenate(split_signal, axis=0)

    return concatenated_signal

