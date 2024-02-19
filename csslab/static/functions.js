the_heading = document.getElementById("heading");
name_input = document.getElementById("username");
color_input = document.getElementById("user-color")
paragraph1 = document.getElementById("paragraph1");
paragraph2 = document.getElementById("paragraph2");

the_heading.onclick = function() {
  the_heading.innerText = "Goodbye World!"
};


the_paragraph.onmouseenter = function() {
  the_paragraph.style.color = "blue";
  the_paragraph.style.backgroundColor = "white";
};

function changeColor() {
  text_input_element = document.getElementById("user-color");
  new_color = text_input_element.value;
  the_heading.style.color = new_color;
}

function toggleColor() {
  old_color = document.body.style.background;
  if (old_color == 'white') {
  	new_color = 'yellow';
  } else {
  	new_color = 'white';
  }
  document.body.style.background = new_color;
}

function randomSentence() {

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