document.addEventListener('alpine:init', () => {
    Alpine.data('messageForm', (messageId = null) => ({
        formData: {
            recipient: '',
            subject: '',
            body: ''
        },
        search: '',
        results: [],
        showResults: false,
        isLoading: false,
        errors: {},
        
        async init() {
            if (messageId) {
                await this.fetchMessage(messageId);
            } else {
                // Check for query params
                const urlParams = new URLSearchParams(window.location.search);
                const recipient = urlParams.get('recipient');
                const subject = urlParams.get('subject');
                
                if (recipient) {
                    this.formData.recipient = recipient;
                    this.search = recipient;
                }
                if (subject) {
                    this.formData.subject = subject;
                }
            }
            
            this.$watch('search', value => {
                this.formData.recipient = value;
            });
        },

        async fetchMessage(id) {
            this.isLoading = true;
            try {
                const response = await fetch(`/api/messages/${id}/`);
                if (response.ok) {
                    const data = await response.json();
                    this.formData = {
                        recipient: data.recipient,
                        subject: data.subject,
                        body: data.body
                    };
                    this.search = data.recipient;
                }
            } catch (error) {
                console.error('Erro:', error);
            } finally {
                this.isLoading = false;
            }
        },

        async fetchUsers() {
            if (this.search.length < 1) {
                this.results = [];
                this.showResults = false;
                return;
            }
            try {
                const response = await fetch(`/api/users/search/?q=${this.search}`);
                this.results = await response.json();
                this.showResults = true;
            } catch (error) {
                console.error('Erro:', error);
            }
        },

        selectUser(username) {
            this.search = username;
            this.showResults = false;
        },

        async submit() {
            this.isLoading = true;
            this.errors = {};
            
            const url = messageId ? `/api/messages/${messageId}/` : '/api/messages/';
            const method = messageId ? 'PUT' : 'POST';
            
            try {
                const response = await fetch(url, {
                    method: method,
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    },
                    body: JSON.stringify(this.formData)
                });

                if (response.ok) {
                    window.location.href = `/messages/u/${this.formData.recipient}/`;
                } else {
                    const data = await response.json();
                    this.errors = data;
                }
            } catch (error) {
                console.error('Erro:', error);
                alert('Ocorreu um erro ao salvar a mensagem.');
            } finally {
                this.isLoading = false;
            }
        }
    }));
});
