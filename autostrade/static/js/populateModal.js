//richiamata al click dei pulsanti di modifica e di eliminazione.
//copia i valori della riga corrente e li inserisce nella form del dialog che compare.
function populateRowModal(codice, provincia, nome) {

	$("#fakeCodiceModal")[0].value = codice;
	$("#id_codiceModalEdit")[0].value = codice;
	$("#id_provinciaModalEdit")[0].value = provincia;
	$("#id_nomeModalEdit")[0].value = nome;

	$("#id_codiceModalDelete")[0].value = codice;
	$("#id_provinciaModalDelete")[0].value = provincia;
	$("#id_nomeModalDelete")[0].value = nome;

	$("#fakeCodiceModalDelete")[0].value = codice;
	$("#fakeProvinciaModalDelete")[0].value = provincia;
	$("#fakeNomeModalDelete")[0].value = nome;
}

//richiamata al click del pulsante inserisci nella pagina Comune.
//copia i campi dei filtri e li mette nella form di inserimento.
function populateInsertModal() {
	$("#id_codiceModalInsert")[0].value = $("#id_codice")[0].value;
	$("#id_provinciaModalInsert")[0].value = $("#id_provincia")[0].value;
	$("#id_nomeModalInsert")[0].value = $("#id_nome")[0].value;
}
