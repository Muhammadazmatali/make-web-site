import streamlit as st
import pandas as pd
st.title("How to create a website using Python")
st.header("Today we learn who is make a web site with python ")
email = st.text_input("Enter your Email:")
password = st.text_input("Enter your password:")
Name = st.text_input("Enter your name:")
addres = st.text_area("Enter your Addres:")
button = st.button("Done")

if button :
    st.markdown(f"""
    Email : {email}
    password : {password}
    name : {Name}
    addres : {addres}
""")
st.subheader("Lets go!")
st.subheader("Introduction of python")
st.markdown("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.")
st.subheader("Introduction of streamlit")
st.markdown("treamlit is an open-source framework that allows data scientists and developers to quickly create interactive data-driven applications without the need for advanced web development skills.")
st.markdown("First we dowland streamlit")
st.code("$ pip install streamlit")
st.markdown("when streamlit dowland so, we make a web page and run our programme")
st.code("$ import streamlit as st")
st.markdown("How to write a title?")
st.code("""$ st.title("Hello world!")""")
st.image("title.png")
st.write("now we are learn some subheadrs and markdown and write")
st.subheader("Streamlit subheader")
st.write("Definition of subheader is: A heading is a main title, and a subheading is the text below that adds information about the headline, or that sets apart sections of an article or book")
st.subheader("Streamlit markdown")
st.write("Definition of markdown is : markdown function, which takes a string argument containing the Markdown-formatted text.")
st.subheader("Streamlit write")
st.write("Definition of write is :This function is used to add anything to a web app, from formatted string to charts in matplotlib figure, Altair charts, plotly figure, data frame, Keras model, and others.")
st.markdown("and for italked in write:")
st.code("""$ st.title("Hello * world *)""")
st.markdown("now we are show a video on the desktop!")
st.code("""st.video("streamlit.webm")""")
st.video("streamlit.webm")
st.markdown("now we are show a .csv file in our web site page")
st.code("""dataset = pd.read_csv("python1.csv")
st.dataframe(dataset)""")
st.image("Image.png")
st.markdown("so friends, now we are learn how is make a table which we ask people your personall information")
st.code("""email = st.text_input("Enter your Email:")
password = st.text_input("Enter your password:")
Name = st.text_input("Enter your name:")
addres = st.text_area("Enter your Addres:")""")
st.write("If you want your information is show in your web site page.")
st.code(st.markdown(f"""
    Email : {email}
    password : {password}
    name : {Name}
    addres : {addres}
"""))
st.code('$ button = st.button("Done")')
st.code('if button:')
st.image("pp.png")