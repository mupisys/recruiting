function tarefasApp() {
    return {
        tarefas: [],
        novaTarefa: '',
        adicionarTarefa() {
            if(this.novaTarefa.trim() === '') return;
            this.tarefas.push({
                id: Date.now(),
                texto: this.novaTarefa,
                feito: false
            });
            this.novaTarefa = '';
        }
    }
}
