document.addEventListener('alpine:init', () => {
    Alpine.data('messageList', () => ({
        messages: [],
        isLoading: true,
        
        init() {
            this.fetchMessages();
        },

        async fetchMessages() {
            this.isLoading = true;
            try {
                const response = await fetch('/api/messages/');
                if (!response.ok) throw new Error('Erro ao carregar mensagens');
                this.messages = await response.json();
            } catch (error) {
                console.error('Erro:', error);
            } finally {
                this.isLoading = false;
            }
        },

        formatDate(dateString) {
            return dayjs(dateString).format('DD/MM/YYYY');
        },

        getDetailUrl(username) {
            return `/messages/u/${username}/`;
        }
    }));
});
