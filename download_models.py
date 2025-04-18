#!/usr/bin/env python

import os
import argparse
import urllib.request
from patchnetvlad.tools import PATCHNETVLAD_ROOT_DIR


def ask_yesno(question):
    """
    Helper to get yes / no answer from user.
    """
    yes = {'yes', 'y'}
    no = {'no', 'n', 'q', 'quit'}  # pylint: disable=invalid-name

    done = False
    print(question)
    while not done:
        choice = input().lower()
        if choice in yes:
            return True
        elif choice in no:
            return False
        else:
            print("Please respond \'yes\' or \'no\'.")


def download_all_models(ask_for_permission=False):
    dest_dir = os.path.join(PATCHNETVLAD_ROOT_DIR, 'pretrained_models')
    if not ask_for_permission or ask_yesno("Auto-download pretrained models into " + dest_dir + " (takes around 3GB of space)? Yes/no."):
        if not os.path.isfile(os.path.join(dest_dir, "mapillary_WPCA128.pth.tar")):
            print('Downloading mapillary_WPCA128.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/mapillary_WPCA128.pth.tar?download=true", os.path.join(dest_dir, "mapillary_WPCA128.pth.tar"))
        if not os.path.isfile(os.path.join(dest_dir, "mapillary_WPCA512.pth.tar")):
            print('Downloading mapillary_WPCA512.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/mapillary_WPCA512.pth.tar?download=true", os.path.join(dest_dir, "mapillary_WPCA512.pth.tar"))
        if not os.path.isfile(os.path.join(dest_dir, "mapillary_WPCA4096.pth.tar")):
            print('Downloading mapillary_WPCA4096.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/mapillary_WPCA4096.pth.tar?download=true", os.path.join(dest_dir, "mapillary_WPCA4096.pth.tar"))
        if not os.path.isfile(os.path.join(dest_dir, "pittsburgh_WPCA128.pth.tar")):
            print('Downloading pittsburgh_WPCA128.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/pitts_WPCA128.pth.tar?download=true", os.path.join(dest_dir, "pittsburgh_WPCA128.pth.tar"))
        if not os.path.isfile(os.path.join(dest_dir, "pittsburgh_WPCA512.pth.tar")):
            print('Downloading pittsburgh_WPCA512.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/pitts_WPCA512.pth.tar?download=true", os.path.join(dest_dir, "pittsburgh_WPCA512.pth.tar"))
        if not os.path.isfile(os.path.join(dest_dir, "pittsburgh_WPCA4096.pth.tar")):
            print('Downloading pittsburgh_WPCA4096.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/pitts_WPCA4096.pth.tar?download=true", os.path.join(dest_dir, "pittsburgh_WPCA4096.pth.tar"))
        if not os.path.isfile(os.path.join(dest_dir, "landmarks_WPCA4096.pth.tar")):
            print('Downloading landmarks_WPCA4096.pth.tar')
            urllib.request.urlretrieve("https://huggingface.co/TobiasRobotics/Patch-NetVLAD/resolve/main/landmarks_WPCA4096.pth.tar?download=true", os.path.join(dest_dir, "landmarks_WPCA4096.pth.tar"))
        print('Downloaded all pretrained models.')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download Pretrained Models for Patch-NetVLAD')
    parser.add_argument('--ask_for_permission', action='store_true',
                        help='Ask for permission before downloading pretrained models.')
    args = parser.parse_args()

    download_all_models(ask_for_permission=args.ask_for_permission)
