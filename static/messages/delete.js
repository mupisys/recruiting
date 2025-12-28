document.addEventListener('alpine:init', () => {
    Alpine.data('messageDelete', (id) => ({
        isLoading: false,
        subject: 'Carregando...',
        
        async init() {
            try {
                const response = await fetch(`/api/messages/${id}/`);
                if (response.ok) {
                    const data = await response.json();
                    this.subject = data.subject;
                }
            } catch (e) {
                this.subject = 'Erro ao carregar';
            }
        },

        async confirmDelete() {
            this.isLoading = true;
            try {
                const response = await fetch(`/api/messages/${id}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });
                
                if (response.ok) {
                    window.location.href = '/messages/';
                } else {
                    alert('Erro ao excluir mensagem.');
                }
            } catch (error) {
                console.error('Erro:', error);
                alert('Erro ao excluir mensagem.');
            } finally {
                this.isLoading = false;
            }
        }
    }));
});
