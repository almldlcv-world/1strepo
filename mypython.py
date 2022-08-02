import streamlit as st
st.markdown('# 📝 **Transcriber App**')
bar = st.progress(0)

st.title('Counter Example')
count = 0

increment = st.button('Increment')
if increment:
    count += 1

st.write('Count = ', count)