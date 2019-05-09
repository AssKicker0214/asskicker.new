Vue.component('navigation', {
    props: {
        tabs: Array,
        /* 定义标签页列表，聊表项可以有二级子列表
        [
          {name: String, link: String, sublist: [{name: String, link: String}}]}
        ]*/

        activePath: Array,
        /* [激活的第一级列表项, 激活的第二级子列表项] null表示当前无激活*/

        fold: Boolean,
        /* 折叠导航栏？ */
    } ,
    template: `
<nav :class="['navigation', fold?'nav-collapse':'nav-expand']">
    <div class="nav-folder">
    <button class="nav-toggle nav-toggle-expand fas fa-bars" @click="toggle()"></button>
    
    </div>
    <div class="nav-content">
        <button class="nav-toggle nav-toggle-collapse fas fa-chevron-left" @click="toggle()"></button>
        <header>
            <img class="nav-portrait" src="/static/assets/portrait.jpg">
            <div>
                <span><i class="fas fa-map-marker-alt"></i><span>南京,</span> </span>
                <span><i class="fas fa-code"></i><span>Coder</span> </span>
            </div>
        </header>
        <ul>
            <li v-for="(tab, ti) in tabs" 
            :class="['tab', ti === activePath[0] ? 'active-tab':'']">
                <a v-text="tab.name" :href="tab.link"></a>
            </li>
        </ul>
        <footer>
            <label>
                <a class="fab fa-github"
                    href="http://github.com/AssKicker0214">
                </a>
                <span>github</span>
            </label>
            <label>
                <a class="fas fa-envelope" 
                href="mailto:asskicker0214@outlook.com">
                </a>
                <span>email</span>
            </label>
        </footer>
    </div>
</nav>
    
    `,
    methods: {
        toggle: function () {
            this.$emit('toggle-nav')
        }
    }
});