function aggiorna_somma_sending() {
	var somma_sending = 0;
	
	for (i = 1; i <= 6; i++) {
		var corso_scelto = document.getElementById("course_selected_sending_" + i).value;
		if (corso_scelto == "---") {
			continue;
		}
		if (corso_scelto == "free") {
			var ects = parseFloat(document.getElementById("input_sending_" + i).value);
			somma_sending = somma_sending + ects;
		}
		else {
			var ects = parseFloat(document.getElementById("ects_course_selected_sending_" + i).textContent);
			somma_sending = somma_sending + ects;
		}
	}
	document.getElementById("somma_ects_sending").innerHTML = "Sending ECTS sum: " + somma_sending;
	
	verificaSomme()
}

function aggiorna_somma_receiving() {
	var somma_receiving = 0;
	
	for (i = 1; i <= 6; i++) {
		var corso_scelto = document.getElementById("course_selected_receiving_" + i).value;
		if (corso_scelto == "---") {
			continue;
		}
		if (corso_scelto == "free") {
			var ects = parseFloat(document.getElementById("input_receiving_" + i).value);
			somma_receiving = somma_receiving + ects;
		}
		else {
			var ects = parseFloat(document.getElementById("ects_course_selected_receiving_" + i).textContent);
			somma_receiving = somma_receiving + ects;
		}
	}
	document.getElementById("somma_ects_receiving").innerHTML = "Receiving ECTS sum: " + somma_receiving;
	
	verificaSomme()
}

function rileva_corso_sending_1() {
	var corso_scelto = document.getElementById("course_selected_sending_1").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_sending_1").innerHTML = "<input id = 'input_sending_1' type = 'number' step = '0.5' onchange = 'aggiorna_somma_sending()' />";
	}
	else {
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_sending_1").innerHTML = ects_numero;
	}
	
	aggiorna_somma_sending()
}

function rileva_corso_receiving_1() {
	var corso_scelto = document.getElementById("course_selected_receiving_1").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_receiving_1").innerHTML = "<input id = 'input_receiving_1' type = 'number' step = '0.5' onchange = 'aggiorna_somma_receiving()' />";
	}
	else {
		var corso_scelto = document.getElementById("course_selected_receiving_1").value;
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_receiving_1").innerHTML = ects_numero;
	}
	
	aggiorna_somma_receiving()
}

function rileva_corso_sending_2() {
	var corso_scelto = document.getElementById("course_selected_sending_2").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_sending_2").innerHTML = "<input id = 'input_sending_2' type = 'number' step = '0.5' onchange = 'aggiorna_somma_sending()' />";
	}
	else {
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_sending_2").innerHTML = ects_numero;
	}
	
	aggiorna_somma_sending()
}

function rileva_corso_receiving_2() {
	var corso_scelto = document.getElementById("course_selected_receiving_2").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_receiving_2").innerHTML = "<input id = 'input_receiving_2' type = 'number' step = '0.5' onchange = 'aggiorna_somma_receiving()' />";
	}
	else {
		var corso_scelto = document.getElementById("course_selected_receiving_2").value;
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_receiving_2").innerHTML = ects_numero;
	}
	
	aggiorna_somma_receiving()
}

function rileva_corso_sending_3() {
	var corso_scelto = document.getElementById("course_selected_sending_3").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_sending_3").innerHTML = "<input id = 'input_sending_3' type = 'number' step = '0.5' onchange = 'aggiorna_somma_sending()' />";
	}
	else {
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_sending_3").innerHTML = ects_numero;
	}
	
	aggiorna_somma_sending()
}

function rileva_corso_receiving_3() {
	var corso_scelto = document.getElementById("course_selected_receiving_3").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_receiving_3").innerHTML = "<input id = 'input_receiving_3' type = 'number' step = '0.5' onchange = 'aggiorna_somma_receiving()' />";
	}
	else {
		var corso_scelto = document.getElementById("course_selected_receiving_3").value;
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_receiving_3").innerHTML = ects_numero;
	}
	
	aggiorna_somma_receiving()
}

function rileva_corso_sending_4() {
	var corso_scelto = document.getElementById("course_selected_sending_4").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_sending_4").innerHTML = "<input id = 'input_sending_4' type = 'number' step = '0.5' onchange = 'aggiorna_somma_sending()' />";
	}
	else {
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_sending_4").innerHTML = ects_numero;
	}
	
	aggiorna_somma_sending()
}

function rileva_corso_receiving_4() {
	var corso_scelto = document.getElementById("course_selected_receiving_4").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_receiving_4").innerHTML = "<input id = 'input_receiving_4' type = 'number' step = '0.5' onchange = 'aggiorna_somma_receiving()' />";
	}
	else {
		var corso_scelto = document.getElementById("course_selected_receiving_4").value;
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_receiving_4").innerHTML = ects_numero;
	}
	
	aggiorna_somma_receiving()
}

function rileva_corso_sending_5() {
	var corso_scelto = document.getElementById("course_selected_sending_5").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_sending_5").innerHTML = "<input id = 'input_sending_5' type = 'number' step = '0.5' onchange = 'aggiorna_somma_sending()' />";
	}
	else {
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_sending_5").innerHTML = ects_numero;
	}
	
	aggiorna_somma_sending()
}

function rileva_corso_receiving_5() {
	var corso_scelto = document.getElementById("course_selected_receiving_5").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_receiving_5").innerHTML = "<input id = 'input_receiving_5' type = 'number' step = '0.5' onchange = 'aggiorna_somma_receiving()' />";
	}
	else {
		var corso_scelto = document.getElementById("course_selected_receiving_5").value;
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_receiving_5").innerHTML = ects_numero;
	}
	
	aggiorna_somma_receiving()
}

function rileva_corso_sending_6() {
	var corso_scelto = document.getElementById("course_selected_sending_6").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_sending_6").innerHTML = "<input id = 'input_sending_6' type = 'number' step = '0.5' onchange = 'aggiorna_somma_sending()' />";
	}
	else {
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_sending_6").innerHTML = ects_numero;
	}
	
	aggiorna_somma_sending()
}

function rileva_corso_receiving_6() {
	var corso_scelto = document.getElementById("course_selected_receiving_6").value;
	
	if (corso_scelto == "free") {
		document.getElementById("ects_course_selected_receiving_6").innerHTML = "<input id = 'input_receiving_6' type = 'number' step = '0.5' onchange = 'aggiorna_somma_receiving()' />";
	}
	else {
		var corso_scelto = document.getElementById("course_selected_receiving_6").value;
		var ects_corso_scelto = corso_scelto.split("-")[1];
		var ects_numero = parseFloat(ects_corso_scelto.split(" ")[1]);
		document.getElementById("ects_course_selected_receiving_6").innerHTML = ects_numero;
	}
	
	aggiorna_somma_receiving()
}

function verificaSomme() {
	var sommaSending = parseFloat(document.getElementById("somma_ects_sending").textContent.split(":")[1]);
	var sommaReceiving = parseFloat(document.getElementById("somma_ects_receiving").textContent.split(":")[1]);
	
	if (Math.abs(sommaSending - sommaReceiving) > 0.5) {
		document.getElementById("messaggio_errore").innerHTML = "The difference between the two ECTS sums can be at most 0.5.";
	}
	else {
		document.getElementById("messaggio_errore").innerHTML = "&nbsp;";
	}
}
