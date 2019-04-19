Vue.component('article-card', {
    props: {
        title: String,
        createOn: String,
        keywords: Array,
    },
    template: `
<div class="article-card">
    <header>
        <h4 v-text="title"><small v-text="createOn"></small></h4> 
    </header>
    <ul>
        <li v-for="kw in keywords" v-text="kw"></li>
    </ul>
</div>
    `,
    methods: {

    }
});