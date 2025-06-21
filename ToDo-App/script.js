function addTask(taskCounter) {
    let taskName = document.getElementById("task").value;

    let taskToadd = document.createElement("span")
    taskToadd.classList.add("taskInList")
    taskToadd.innerHTML = `${taskName} <input type="checkbox" onclick="removeTask()">`

    document.querySelector(".task-list").append(taskToadd)
}

function removeTask(){
    let task = document.querySelector(".taskInList")
    
}

const taskCounter = 0