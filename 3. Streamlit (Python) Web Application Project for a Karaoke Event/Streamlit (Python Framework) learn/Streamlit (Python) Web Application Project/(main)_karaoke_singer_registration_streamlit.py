#Idea of this Streamlit (Python) Webb Application Karaoke Event is to create 3 seperate files:
#1. First is a streamlit app to get user input for their song choice and to indicate interest to add to queue 
#   ('(main)_karaoke_singer_registration_streamlit.py')
#2. Second in a database to load their inputs into ('database.csv')
#3. Third is a streamlit app that displays the queue on the karaoke projector screen in a graphing/figure format
#   ('(main)_song_queue_streamlit.py')

#This is app '#1. First is a streamlit app to get user input for their song choice and to indicate interest to add 
#to queue'
import streamlit as st
import pandas as pd
from karaoke_singer_class import KaraokeSinger


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

st.image(image="karaoke_poster.jpg", width=680)
st.header("🎶 Add Your Name and Your Song Choice! 🎶")

#There are some 'st.session_state' stuffs (pretty complicated stuff tbh) but its needed for the confirmation function 
#to work (Youtube link about it here: https://www.youtube.com/watch?v=92jUAXBmZyU). Uncomment the below code to see the
#'st.session_state' for each of the button widget's session states
# "st.session_state object:", st.session_state
st.session_state["Button2"] = False

name = st.text_input("Name: ")
song_choice = st.text_input("Song choice: ")

button_state = st.button(label="Submit", key="button1")


if button_state:
    if name == "" or song_choice == "":
        st.warning("Please fill up all the above fields!")
    else:
        #Confirm submission:
        st.write("Confirm?")
        st.write("Name: ", name)
        st.write("Song choice: ", song_choice)

        button_state2 = st.button(label="Confirm Submit", key="button2")
        if button_state2:
            st.session_state["button2"] = True

        #Not confirm submission:
        button_state3 = st.button(label="Back", key="button3")
        if button_state3:
            pass


#Uploading the 'KaraokeSinger''s name and song choice into the 'database_array'
if "button2" in st.session_state:
    if st.session_state["button2"] == True:
        database_array.append(KaraokeSinger(name, song_choice))
        print(database_array)

        # #Reupdating the database from 'database_array' to 'database'...

        # #Converting each 'KaraokeSinger' object in the 'database_array' into a dictionary, then appending them back into 
        # #the 'updated_database' DataFrame
        updated_database = pd.DataFrame([x.as_dict() for x in database_array])
        print(updated_database)
        updated_database.to_csv('database.csv', index=False)

        st.success("You have been added to the song queue! It might take some time for your name to appear on the screen. Please give others a chance before adding yourself to the song queue again!")


#DONEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
 
#To be improved areas:
#- maybe can say how many people left before the user in the queue
#- automatically dequeue the top singer in the queue after they have finished their song during the Karaoke Evenet