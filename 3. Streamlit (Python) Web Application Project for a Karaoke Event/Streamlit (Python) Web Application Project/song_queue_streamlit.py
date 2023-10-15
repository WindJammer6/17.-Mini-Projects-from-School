#Idea is to create 3 seperate apps
#1. first is a streamlit app to get user input for their song choice and to indicate interest to add to queue 
#   ('karaoke_singer_registration_streamlit.py')
#2. second in a database to load their inputs into ('database.csv')
#3. third is the streamlit app that displays the queue on the karaoke projector screen in a graphing/figure format
#   ('song_queue_streamlit.py')

#This is app '3. third is the streamlit app that displays the queue on the karaoke projector screen in a 
#graphing/figure format'
import streamlit as st
import pandas as pd
from zqueue_data_structure import Queue
from zkaraoke_singer_class import KaraokeSinger



#Backend side of things... 
database = pd.read_csv("database.csv")
print(database)

queue = Queue()

#Loading the csv file contents into the Queue Data Structure, enqueueing the person at the top of the database first (to 
#show that he will be the next singer)
for index, row in database.iterrows():
    user = KaraokeSinger(row['name'], row['song_choice'])
    queue.enqueue(user)
print(queue)


#///////////////////////////////////////////////////////////////////////////////////////////////


#(Frontend) Streamlit (Python) of things...
st.header("Song Queue:")

column1, column2 = st.columns(2)

with column1:
    st.write("### Name")
    for i in reversed(queue.buffer):
        st.write(i.name)

with column2:
    st.write("### Song choice")
    for i in reversed(queue.buffer):
        st.write(i.song_choice)



#Only issue is how to automate when to remove a person from the queue when their song is done? (How do dequeue is easy,
#problem is just when to do it)