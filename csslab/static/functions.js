the_heading = document.getElementById("heading");

function editHeading() {
  the_heading.innerText = "Goodbye World!"
}

function editParagraph1() {
  paragraph1 = document.getElementById("paragraph1");
  paragraph1.style.color = "blue";
  paragraph1.style.backgroundColor = "white";
}

function changeColor() {
  text_input_element = document.getElementById("user-color");
  new_color = text_input_element.value;
  the_heading.style.color = new_color;
}

function toggleColor() {
  old_color = document.body.style.background;
  if (old_color == 'white' || old_color == '') {
  	new_color = 'yellow';
  } else {
  	new_color = 'white';
  }
  document.body.style.background = new_color;
}

function randomSentence() {
	name_input = document.getElementById("username");
  paragraph2 = document.getElementById("paragraph2");
  if (name_input.value != 0) {
  	paragraph2.innerHTML = 'Hello, ' + name_input.value + '! Go to bed.';
	} else {
  	paragraph2.innerHTML = 'Please input a name.'
  }
}

function randomNumber() {
  button = document.getElementById("randomNumber");
  button.innerHTML = Math.floor((Math.random() * 100000) + 1);
}