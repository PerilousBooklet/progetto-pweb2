var codice = "";
var provincia = "";
var nome = "";

document.addEventListener("DOMContentLoaded", function () {
	//edit row
	$(".rs-row").click(function () {
		// console.log($(this));

		codice = this.childNodes[1].childNodes[0].textContent;
		provincia = this.childNodes[3].childNodes[0].textContent;
		nome = this.childNodes[5].childNodes[0].textContent;

		// console.log(codice + " " + provincia + " " + nome);

		$("#fakeCodiceModal")[0].value = codice;

		$("#id_codiceModal")[0].value = codice; //Codice
		$("#id_provinciaModal")[0].value = provincia; //Provincia
		$("#id_nomeModal")[0].value = nome; //Nome

		//nel caso fare un for
	});
});
