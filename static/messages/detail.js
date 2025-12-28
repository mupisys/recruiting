document.addEventListener('alpine:init', () => {
    Alpine.data('messageDetail', (id, currentUser) => ({
        message: null,
        isLoading: true,
        currentUser: currentUser,
        
        init() {
            this.fetchMessage(id);
        },

        async fetchMessage(id) {
            try {
                const response = await fetch(`/api/messages/${id}/`);
                if (!response.ok) throw new Error('Erro ao carregar mensagem');
                this.message = await response.json();
            } catch (error) {
                console.error('Erro:', error);
                alert('Erro ao carregar mensagem.');
                window.location.href = '/messages/';
            } finally {
                this.isLoading = false;
            }
        },
        
        formatDate(dateString) {
            return dayjs(dateString).format('DD MMM YYYY, HH:mm');
        },
        
        getInitial(name) {
            return name ? name.charAt(0).toUpperCase() : '?';
        },

        get canEdit() {
            return this.message && this.message.sender === this.currentUser;
        },

        reply() {
            if (!this.message) return;
            
            const recipient = this.message.sender === this.currentUser ? this.message.recipient : this.message.sender;
            const subject = this.message.subject.startsWith('Re:') ? this.message.subject : `Re: ${this.message.subject}`;
            
            window.location.href = `/messages/new/?recipient=${recipient}&subject=${encodeURIComponent(subject)}`;
        }
    }));
});
