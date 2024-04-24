# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import subprocess

def run_script(script_name):
    subprocess.run(["streamlit", "run", script_name])

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Cryptographic Application",
        page_icon="🔒",
    )
  
    st.write("Applied Cryptography - CSAC 329 || Final Project")
    st.write("# Cryptographic Application 🔒")
    st.write("By Group 2 - BSCS 3A || [VARGAS, Regine B., VIÑAS, Christian Joseph C., TUMANENG, Marc Christian D.]")
   
    
    st.sidebar.success("Select a cryptographic algorithm.")

    st.markdown(
        """
       
    """
    )
    st.write("---")

    st.write("## Symmetric Encryption")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Block Cipher"):
            run_script("🔒1_Block_Cipher.py")
    with col2:
        if st.button("Ceasar Cipher"):
            run_script("2_Ceasar_Cipher.py")
    with col3:
        if st.button("XOR Cipher"):
            run_script("3_XOR_Cipher.py")

    st.write("## Asymmetric Encryption")
    col4, col5 = st.columns(2)
    with col4:
        if st.button("Diffie-Hellman"):
            run_script("4_Diffie_Hellman.py")
    with col5:
        if st.button("RSA"):
            run_script("5_RSA.py")

    st.write("## Hashing")
    col6, col7, col8, col9 = st.columns(4)
    with col6:
        if st.button("SHA-1"):
            run_script("6_SHA_1.py")
    with col7:
        if st.button("SHA-2"):
            run_script("7_SHA_2.py")
    with col8:
        if st.button("SHA-3"):
            run_script("8_SHA_3.py")
    with col9:
        if st.button("MD5"):
            run_script("9_MD_5.py")
   


if __name__ == "__main__":
    run()
