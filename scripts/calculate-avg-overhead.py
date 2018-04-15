#!/usr/bin/python3
"""
# Copyright (c) 2018, Peter Nirschl
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import re
import sys

DATA_PATH = "../plots/crypto-comparison/median/"

def parse_file( path, resultset ):
    with open(path,'r') as f:
        line = f.readline()
        parts = line.split(' ')
        resultset[parts[0]] = parts[1]
    f.close()

def main():
    none = {}
    botan = {}
    openssl = {}
    gcrypt = {}
    fcrypt = {}

    parse_file(DATA_PATH + "get_crypto_botan.dat", botan)
    parse_file(DATA_PATH + "get_crypto_openssl.dat", openssl)
    parse_file(DATA_PATH + "get_crypto_gcrypt.dat", gcrypt)
    parse_file(DATA_PATH + "get_no_crypto_plugin.dat", none)

if __name__ == "__main__":
    main()

