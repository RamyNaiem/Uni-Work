const createBox = document.getElementsByClassName("createBox")[0];
const notes = document.getElementsByClassName("notes")[0];
let contentArray = localStorage.getItem("items")
  ? JSON.parse(localStorage.getItem("items"))
  : [];

var i = 0;

contentArray.forEach(divMaker);

function divMaker(noteObj) {
  var div = document.createElement("div");
  div.setAttribute("noteId", noteObj.noteId);
  var h1 = document.createElement("h1");

  const deleteBtn = document.createElement("button");
  deleteBtn.setAttribute("class", "hidden");
  deleteBtn.setAttribute("name", "delete");
  deleteBtn.textContent = "delete";
  h1.textContent = noteObj.text;

  div.className = "note";
  div.setAttribute("style","margin:" + margin() + "; background:" + color() + "");
  div.appendChild(deleteBtn);
  div.appendChild(h1);
  notes.appendChild(div);


}

function addNote() {
  const input = document.getElementById("user-input");
  const noteId = getUniqueId();
  const noteObj = { noteId: noteId, text: input.value };
  contentArray.push(noteObj);
  localStorage.setItem("items", JSON.stringify(contentArray));
  divMaker(noteObj);
  input.value = "";
}

function createNote() {
  if (createBox.style.display === "none") createBox.style.display = "block";
  else createBox.style.display = "none";
}

function deletenotes() {
  localStorage.clear();
  notes.innerHTML = "";
  contentArray = [];
}

function margin() {
  var random_margin = ["10px"];
  return random_margin;
}

function color() {
  var random_colors = ["lightblue","lightgreen","red","lightgreen","violet",];

  if (i > random_colors.length - 1) {
    i = 0;
  }
  return random_colors[i++];
}

createBox.addEventListener("keydown", function (event) {
  if (event.key === "Enter") addNote();
});



function getUniqueId() {
  return Date.now().toString(36) + Math.random().toString(36).substr(2);
}

//-----selecting a .note
//-----it toggle delete btn when you click inside or outside the .notes element
notes.addEventListener("click", function (event) {
  const noteElement = event.target.closest(".note");
  if (noteElement !== null) {
    const buttons = noteElement.querySelectorAll("button");
    buttons.forEach(function (btn) {
      btn.classList.remove("hidden");
    });
  } else {
    document.querySelectorAll(".note button").forEach(function (btn) {
      btn.classList.add("hidden");
    });
  }
});

//----- deleting a .note element
notes.addEventListener("click", function (event) {
  if (event.target.tagName === "BUTTON") {
    const noteElement = event.target.closest(".note");
    const noteId = noteElement.getAttribute("noteId");
    console.log(noteId);
    //remove item from localStorage
    contentArray = contentArray.filter(x => x.noteId !== noteId);
    localStorage.setItem("items", JSON.stringify(contentArray));
    //remove note element
    noteElement.remove();
  }
});
