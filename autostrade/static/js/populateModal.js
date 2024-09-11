function populateModal(codice, provincia, nome) {
	// console.log(codice + " " + provincia + " " + nome);

	$("#fakeCodiceModal")[0].value = codice;
	$("#id_codiceModalEdit")[0].value = codice; //Codice
	$("#id_provinciaModalEdit")[0].value = provincia; //Provincia
	$("#id_nomeModalEdit")[0].value = nome; //Nome

	$("#id_codiceModalDelete")[0].value = codice; //Codice
	$("#id_provinciaModalDelete")[0].value = provincia; //Provincia
	$("#id_nomeModalDelete")[0].value = nome; //Nome

	$("#fakeCodiceModalDelete")[0].value = codice; //Codice
	$("#fakeProvinciaModalDelete")[0].value = provincia; //Provincia
	$("#fakeNomeModalDelete")[0].value = nome; //Nome
}
