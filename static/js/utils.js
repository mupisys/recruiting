const Utils = {
    getCookie(name) {
        if (!document.cookie) return null;
        const cookie = document.cookie.split(';').find(c => c.trim().startsWith(name + '='));
        return cookie ? decodeURIComponent(cookie.trim().split('=')[1]) : null;
    },

    async fetchJSON(url, options = {}) {
        const headers = {
            'X-CSRFToken': this.getCookie('csrftoken'),
            ...options.headers
        };
        
        if (!(options.body instanceof FormData) && !headers['Content-Type']) {
            headers['Content-Type'] = 'application/json';
        }
        
        if (options.body instanceof FormData) {
            delete headers['Content-Type'];
        }

        try {
            const response = await fetch(url, { ...options, headers });
            
            if (response.status === 401 || response.status === 403) {
                await Swal.fire({
                    icon: 'warning',
                    title: 'Login Necessário',
                    text: 'Você precisa estar logado para realizar esta ação.',
                    confirmButtonColor: '#ccff00',
                    confirmButtonText: '<span style="color:black; font-weight:bold;">Login Agora</span>',
                    background: '#1a1a1a',
                    color: '#ffffff'
                });
                window.location.href = '/login/';
                throw new Error('Unauthorized');
            }
            
            if (!response.ok) {
                const error = await response.json().catch(() => ({}));
                throw new Error(error.detail || 'Erro na API');
            }

            return response.json();
        } catch (error) {
            if (error.message !== 'Unauthorized') {
                console.error('API Error:', error);
            }
            throw error;
        }
    },

    formatDate(dateString) {
        return dayjs(dateString).format('D MMMM YYYY');
    },

    timeSince(dateString) {
        return dayjs(dateString).fromNow();
    },
    
    truncate(text, length) {
        return text?.length > length ? text.substring(0, length) + '...' : text || '';
    },

    showToast(icon, title) {
        const Toast = Swal.mixin({
            toast: true,
            position: 'top-end',
            showConfirmButton: false,
            timer: 3000,
            timerProgressBar: true,
            background: '#1a1a1a',
            color: '#ffffff',
            didOpen: (toast) => {
                toast.addEventListener('mouseenter', Swal.stopTimer)
                toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
        });

        Toast.fire({
            icon: icon,
            title: title
        });
    },

    showError(message) {
        Swal.fire({
            icon: 'error',
            title: 'Oops...',
            text: message,
            background: '#1a1a1a',
            color: '#ffffff',
            confirmButtonColor: '#ccff00',
            confirmButtonText: '<span style="color:black; font-weight:bold;">OK</span>'
        });
    }
};
