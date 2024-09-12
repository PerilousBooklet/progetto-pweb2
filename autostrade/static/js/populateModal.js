function populateRowModal(codice, provincia, nome) {
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

function populateInsertModal() {
	$("#id_codiceModalInsert")[0].value = $("#id_codice")[0].value;
	$("#id_provinciaModalInsert")[0].value = $("#id_provincia")[0].value;
	$("#id_nomeModalInsert")[0].value = $("#id_nome")[0].value;
}
