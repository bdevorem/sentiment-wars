//Breanna Devore-McDonald

document.getElementById("b1").onmouseup = changeText

var label = document.createElement("p");
label.setAttribute("id", "Label1");

var labeltext = document.createTextNode("Who?");
label.appendChild(labeltext);
document.body.appendChild(label);

function changeText(){
	//var label2 = document.createElement("p");
	//label2.setAttribute("id", "NewLabel");

	//var labeltext2 = document.createTextNode("Breanna McDonald");
	//label.appendChild(labeltext2);
	//document.body.appendChild(label2);
	//document.body.removeChild(label);
	label.textContent = "Breanna McDonald";

}
