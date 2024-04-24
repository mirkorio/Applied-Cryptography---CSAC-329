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

     # Symmetric
    st.write("## Symmetric - table")
    if st.button("1_Block_Cipher.py"):
        st.markdown("[1_Block_Cipher.py](https://example.com/1_Block_Cipher.py)")
    if st.button("2_Ceasar_Cipher.py"):
        st.markdown("[2_Ceasar_Cipher.py](https://example.com/2_Ceasar_Cipher.py)")
    if st.button("3_XOR_Cipher.py"):
        st.markdown("[3_XOR_Cipher.py](https://example.com/3_XOR_Cipher.py)")

    # Asymmetric
    st.write("## Asymmetric - table")
    if st.button("4_Diffie_Hellman.py"):
        st.markdown("[4_Diffie_Hellman.py](https://example.com/4_Diffie_Hellman.py)")
    if st.button("5_RSA.py"):
        st.markdown("[5_RSA.py](https://example.com/5_RSA.py)")

    # Hashing
    st.write("## Hashing - table")
    if st.button("6_SHA_1.py"):
        st.markdown("[6_SHA_1.py](https://example.com/6_SHA_1.py)")
    if st.button("7_SHA_2.py"):
        st.markdown("[7_SHA_2.py](https://example.com/7_SHA_2.py)")
    if st.button("8_SHA_3.py"):
        st.markdown("[8_SHA_3.py](https://example.com/8_SHA_3.py)")
    if st.button("9_MD_5.py"):
        st.markdown("[9_MD_5.py](https://example.com/9_MD_5.py)")



if __name__ == "__main__":
    run()
