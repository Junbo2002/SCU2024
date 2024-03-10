import { createRouter, createWebHistory } from "vue-router";
import Home from "@/components/Home.vue";
import Music from "@/components/Music.vue";
import Data from "@/components/Data.vue";

import TrackRank from "@/components/rank/TrackRank.vue";
import PlaylistRank from "@/components/rank/AlbumRank.vue";
import ArtistRank from "@/components/rank/ArtistRank.vue";

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: "/home",
            name: "home",
            component: Home,
            children: [
                {
                    path: "trackrank",
                    name: "TrackRank",
                    component: TrackRank,
                },
                {
                    path: "playlistrank",
                    name: "PlaylistRank",
                    component: PlaylistRank,
                },
                {
                    path: "artistrank",
                    name: "ArtistRank",
                    component: ArtistRank,
                },
            ],
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
        {
            path: "/home/",
            redirect: "/home/trackrank",
        },
        {
            path: "/",
            redirect: "/home/trackrank",
        },
    ],
});

export default router;
