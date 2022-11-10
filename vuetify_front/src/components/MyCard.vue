<template>
    <v-card :loading="loading" class="mx-auto my-12" max-width="374">

    <!-- <v-img
        max-height="2"
        max-width="2"
        src="{{ image }}"
    ></v-img> -->

    <v-card-title>{{ name }}</v-card-title>

    <v-card-text>
        <div class="my-4 text-subtitle-1">{{ quantity }}</div>
        <div class="my-4 text-subtitle-1">{{ brand }}</div>

    </v-card-text>

    <v-divider class="mx-4"></v-divider>

        <v-card-actions>
            <v-btn color="primary" text @click="reserve">
                <a :href="urlKey" />
            </v-btn>
        </v-card-actions>
    </v-card>
</template>

<script>
    export default {
        props: ['name, quantity, brand, urlKey'],
    }
</script>


//  computed: {
//             welcome() {
//                 return '${this.name}';
//             },
//         },