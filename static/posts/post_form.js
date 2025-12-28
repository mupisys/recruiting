function postForm() {
    return {
        formData: {
            title: '',
            category_id: '',
            content: '',
            image: null,
            video: null
        },
        categories: [],
        loading: false,

        async init() {
            try {
                this.categories = await Utils.fetchJSON('/api/categories/');
            } catch (e) {
                console.error('Categories error:', e);
            }
        },

        handleFileChange(event, field) {
            this.formData[field] = event.target.files[0];
        },

        async submitPost() {
            this.loading = true;
            const data = new FormData();
            Object.entries(this.formData).forEach(([key, value]) => {
                if (value) data.append(key, value);
            });

            try {
                await Utils.fetchJSON('/api/posts/', {
                    method: 'POST',
                    body: data
                });
                Utils.showToast('success', 'Post criado com sucesso!');
                setTimeout(() => window.location.href = '/', 1500);
            } catch (e) {
                Utils.showError('Erro ao criar post: ' + e.message);
            } finally {
                this.loading = false;
            }
        }
    }
}
