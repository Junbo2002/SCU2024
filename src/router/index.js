import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Music from "@/components/Music.vue";
import Data from "@/components/Data.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/",
            name: "home",
            component: Home,
        },
        {
            path: "/music",
            name: "music",
            component: Music,
        },
        {
            path: "/data",
            name: "data",
            component: Data,
        },
    ],
});

export default router;
