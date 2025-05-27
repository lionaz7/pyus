import argparse
import os
import json
import h5py

def convert_uff_to_bids(input_path, subject, session, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"sub-{subject}_ses-{session}_us.h5")
    metadata_path = os.path.join(output_dir, f"sub-{subject}_ses-{session}_us.json")

    # Mock copy
    with h5py.File(input_path, 'r') as f_in, h5py.File(output_path, 'w') as f_out:
        for name in f_in:
            f_in.copy(name, f_out)

    # Minimal metadata
    metadata = {
        "Manufacturer": "us4us",
        "Modality": "Ultrasound",
        "Format": "UFF",
        "TaskName": "RestingState",
        "BIDSVersion": "1.7.0"
    }

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"BIDS export complete: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--subject', required=True)
    parser.add_argument('--session', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    convert_uff_to_bids(args.input, args.subject, args.session, args.output)
