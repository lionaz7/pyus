# uff2bids

A lightweight tool for exporting ultrasound data stored in UFF format (from us systems for example) to the Brain Imaging Data Structure (BIDS) format.

## Features

- Loads UFF files (.h5) from us systems
- Converts metadata and waveform structures into BIDS-compatible format
- Generates subject/session file trees under /exports/bids
- Outputs standard sidecar .json files with modality metadata

## Requirements

- Python 3.8+
- h5py
- numpy
- json
- os

## Usage

```bash
python src/uff2bids_exporter.py --input data/sample.uff --subject 01 --session 01 --output exports/bids
```


---

## Disclaimer

This tool and its included dataset are intended for testing and development purposes only.  
The included `.uff` file and metadata are artificially generated and not suitable for scientific use.
