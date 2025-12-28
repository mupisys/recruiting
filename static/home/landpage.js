function appData() {
    return {
        news: [],
        communityPosts: [],
        loading: true,
        newsNext: null,
        communityNext: null,

        init() {
            Promise.all([
                this.fetchPosts(true),
                this.fetchPosts(false)
            ]).finally(() => this.loading = false);
        },

        async fetchPosts(isOfficial, url = null) {
            try {
                const endpoint = url || `/api/posts/?is_official=${isOfficial}`;
                const data = await Utils.fetchJSON(endpoint);
                
                const results = data.results;
                const next = data.next;

                if (isOfficial) {
                    if (url) {
                        this.news = [...this.news, ...results];
                    } else {
                        this.news = results;
                    }
                    this.newsNext = next;
                } else {
                    if (url) {
                        this.communityPosts = [...this.communityPosts, ...results];
                    } else {
                        this.communityPosts = results;
                    }
                    this.communityNext = next;
                }
            } catch (e) {
                Utils.showError(`Error fetching ${isOfficial ? 'news' : 'posts'}`);
                console.error(e);
            }
        },
        
        loadMoreNews() {
            if (this.newsNext) {
                this.fetchPosts(true, this.newsNext);
            }
        },

        loadMoreCommunity() {
            if (this.communityNext) {
                this.fetchPosts(false, this.communityNext);
            }
        },

        async likePost(post) {
            try {
                const data = await Utils.fetchJSON(`/api/posts/${post.id}/like/`, { method: 'POST' });
                post.likes_count = data.total_likes;
                post.is_liked = !post.is_liked;
            } catch (e) {
                Utils.showError('Error liking post');
            }
        },
        
        formatDate: Utils.formatDate,
        timeSince: Utils.timeSince,
        truncate: Utils.truncate
    }
}
