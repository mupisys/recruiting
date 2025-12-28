document.addEventListener('alpine:init', () => {
    Alpine.data('conversationDetail', (partnerUsername, currentUser) => ({
        messages: [],
        isLoading: true,
        isSending: false,
        currentUser: currentUser,
        partnerName: partnerUsername,
        newMessage: '',
        
        init() {
            this.fetchMessages();
            setInterval(() => this.fetchMessages(false), 10000);
        },

        async fetchMessages(showLoading = true) {
            if (showLoading) this.isLoading = true;
            try {
                const response = await fetch(`/api/messages/conversation/${partnerUsername}/`);
                if (!response.ok) throw new Error('Erro ao carregar mensagens');
                this.messages = await response.json();
                this.scrollToBottom();
            } catch (error) {
                console.error('Erro:', error);
            } finally {
                if (showLoading) this.isLoading = false;
            }
        },

        async sendMessage() {
            if (!this.newMessage.trim()) return;
            
            this.isSending = true;
            try {
                const response = await fetch('/api/messages/', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    },
                    body: JSON.stringify({
                        recipient: partnerUsername,
                        subject: 'Chat Message', 
                        body: this.newMessage
                    })
                });

                if (response.ok) {
                    this.newMessage = '';
                    await this.fetchMessages(false);
                } else {
                    alert('Erro ao enviar mensagem.');
                }
            } catch (error) {
                console.error('Erro:', error);
                alert('Erro ao enviar mensagem.');
            } finally {
                this.isSending = false;
            }
        },

        async deleteMessage(id) {
            if (!confirm('Tem certeza que deseja excluir esta mensagem?')) return;
            
            try {
                const response = await fetch(`/api/messages/${id}/`, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                });
                
                if (response.ok) {
                    await this.fetchMessages(false);
                } else {
                    alert('Erro ao excluir mensagem.');
                }
            } catch (error) {
                console.error('Erro:', error);
            }
        },
        
        formatDate(dateString) {
            return dayjs(dateString).format('DD/MM/YYYY HH:mm');
        },

        scrollToBottom() {
            this.$nextTick(() => {
                const container = document.getElementById('chat-messages');
                if (container) {
                    container.scrollTop = container.scrollHeight;
                }
            });
        }
    }));
});
