#Idea is to create 3 seperate apps
#1. first is a streamlit app to get user input for their song choice and to indicate interest to add to queue 
#   ('karaoke_singer_registration_streamlit.py')
#2. second in a database to load their inputs into ('database.csv')
#3. third is the streamlit app that displays the queue on the karaoke projector screen in a graphing/figure format
#   ('song_queue_streamlit.py')

#This is app '#1. first is a streamlit app to get user input for their song choice and to indicate interest to add 
#to queue'
import streamlit as st
import pandas as pd
from zkaraoke_singer_class import KaraokeSinger


#Backend side of things...
database = pd.read_csv("database.csv")
print(database)

database_array = []

#Loading the csv file contents into an Array, to make manipulation of the database easier (such as when you want to
#append a new 'KaraokeSinger')
for index, row in database.iterrows():
    user = KaraokeSinger(row['name'], row['song_choice'])
    database_array.append(user)
print(database_array)


#/////////////////////////////////////////////////////////////////////////


#(Frontend) Streamlit (Python) app side of things...
st.header("Fill up this form to add yourself to the karaoke queue!")
st.image(image="karaoke_poster.jpg")

with st.form(key="Form 1"):
    name = st.text_input(label="Name")
    song_choice = st.text_input(label="Song you want to sing")

    submit_button_state = st.form_submit_button(label="Submit")

    if submit_button_state:
        if name == "" or song_choice == "":
            st.warning("Please fill up all the above fields!")
        else:
            st.success("Submitted successfully!")

            #Uploading the 'KaraokeSinger''s name and song choice into the 'database_array'
            database_array.append(KaraokeSinger(name, song_choice))
            print(database_array)


#/////////////////////////////////////////////////////////////////////////


#Reupdating the database from 'database_array' to 'database'...

#Converting each 'KaraokeSinger' object in the 'database_array' into a dictionary, then appending them back into the 
#'updated_database' DataFrame
updated_database = pd.DataFrame([x.as_dict() for x in database_array])
print(updated_database)
updated_database.to_csv('database.csv', index=False)




#DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE