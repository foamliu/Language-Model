# coding: utf-8
import argparse
import time
import math
import os
import torch
import torch.nn as nn
import torch.onnx

import data
import model

device = torch.device("cuda" if args.cuda else "cpu")