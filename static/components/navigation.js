Vue.component('navigation', {
    props: {
        tabs: Array,
        /* 定义标签页列表，聊表项可以有二级子列表
        [
          {name: String, link: String, sublist: [{name: String, link: String}}]}
        ]*/

        activePath: [null, null]
        /* [激活的第一级列表项, 激活的第二级子列表项] null表示当前无激活*/
    } ,
    template: `
<nav class="navigation">
    <ul>
        <li v-for="(tab, ti) in tabs" :class="['tab', ti === activePath[0] ? 'active-tab':''">
            
        </li>
    </ul>
</nav>
    
    `
});