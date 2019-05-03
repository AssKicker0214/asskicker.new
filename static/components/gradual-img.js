Vue.component('gradual-img', {
    props: {
        src: String,
        id: String
    },
    template:
    `
<div class="gradual-img" :id="id">
    
</div>
    `,
    methods: {

    },
    created: function () {
        const img = new Image();
        img.style.transition = `3s`;
        img.src = this.src;
        img.onload = () => {//return;
            const container = document.querySelector(`#${this.id}`);
            const h = img.naturalHeight
                , w = img.naturalWidth;
            let r = Math.sqrt(h * h + w * w);
            img.style.filter = `blur(${r}px)`;
            img.style.opacity = `0`;
            container.appendChild(img);

            setTimeout(() => {
                img.style.opacity = '1';
                img.style.filter = `blur(0)`;
            }, 100);
        }
    }
});