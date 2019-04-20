Vue.component('article-card', {
    props: {
        title: String,
        createOn: Number,
        keywords: Array,
        aid: Number
    },
    template: `
<a class="article-card" :href="'/article/'+aid">
    <header>
        <span v-text="title"></span> 
        <small v-text="createTime()"></small>
    </header>
    <ul>
        <li v-for="kw in keywords" v-text="kw"></li>
    </ul>
</a>
    `,
    methods: {
        createTime: function () {
            const date = new Date(this.createOn * 1000);
            return `${date.getFullYear()}/${date.getMonth()}/${date.getDate()}`
            // return this.createOn+'';
        }
    }
});