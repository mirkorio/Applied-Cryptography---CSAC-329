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
    st.write("---")
    st.markdown(
        """This Application implements various cryptographic techniques to secure communication,
          data, and information exchange. Cryptography is the science of encoding and decoding 
          messages to protect their confidentiality, integrity, and authenticity. The application
            provides a user-friendly interface that allows users to encrypt, decrypt and hash
              messages/file using different cryptographic algorithms.
    """
    )
    
   


if __name__ == "__main__":
    run()
