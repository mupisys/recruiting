function postDetail(postId) {
    return {
        post: null,
        comments: [],
        loading: true,
        newComment: '',
        submittingComment: false,
        replyToId: null,
        replyContent: '',
        submittingReply: false,

        async init() {
            try {
                const data = await Utils.fetchJSON(`/api/posts/${postId}/`);
                this.post = data;
                this.comments = data.comments || [];
            } catch (e) {
                console.error('Post fetch error:', e);
            } finally {
                this.loading = false;
            }
        },

        async likePost() {
            try {
                const data = await Utils.fetchJSON(`/api/posts/${postId}/like/`, { method: 'POST' });
                this.post.likes_count = data.total_likes;
                this.post.is_liked = data.liked;
            } catch (e) {
                console.error('Like error:', e);
            }
        },

        async submitComment() {
            if (!this.newComment.trim()) return;
            
            this.submittingComment = true;
            try {
                const comment = await Utils.fetchJSON(`/api/posts/${postId}/comment/`, {
                    method: 'POST',
                    body: JSON.stringify({ content: this.newComment })
                });
                this.comments.unshift(comment);
                this.newComment = '';
                Utils.showToast('success', 'Comentário postado!');
            } catch (e) {
                Utils.showError('Erro ao postar comentário');
            } finally {
                this.submittingComment = false;
            }
        },

        async submitReply(parentId) {
            if (!this.replyContent.trim()) return;

            this.submittingReply = true;
            try {
                const reply = await Utils.fetchJSON(`/api/posts/${postId}/comment/`, {
                    method: 'POST',
                    body: JSON.stringify({ 
                        content: this.replyContent,
                        parent: parentId 
                    })
                });
                
                // Find the parent comment and add the reply
                const parentComment = this.comments.find(c => c.id === parentId);
                if (parentComment) {
                    if (!parentComment.replies) parentComment.replies = [];
                    parentComment.replies.push(reply);
                }
                
                this.replyContent = '';
                this.replyToId = null;
                Utils.showToast('success', 'Resposta postada!');
            } catch (e) {
                Utils.showError('Erro ao postar resposta');
            } finally {
                this.submittingReply = false;
            }
        },

        formatDate: Utils.formatDate,
        timeSince: Utils.timeSince
    }
}
