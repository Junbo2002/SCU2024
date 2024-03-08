import { createRouter, createWebHistory } from "vue-router";
import ButtonTest from "../ButtonTest.vue";
import BorderTest from "../BorderTest.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: ButtonTest,
        },
        {
            path: "/about",
            name: "about",
            component: BorderTest,
        },
    ],
});

export default router;
