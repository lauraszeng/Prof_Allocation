document.addEventListener('DOMContentLoaded', () => {
    prof_info()
    assistant_info()
    drag_and_drop()
    drag_and_drop_mobile()
})

function drag_and_drop() {
    // create variables for items to be dragged and containers to house draggable items
    const draggables = document.querySelectorAll('.draggable')
    const containers = document.querySelectorAll('.container') 

    // when an item is clicked and dragged, classify it as being dragged. when the mouse lets go of the item, dismiss it from the dragged class.
    draggables.forEach(draggable => {
        draggable.addEventListener("dragstart", () => {
            draggable.classList.add('dragging')
        })
        draggable.addEventListener('dragend', () => {
            draggable.classList.remove('dragging')
        })
    })

    // when a draggable item is dragged over a container, append it to the container
    containers.forEach(container => {
        container.addEventListener('dragover', () => {
            const draggable = document.querySelector('.dragging')
            container.appendChild(draggable)
        })
    })   
}

// this calculates how many total credits a prof has
function prof_info() {
    // get all cards with professor information
    const prof_cards = document.querySelectorAll(".prof")

    // iterate through professor cards
    prof_cards.forEach(prof_card => {
        // get prof id
        let prof_id = prof_card.id
        // use fetch api to get prof details
        fetch(`professor_json/${prof_id}`)
        .then(response => response.json())
        .then(professor => {
            // get sum of course credits
            total_credits = 0;
            courses = professor.course_credits
            //iterate through all course credits and sum
            for (course in courses) {
                total_credits += (courses[course])
            }
            prof_card.innerHTML += `Total Credits: ${total_credits}`
        })
    })
}

function assistant_info() {
    // get all cards with assistant information
    const assistant_cards = document.querySelectorAll(".assistant")

    //iterate through assistant cards
    assistant_cards.forEach(assistant_card => {
        // get assistant id
        let assistant_id = assistant_card.id
        attach_profs(assistant_id)
    })
}

function attach_profs(assistant_id) {
    fetch(`assistant_json/${assistant_id}`)
    .then(response => response.json())
    .then(assistant => {
        professor_list = assistant.professors
        for (professor in professor_list) {
            console.log(assistant)
            search_prof(professor)
            console.log(professor_list[professor])
        }
    })
}

function search_prof(professor_id) {
    fetch(`professor_json/${professor_id}`)
    .then(response => response.json())
    .then(professor => {
        console.log("hi")
    })
}