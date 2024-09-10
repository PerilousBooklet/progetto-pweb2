var codice = "";
var provincia = "";
var nome = "";

document.addEventListener("DOMContentLoaded", function () {
	console.log("ciao2");
	//edit row
	$(".rs-row").click(function () {
		console.log("ciao");
		// console.log($(this));

		codice = this.childNodes[1].childNodes[0].textContent;
		console.log(codice);
		provincia = this.childNodes[3].childNodes[0].textContent;
		nome = this.childNodes[5].childNodes[0].textContent;

		// console.log(codice + " " + provincia + " " + nome);

		$("#fakeCodiceModal")[0].value = codice;
		$("#id_codiceModalEdit")[0].value = codice; //Codice
		$("#id_provinciaModalEdit")[0].value = provincia; //Provincia
		$("#id_nomeModalEdit")[0].value = nome; //Nome

		$("#id_codiceModalDelete")[0].value = codice; //Codice
		$("#id_provinciaModalDelete")[0].value = provincia; //Provincia
		$("#id_nomeModalDelete")[0].value = nome; //Nome

		//nel caso fare un for
	});
});
