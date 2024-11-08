# Project 5: Professor Allocation

## Purpose

I currently work as a Faculty Assistant at Harvard Law School (HLS). In addition to permanent faculty, HLS receives a number of visiting professors and lecturers each semester. These temporary faculty have to be divided among the faculty assistants, which is currently done via Excel, which is incredibly clunky. I created this project in order to better visualize the process in order to make this process easier.

## Pages

**Models.py**

I've created three models to be used for this app-- Professor, Course, and Assistant. Each professor can teach multiple courses. I've chosen a ManytoMany model for the courses since some courses are taught by multiple professors.

Each course has a credit number associated with it.

Each assistant can work with multiple professors.

**Forms.py**

I've created ModelForms for each model to allow submission of new entries to each model

**Views.py**

index is used to provide the necessary info to fill in the template for both layout.html and index.html. The database info is used to populate the cards in the sidebar in layout.html as well as the containers representing each assistant.

professor_json, course_json, and assistant_json are all used to turn model information from Professor, Assistant, and Course into json data that can be retrieved via a fetch API.

add_prof, add_course, and add_assistant are respectively linked to add_prof.html ,add_course.html, and add_assistant.html, and are used to submit form data to create new entries in these models

**Script.js**

drag_and_drop allows for drag and drop functionality. Whenever something with the class attribute "draggable" starts getting dragged, the class attribute "dragging" added to it. When it stops getting dragged, the "dragging" attribute is removed. Containers, that is things with the class attribute "container", will have things with the class attribute "dragging" appended to them when the draggable item it dragged over the container.

prof_info uses fetch api to retrieve information about the courses a professor teaches. It goes through all courses and sums up the cumulative credit amounts (which is something accessed through JSON property "professor.course_credits"), then appends that sum to the professor's card.

ideally, i would have liked to have updated each assistant's model information with each added professor draggable added to the assistant's container, but I wasn't able to figure out how to do this. I intended to use a fetch api inside of a fetch api, but this didn't seem to work. You can see my attempts to do this in assistant_info, in which I iterate through each assistant card, attach_profs, in which I locate the professors associated with each assistant associated with their corresponding assistant card, and search_prof, in which I use the fetch api to retrieve prof data.
